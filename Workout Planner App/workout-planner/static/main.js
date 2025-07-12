console.log("Script loaded");

let selectedCategory = "BODYWEIGHT"; // default
let allWorkouts = []; // Store fetched workouts

function selectWorkout(elem) {
  // Toggle selection
  if (elem.classList.contains('selected')) {
    elem.classList.remove('selected');
    selectedCategory = "";
  } else {
    // Remove selection from all buttons first
    document.querySelectorAll('.selector').forEach(div => {
      div.classList.remove('selected');
    });
    // Select clicked button
    elem.classList.add('selected');
    selectedCategory = elem.innerText.trim();
  }
}

document.querySelector('.generate-plan-btn').onclick = async function() {
  const goalSelect = document.getElementById('fitness-goal');
  const goal = goalSelect.value;
  const resultDiv = document.getElementById('workout-result');
  
  // Input validation
  if (!selectedCategory) {
    resultDiv.innerHTML = "<p>Please select a workout category first.</p>";
    return;
  }
  
  if (!goal) {
    resultDiv.innerHTML = "<p>Please select a fitness goal.</p>";
    return;
  }

  // Format parameters
  const category = selectedCategory.charAt(0).toUpperCase() + selectedCategory.slice(1).toLowerCase();
  const apiGoal = goal === "Lose Fat" ? "Loss Fat" : goal;
  const days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"];
  
  resultDiv.innerHTML = "<p>Loading workouts...</p>";
  allWorkouts = []; // Reset storage

  try {
    // Fetch workouts for each day
    for (const day of days) {
      const url = `/api/workouts?category=${encodeURIComponent(category)}&goal=${encodeURIComponent(apiGoal)}&day=${encodeURIComponent(day)}`;
      
      const res = await fetch(url);
      if (!res.ok) {
        const error = await res.json().catch(() => ({ message: 'Failed to fetch workouts' }));
        throw new Error(error.message || `Network response was not ok for ${day}`);
      }
      
      const data = await res.json();
      if (data.data && Object.keys(data.data).length > 0) {
        allWorkouts.push({ 
          day: day, 
          workouts: data.data[day] || data.data // Handle both formats
        });
      }
    }
    
    if (allWorkouts.length === 0) {
      resultDiv.innerHTML = `<p>No workouts found for ${category} - ${apiGoal}.</p>`;
      return;
    }
    
    // Display workouts by day
    resultDiv.innerHTML = `
      <h2>${category} - ${apiGoal}</h2>
      ${allWorkouts.map(dayWorkouts => `
        <div class="day-plan">
          <h3>${dayWorkouts.day}</h3>
          <ul>
            ${dayWorkouts.workouts.map(w => `
              <li>${w.name}: ${w.sets} sets × ${w.reps}</li>
            `).join('')}
          </ul>
        </div>
      `).join('')}
    `;
    
  } catch (error) {
    console.error('Error fetching workouts:', error);
    resultDiv.innerHTML = `<p>Error: ${error.message}</p>`;
  }
};

document.addEventListener('DOMContentLoaded', function() {
    const workoutTypeContainer = document.getElementById('workout-type-buttons');
    const goalContainer = document.getElementById('goal-buttons');
    const generateBtn = document.getElementById('generate-btn');
    const resultContainer = document.getElementById('workout-result');
    
    let selectedWorkoutType = null;
    let selectedGoal = null;
    
    // Load workout types
    fetch('/get_workout_types')
        .then(response => response.json())
        .then(types => {
            types.forEach(type => {
                const btn = document.createElement('button');
                btn.textContent = type;
                btn.addEventListener('click', () => selectWorkoutType(type, btn));
                workoutTypeContainer.appendChild(btn);
            });
        });
    
    function selectWorkoutType(type, button) {
        selectedWorkoutType = type;
        
        // Update UI
        document.querySelectorAll('#workout-type-buttons button').forEach(btn => {
            btn.classList.remove('active');
        });
        button.classList.add('active');
        
        // Load goals for this workout type
        fetch(`/get_goals/${type}`)
            .then(response => response.json())
            .then(goals => {
                goalContainer.innerHTML = '';
                goals.forEach(goal => {
                    const btn = document.createElement('button');
                    btn.textContent = goal;
                    btn.addEventListener('click', () => selectGoal(goal, btn));
                    goalContainer.appendChild(btn);
                });
                
                generateBtn.disabled = true;
                selectedGoal = null;
            });
    }
    
    function selectGoal(goal, button) {
        selectedGoal = goal;
        
        // Update UI
        document.querySelectorAll('#goal-buttons button').forEach(btn => {
            btn.classList.remove('active');
        });
        button.classList.add('active');
        
        generateBtn.disabled = false;
    }
    
    generateBtn.addEventListener('click', generatePlan);
    
    function generatePlan() {
        if (!selectedWorkoutType || !selectedGoal) return;
        
        fetch(`/get_plan/${selectedWorkoutType}/${selectedGoal}`)
            .then(response => response.json())
            .then(plan => {
                renderWorkoutPlan(plan);
            });
    }
    
    function renderWorkoutPlan(plan) {
        resultContainer.innerHTML = `
            <h2>${plan.title}</h2>
            <div class="week-container"></div>
        `;
        
        const weekContainer = resultContainer.querySelector('.week-container');
        
        plan.days.forEach(day => {
            const dayCard = document.createElement('div');
            dayCard.className = 'day-card';
            
            dayCard.innerHTML = `
                <h3 class="day-title">${day.name}</h3>
                <ul class="exercise-list"></ul>
            `;
            
            const exerciseList = dayCard.querySelector('.exercise-list');
            
            if (day.exercises.length > 0) {
                day.exercises.forEach(exercise => {
                    const item = document.createElement('li');
                    item.className = 'exercise-item';
                    item.textContent = `${exercise.name}: ${exercise.sets} sets x ${exercise.reps}`;
                    exerciseList.appendChild(item);
                });
            } else {
                const item = document.createElement('li');
                item.className = 'empty-day';
                item.textContent = 'Rest day';
                exerciseList.appendChild(item);
            }
            
            weekContainer.appendChild(dayCard);
        });
    }
});
