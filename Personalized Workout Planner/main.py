import random

def generate_workout(goal):
    workouts = {
        "weight_loss": ["Jumping Jacks", "Burpees", "Mountain Climbers"],
        "muscle_building": ["Push-ups", "Pull-ups", "Deadlifts"],
        "flexibility": ["Yoga", "Stretching", "Pilates"]
    }
    return random.choice(workouts.get(goal, []))

goal = input("Enter your fitness goal (weight_loss, muscle_building, flexibility): ").lower()
print(f"Today's workout: {generate_workout(goal)}")
