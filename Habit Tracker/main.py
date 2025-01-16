import json

habits = {}

def add_habit(habit):
    habits[habit] = 0

def complete_habit(habit):
    if habit in habits:
        habits[habit] += 1
    else:
        print("Habit not found.")

def view_habits():
    for habit, streak in habits.items():
        print(f"{habit}: {streak} day(s)")

while True:
    action = input("Enter action (add, complete, view, quit): ").lower()
    if action == "add":
        add_habit(input("Enter habit: "))
    elif action == "complete":
        complete_habit(input("Enter habit: "))
    elif action == "view":
        view_habits()
    elif action == "quit":
        break