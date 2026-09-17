# Write a program to create a quiz where the player answers multiple choice questions.
# The program should evaluate the player's answers & provide a score at the end

# Basic solution:

questions = [
    {
      "question": "What is the capital of France?",
      "options": {
        "a": "Paris",
        "b": "London",
        "c": "Rome"
      },
      "answer": "a",
      "category": "geography",
      "difficulty": "easy"
    },
    {
      "question": "What is the largest planet in our solar system?",
      "options": {
        "a": "Earth",
        "b": "Jupiter",
        "c": "Mars"
      },
      "answer": "b",
      "category": "science",
      "difficulty": "easy"
    },
    {
      "question": "In which year did World War II end?",
      "options": {
        "a": "1943",
        "b": "1945",
        "c": "1947"
      },
      "answer": "b",
      "category": "history",
      "difficulty": "medium"
    }
]

print("Answer the following question: ")

score = 0

for question in questions:
    # question = random.choice(questions)
    print(question["question"])

    options = (question["options"])
    for x, y in options.items():
        print(f"{x}) {y}")
        # print(y)

    # Ask user to answer & validate

    while True:
        user_answer = input("Select the right answer: 'a', 'b', or 'c': ").lower()

        if user_answer in options:
            print("valid choice... let's see if it's correct")
            break
        else:
            print("Please enter a valid answer: ")

    if user_answer == question["answer"]:
        print("correct!")
        score += 1
    else:
        print("incorrect!")


print(f"You answered {score} out of {len(questions)} questions correctly!")
