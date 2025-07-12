from flask import Flask, render_template, request, jsonify
from flask_cors import CORS  # Add this import


app = Flask(__name__)
CORS(app) 

from workout_plans import workoutPlans  # Import the dictionary

 


@app.route('/')
def home():
    return render_template('index.html')
    

@app.route('/get_workout_types')
def get_workout_types():
    return jsonify(list(workoutPlans.keys()))

@app.route('/get_goals/<workout_type>')
def get_goals(workout_type):
    if workout_type in workoutPlans:
        return jsonify(list(workoutPlans[workout_type].keys()))
    return jsonify([])

@app.route('/get_plan/<workout_type>/<goal>')
def get_plan(workout_type, goal):
    if workout_type in workoutPlans and goal in workoutPlans[workout_type]:
        plan = workoutPlans[workout_type][goal]
        
        # Convert to list of days for consistent ordering
        days_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        ordered_plan = [{
            "name": day,
            "exercises": plan[day]
        } for day in days_order]
        
        return jsonify({
            "title": f"{workout_type} - {goal}",
            "days": ordered_plan
        })
    return jsonify({"error": "Plan not found"}), 404



@app.route('/test')
def test():
    return "Basic route works!"

@app.route('/api/workouts', methods=['GET'])
def get_workouts():
    try:
        category = request.args.get('category', '').strip().title()
        goal = request.args.get('goal', '').strip().title()
        day = request.args.get('day', '').strip()

         # If no day specified, return all days
        if not day:
            all_workouts = {}
            category_data = workoutPlans.get(category, {})
            goal_data = category_data.get(goal, {})
            
            for day_name, workouts in goal_data.items():
                if workouts:  # Only include days with workouts
                    all_workouts[day_name] = workouts
            
            if not all_workouts:
                return jsonify({"error": "No workouts found"}), 404
                
            return jsonify({
                "status": "success",
                "data": all_workouts,
                "category": category,
                "goal": goal
            })
        
        # If specific day requested
        workouts = workoutPlans.get(category, {}).get(goal, {}).get(day)
        
        if not workouts:
            return jsonify({"error": "No workouts found"}), 404

        return jsonify({
            "status": "success",
            "data": {day: workouts},
            "category": category,
            "goal": goal,
            "day": day
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500
 

if __name__ == '__main__':
    app.run(debug=True, port=5000)