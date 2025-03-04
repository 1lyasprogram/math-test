import random

def generate_math_question(a, b):
    num1 = random.randint(a, b)
    num2 = random.randint(a, b)
    operator = random.choice(['+', '-', '*', '/'])
    question = f"{num1} {operator} {num2}"
    return question

print(generate_math_question(1, 10))

# Проверка ответа пользователя на правильность
def check_answer(question, userAnswer):
    try:
        userAnswer = float(userAnswer)
        if userAnswer == eval(question):
            return True
        else:
            return False
    except ValueError:
        return False

print(check_answer("2 + 3", "5"))
print(check_answer("5 * 3", "10"))
print(check_answer("10-3", "семь"))


def math_quiz(number_of_questions=5):
    print("Добро пожаловать в математический тест!")
    correct_answers = 0

    for i in range(number_of_questions):
        question = generate_math_question(1, 5)
        userAnswer = input(f'{question} = ')
        if check_answer(question, userAnswer) == True:
            correct_answers += 1


    print("Тест завершен.")
    print(f"Вы правильно решили {correct_answers} из {number_of_questions} вопросов.")

    if correct_answers >= number_of_questions * 0.8:
        print("Отлично! Вы получаете оценку A.")
    elif correct_answers >= number_of_questions * 0.6:
        print("Хорошо! Вы получаете оценку B.")
    else:
        print("Попробуйте еще раз. Вы получаете оценку C.")


# Запуск теста
math_quiz(7)