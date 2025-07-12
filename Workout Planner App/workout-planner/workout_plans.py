from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

# Your workoutPlans data (convert JS object to Python dict)
workoutPlans = {
    # ...PASTE YOUR PYTHON DICT VERSION OF THE workoutPlans DATA HERE...

    "Bodyweight": {
        "Build Muscle": { 
            "Monday": [
                {"name": "Push-ups", "sets": 4, "reps": 12},
                {"name": "Bulgarian Split Squats", "sets": 3, "reps": 10},
                {"name": "Diamond Push-ups", "sets": 3, "reps": 8}
          ],
            "Tuesday": [
                {"name": "Pull-ups", "sets": 4, "reps": 8},
                {"name": "Pike Push-ups", "sets": 3, "reps": 10},
                {"name": "Plank", "sets": 3, "reps": "45 sec"}
            ],
            "Wednesday": [
                {"name": "Squats", "sets": 4, "reps": 15},
                {"name": "Lunges", "sets": 3, "reps": 12},
                {"name": "Leg Raises", "sets": 3, "reps": 12}
            ],
            "Thursday": [
                {"name": "Dips (Chair/Bench)", "sets": 4, "reps": 10},
                {"name": "Decline Push-ups", "sets": 3, "reps": 8},
                {"name": "Side Plank", "sets": 3, "reps": "30 sec"}
            ],
            "Friday": [
                {"name": "Chin-ups", "sets": 4, "reps": 8},
                {"name": "Jump Squats", "sets": 3, "reps": 12},
                {"name": "Mountain Climbers", "sets": 3, "reps": 20}
            ]
        },
        "Functional Strength": {
            "Monday": [
                {"name": "Push-ups", "sets": 5, "reps": 10},
                {"name": "Plank", "sets": 3, "reps": "1 min"},
                {"name": "Squat Jumps", "sets": 4, "reps": 15}
            ],
            "Tuesday": [
                {"name": "Pull-ups", "sets": 5, "reps": 6},
                {"name": "Reverse Lunges", "sets": 3, "reps": 12},
                {"name": "Bear Crawl", "sets": 3, "reps": "30 sec"}
            ],
            "Wednesday": [
                {"name": "Single-leg Romanian Deadlift", "sets": 3, "reps": 10},
                {"name": "Push-up to T", "sets": 3, "reps": 8},
                {"name": "Wall Sit", "sets": 3, "reps": "45 sec"}
            ],
            "Thursday": [
                {"name": "Dips", "sets": 4, "reps": 10},
                {"name": "Side Lunges", "sets": 3, "reps": 12},
                {"name": "Superman", "sets": 3, "reps": 15}
            ],
            "Friday": [
                {"name": "Plank Up-downs", "sets": 3, "reps": 12},
                {"name": "Jumping Lunges", "sets": 3, "reps": 15},
                {"name": "Mountain Climbers", "sets": 3, "reps": 20}
            ]
        },
        "Loss Fat": {
            "Monday": [
                {"name": "Burpees", "sets": 4, "reps": 20},
                {"name": "Jumping Jacks", "sets": 3, "reps": 30},
                {"name": "Mountain Climbers", "sets": 3, "reps": 20}
            ],
            "Tuesday": [
                {"name": "High Knees", "sets": 4, "reps": "40 sec"},
                {"name": "Squat Jumps", "sets": 3, "reps": 20},
                {"name": "Plank", "sets": 3, "reps": "45 sec"}
            ],
            "Wednesday": [
                {"name": "Push-ups", "sets": 3, "reps": 15},
                {"name": "Lunges", "sets": 4, "reps": 12},
                {"name": "Jump Rope", "sets": 3, "reps": "1 min"}
            ],
            "Thursday": [
                {"name": "Mountain Climbers", "sets": 4, "reps": 25},
                {"name": "Plank Jacks", "sets": 3, "reps": 20},
                {"name": "Flutter Kicks", "sets": 3, "reps": 30}
            ],
            "Friday": [
                {"name": "Burpees", "sets": 4, "reps": 15},
                {"name": "Sit-ups", "sets": 3, "reps": 20},
                {"name": "Jumping Lunges", "sets": 3, "reps": 12}
            ]
        }
    },
    "Gym": {
        "Build Muscle": {
            "Monday": [
                {"name": "Barbell Bench Press", "sets": 4, "reps": 10},
                {"name": "Incline Dumbbell Press", "sets": 3, "reps": 12},
                {"name": "Triceps Pushdown", "sets": 3, "reps": 12}
            ],
            "Tuesday": [
                {"name": "Barbell Squats", "sets": 4, "reps": 8},
                {"name": "Leg Press", "sets": 3, "reps": 12},
                {"name": "Hamstring Curl", "sets": 3, "reps": 12}
            ],
            "Wednesday": [
                {"name": "Lat Pulldown", "sets": 4, "reps": 10},
                {"name": "Seated Row", "sets": 3, "reps": 12},
                {"name": "Bicep Curl", "sets": 3, "reps": 15}
            ],
            "Thursday": [
                {"name": "Shoulder Press", "sets": 4, "reps": 10},
                {"name": "Lateral Raise", "sets": 3, "reps": 12},
                {"name": "Face Pull", "sets": 3, "reps": 15}
            ],
            "Friday": [
                {"name": "Deadlift", "sets": 4, "reps": 6},
                {"name": "Farmer’s Walk", "sets": 3, "reps": "30 meters"},
                {"name": "Plank", "sets": 3, "reps": "1 min"}
            ]
        },
        "Functional Strength": {
            "Monday": [
                {"name": "Barbell Squat", "sets": 5, "reps": 5},
                {"name": "Pull-ups", "sets": 4, "reps": 8},
                {"name": "Farmer’s Walk", "sets": 4, "reps": "30 meters"}
            ],
            "Tuesday": [
                {"name": "Deadlift", "sets": 5, "reps": 5},
                {"name": "Hanging Leg Raise", "sets": 4, "reps": 10},
                {"name": "Push-ups", "sets": 3, "reps": 15}
            ],
            "Wednesday": [
                {"name": "Bench Press", "sets": 5, "reps": 5},
                {"name": "Barbell Row", "sets": 4, "reps": 8},
                {"name": "Plank", "sets": 4, "reps": "1 min"}
            ],
            "Thursday": [
                {"name": "Overhead Press", "sets": 5, "reps": 5},
                {"name": "Face Pull", "sets": 3, "reps": 15},
                {"name": "Dips", "sets": 3, "reps": 12}
            ],
            "Friday": [
                {"name": "Trap Bar Deadlift", "sets": 4, "reps": 8},
                {"name": "Walking Lunges", "sets": 3, "reps": 12},
                {"name": "Russian Twists", "sets": 3, "reps": 20}
            ]
        },
        "Loss Fat": {
            "Monday": [
                {"name": "Treadmill HIIT", "sets": 10, "reps": "1 min sprint/2 min walk"},
                {"name": "Push-ups", "sets": 3, "reps": 20},
                {"name": "Jump Rope", "sets": 3, "reps": "2 min"}
            ],
            "Tuesday": [
                {"name": "Rowing Machine", "sets": 4, "reps": "5 min"},
                {"name": "Box Jumps", "sets": 3, "reps": 15},
                {"name": "Sit-ups", "sets": 3, "reps": 20}
            ],
            "Wednesday": [
                {"name": "Bike Sprints", "sets": 10, "reps": "30 sec sprint/1 min rest"},
                {"name": "Burpees", "sets": 4, "reps": 15},
                {"name": "Mountain Climbers", "sets": 3, "reps": 30}
            ],
            "Thursday": [
                {"name": "Circuit: Squat/Deadlift/Row", "sets": 3, "reps": 12},
                {"name": "Plank", "sets": 3, "reps": "1 min"},
                {"name": "Jumping Jacks", "sets": 3, "reps": 30}
            ],
            "Friday": [
                {"name": "Stairmaster", "sets": 4, "reps": "5 min"},
                {"name": "Russian Twists", "sets": 3, "reps": 25},
                {"name": "Push-ups", "sets": 3, "reps": 20}
            ]
        }
    },
    "Hybrid": {
        "Build Muscle": {
            "Monday": [
                {"name": "Push-ups", "sets": 4, "reps": 12},
                {"name": "Dumbbell Bench Press", "sets": 3, "reps": 10},
                {"name": "Squats", "sets": 4, "reps": 15}
            ],
            "Tuesday": [
                {"name": "Pull-ups", "sets": 4, "reps": 8},
                {"name": "Barbell Row", "sets": 3, "reps": 10},
                {"name": "Mountain Climbers", "sets": 3, "reps": 20}
            ],
            "Wednesday": [
                {"name": "Deadlift", "sets": 4, "reps": 8},
                {"name": "Lunges", "sets": 3, "reps": 12},
                {"name": "Leg Raises", "sets": 3, "reps": 12}
            ],
            "Thursday": [
                {"name": "Shoulder Press", "sets": 4, "reps": 10},
                {"name": "Plank", "sets": 3, "reps": "1 min"},
                {"name": "Burpees", "sets": 3, "reps": 15}
            ],
            "Friday": [
                {"name": "Chin-ups", "sets": 3, "reps": 10},
                {"name": "Jump Squats", "sets": 3, "reps": 15},
                {"name": "Dumbbell Curl", "sets": 3, "reps": 12}
            ]
        },
        "Functional Strength": {
            "Monday": [
                {"name": "Kettlebell Swings", "sets": 4, "reps": 15},
                {"name": "Push-ups", "sets": 3, "reps": 15},
                {"name": "Barbell Squat", "sets": 3, "reps": 8}
            ],
            "Tuesday": [
                {"name": "Pull-ups", "sets": 4, "reps": 8},
                {"name": "Farmer’s Walk", "sets": 3, "reps": "30 meters"},
                {"name": "Lunges", "sets": 3, "reps": 12}
            ],
            "Wednesday": [
                {"name": "Deadlift", "sets": 4, "reps": 6},
                {"name": "Plank", "sets": 4, "reps": "1 min"},
                {"name": "Jump Rope", "sets": 3, "reps": "1 min"}
            ],
            "Thursday": [
                {"name": "Overhead Press", "sets": 3, "reps": 10},
                {"name": "Bear Crawl", "sets": 3, "reps": "30 sec"},
                {"name": "Single-leg Squat", "sets": 3, "reps": 8}
            ],
            "Friday": [
                {"name": "Box Jumps", "sets": 3, "reps": 15},
                {"name": "Russian Twists", "sets": 3, "reps": 20},
                {"name": "Sit-ups", "sets": 3, "reps": 20}
            ]
        },
        "Loss Fat": {
            "Monday": [
                {"name": "Burpees", "sets": 4, "reps": 20},
                {"name": "Kettlebell Thrusters", "sets": 3, "reps": 15},
                {"name": "Jump Lunges", "sets": 3, "reps": 20}
            ],
            "Tuesday": [
                {"name": "Mountain Climbers", "sets": 3, "reps": 30},
                {"name": "Push-ups", "sets": 3, "reps": 20},
                {"name": "Jump Rope", "sets": 3, "reps": "1 min"}
            ],
            "Wednesday": [
                {"name": "HIIT: Sprint/Walk", "sets": 8, "reps": "30 sec sprint/1 min walk"},
                {"name": "Bodyweight Dips", "sets": 3, "reps": 15},
                {"name": "Plank", "sets": 3, "reps": "1 min"}
            ],
            "Thursday": [
                {"name": "Rowing Machine", "sets": 3, "reps": "10 min"},
                {"name": "Box Jumps", "sets": 3, "reps": 15},
                {"name": "Sit-ups", "sets": 3, "reps": 20}
            ],
            "Friday": [
                {"name": "Jumping Jacks", "sets": 4, "reps": 30},
                {"name": "Bicycle Crunches", "sets": 3, "reps": 25},
                {"name": "Push-ups", "sets": 3, "reps": 20}
            ]
        }
    }

}

