import random

def rock_paper_scissors():
    choices = ["камень", "ножницы", "бумага"]
    user_choice = input("Выберите: камень, ножницы или бумага: ").lower()
    if user_choice not in choices:
        return "Неверный выбор!"
    computer_choice = random.choice(choices)
    print(f"Компьютер выбрал: {computer_choice}")
    if user_choice == computer_choice:
        return "Ничья!"
    elif (user_choice == "камень" and computer_choice == "ножницы") or \
         (user_choice == "ножницы" and computer_choice == "бумага") or \
         (user_choice == "бумага" and computer_choice == "камень"):
        return "Вы победили!"
    return "Компьютер победил!"

print(rock_paper_scissors())