questions = [
    {
        "prompt": "What is the capital of France?",
        "options": ["1. Berlin", "2. Madrid", "3. Paris", "4. Rome"],
        "answer": 3
    },
    {
        "prompt": "What is 5 + 3?",
        "options": ["1. 5", "2. 8", "3. 10", "4. 15"],
        "answer": 2
    },
    {
        "prompt": "Which programming language is known as 'snake'?",
        "options": ["1. Python", "2. Java", "3. C++", "4. Ruby"],
        "answer": 1
    },
    {
        "prompt": "What is the output of `2 ** 3` in Python?",
        "options": ["1. 6", "2. 8", "3. 9", "4. 10"],
        "answer": 2
    },
    {
        "prompt": "Which planet is known as the Red Planet?",
        "options": ["1. Venus", "2. Mars", "3. Jupiter", "4. Saturn"],
        "answer": 2
    },
    {
        "prompt": "Who wrote 'Romeo and Juliet'?",
        "options": ["1. William Shakespeare", "2. Charles Dickens", "3. J.K. Rowling", "4. Mark Twain"],
        "answer": 1
    },
    {
        "prompt": "What is the chemical symbol for water?",
        "options": ["1. O2", "2. CO2", "3. H2O", "4. NaCl"],
        "answer": 3
    },
    {
        "prompt": "Which animal is known as the King of the Jungle?",
        "options": ["1. Elephant", "2. Lion", "3. Tiger", "4. Bear"],
        "answer": 2
    },
    {
        "prompt": "What is the largest planet in the Solar System?",
        "options": ["1. Earth", "2. Jupiter", "3. Saturn", "4. Uranus"],
        "answer": 2
    },
    {
        "prompt": "Which gas do plants absorb during photosynthesis?",
        "options": ["1. Oxygen", "2. Nitrogen", "3. Carbon dioxide", "4. Hydrogen"],
        "answer": 3
    },
    {
        "prompt": "Which country is known as the Land of the Rising Sun?",
        "options": ["1. China", "2. Japan", "3. Thailand", "4. India"],
        "answer": 2
    },
    {
        "prompt": "What is the square root of 64?",
        "options": ["1. 6", "2. 7", "3. 8", "4. 9"],
        "answer": 3
    },
    {
        "prompt": "What does HTML stand for?",
        "options": ["1. Hyperlinks and Text Markup Language", "2. Hyper Text Markup Language", "3. Home Tool Markup Language", "4. None of the above"],
        "answer": 2
    },
    {
        "prompt": "Which programming language is best for AI?",
        "options": ["1. Python", "2. C#", "3. JavaScript", "4. PHP"],
        "answer": 1
    },
    {
        "prompt": "What is the main ingredient in bread?",
        "options": ["1. Sugar", "2. Salt", "3. Flour", "4. Milk"],
        "answer": 3
    },
    {
        "prompt": "Who painted the Mona Lisa?",
        "options": ["1. Pablo Picasso", "2. Leonardo da Vinci", "3. Vincent van Gogh", "4. Michelangelo"],
        "answer": 2
    },
    {
        "prompt": "What is the smallest prime number?",
        "options": ["1. 1", "2. 2", "3. 3", "4. 5"],
        "answer": 2
    },
    {
        "prompt": "What is the hardest natural substance on Earth?",
        "options": ["1. Gold", "2. Iron", "3. Diamond", "4. Platinum"],
        "answer": 3
    },
    {
        "prompt": "Which country is known for its tulips?",
        "options": ["1. Netherlands", "2. Switzerland", "3. Denmark", "4. Belgium"],
        "answer": 1
    },
    {
        "prompt": "Which is the longest river in the world?",
        "options": ["1. Amazon", "2. Nile", "3. Ganges", "4. Yangtze"],
        "answer": 2
    },
    {
        "prompt": "What is the boiling point of water at sea level?",
        "options": ["1. 50°C", "2. 75°C", "3. 100°C", "4. 125°C"],
        "answer": 3
    },
    {
        "prompt": "What is the national currency of Japan?",
        "options": ["1. Yen", "2. Won", "3. Rupee", "4. Dollar"],
        "answer": 1
    },
    {
        "prompt": "Which element has the chemical symbol 'O'?",
        "options": ["1. Oxygen", "2. Osmium", "3. Gold", "4. Silver"],
        "answer": 1
    },
    {
        "prompt": "Who discovered penicillin?",
        "options": ["1. Alexander Fleming", "2. Marie Curie", "3. Isaac Newton", "4. Albert Einstein"],
        "answer": 1
    },
    {
        "prompt": "What is the result of 9 * 9?",
        "options": ["1. 72", "2. 81", "3. 90", "4. 99"],
        "answer": 2
    },
]

def run_quiz(questions):
    score=0
    for question in questions:
        print(question['prompt'])
        for option in question['options']:
            print(option)
        answer=int(input("Enter your answer:(1,2,3,4)"))
        if answer == question["answer"]:
            print("Your answer is correct") 
            score+=1
        else:
            print(f"Wrong ,LOSERRR the correct answer is ",(question['answer']))     
    print(f"you score{score} out of {len(questions)} question correct")          

run_quiz(questions)