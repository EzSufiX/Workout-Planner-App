function selectWorkout(clickedCard) {
  const cards = document.querySelectorAll('.selector');
  const isSelected = clickedCard.classList.contains('selected');

  // Remove 'selected' from all cards
  cards.forEach(card => card.classList.remove('selected'));

  // If it was not already selected, select it
  if (!isSelected) {
    clickedCard.classList.add('selected');
  }
}

async function fetchWorkouts() {
  const category = document.getElementById('category').value;
  const goal = document.getElementById('goal').value;
  const day = document.getElementById('day').value;

  const response = await fetch(`/api/workouts?category=${category}&goal=${goal}&day=${day}`);
  const workouts = await response.json();

  const list = document.getElementById('workout-list');
  list.innerHTML = workouts.map(
    w => `<li>${w.name}: ${w.sets} sets x ${w.reps}</li>`
  ).join('');
}

document.getElementById('category').onchange = fetchWorkouts;
document.getElementById('goal').onchange = fetchWorkouts;
document.getElementById('day').onchange = fetchWorkouts;

// Load initial workouts
fetchWorkouts();
