quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["1. Berlin", "2. Madrid", "3. Paris", "4. Rome"],
        "answer": 3  # Correct option number
    },
    {
        "question": "Which programming language is known as the 'language of the web'?",
        "options": ["1. Python", "2. Java", "3. HTML", "4. JavaScript"],
        "answer": 4
    },
    {
        "question": "Who is the founder of Microsoft?",
        "options": ["1. Steve Jobs", "2. Bill Gates", "3. Elon Musk", "4. Larry Page"],
        "answer": 2
    },
    {
        "question": "What does RAM stand for?",
        "options": ["1. Read Access Memory", "2. Random Access Memory", "3. Runtime Application Manager", "4. Read-Only Memory"],
        "answer": 2
    },
    {
        "question": "Which data type is immutable in Python?",
        "options": ["1. List", "2. Dictionary", "3. String", "4. Set"],
        "answer": 3
    },
    {
        "question": "What is the result of 5 + 3 * 2 in Python?",
        "options": ["1. 16", "2. 13", "3. 11", "4. 10"],
        "answer": 3
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["1. func", "2. define", "3. def", "4. function"],
        "answer": 3
    },
    {
        "question": "What does 'HTML' stand for?",
        "options": ["1. HyperText Markup Language", "2. HighText Machine Language", "3. HyperText Machine Language", "4. HighText Markup Language"],
        "answer": 1
    },
    {
        "question": "Which company developed the Java programming language?",
        "options": ["1. Microsoft", "2. Sun Microsystems", "3. Google", "4. Oracle"],
        "answer": 2
    },
    {
        "question": "Which of the following is not a Python framework?",
        "options": ["1. Flask", "2. Spring", "3. Django", "4. Pyramid"],
        "answer": 2
    }
]
def run_quiz(quiz_data):
    score = 0
    for i, item in enumerate(quiz_data, start=1):
        print(f"Question {i}: {item['question']}")
        for option in item['options']:
            print(option)
        
        try:
            answer = int(input("Enter your answer (1/2/3/4): "))
            if answer == item['answer']:
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong! The correct answer was {item['answer']}.\n")
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 4.\n")
    
    print(f"Your final score is {score}/{len(quiz_data)}.")

# Run the quiz
run_quiz(quiz_data)
