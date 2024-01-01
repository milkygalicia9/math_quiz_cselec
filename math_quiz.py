import random

class MathQuiz:
    def generate_question(self):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operator = random.choice(['+', '-', '*'])
        question = f"{num1} {operator} {num2}"
        answer = eval(question)
        return question, answer

def main():
    quiz = MathQuiz()
    score = 0
    num_questions = 5

    print("Welcome to Math Quiz!")

    for _ in range(num_questions):
        question, answer = quiz.generate_question()
        user_answer = input(f"What is {question}? ")

        try:
            user_answer = float(user_answer)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if user_answer == answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {answer}.")

    print(f"\nQuiz completed! Your score is {score}/{num_questions}.")

if __name__ == "__main__":
    main()
