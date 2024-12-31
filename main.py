import random

def generate_equation():
    #Generates a random equation in the form 'a * x = b'
    a = random.randint(1, 10)  # Random multiplier
    x = random.randint(1, 10)  # Random solution
    b = a * x  # Calculate the result
    return a, x, b

def ask_question(a, b):
    #Displays the question and gets user's answer
    print(f"Solve the equation: {a} * x = {b}")
    user_answer = int(input("What is x? "))
    return user_answer

def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        print("Well done, right answer!")
        return True
    else:
        print(f"Incorrect answer. The correct answer is {correct_answer}.")
        return False

def math_quiz():
    #Initialise the score
    score = 0 
    #Number of questions to ask
    num_questions = 5

    for i in range(num_questions):
        # Generate a new equation
        a, x, b = generate_equation()

        # Ask the question and get the user's anser
        user_answer = ask_question(a, b)

        # Check if the user's answer is correct
        if check_answer(user_answer, x):
            score +=1

    print(f"Quiz Over. Your final score is {score}/{num_questions}.")

if __name__ == "__main__":
            print("Welcome to the Math Quiz!")
            math_quiz()