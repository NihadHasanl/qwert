
import logging
logging.basicConfig(level=logging.DEBUG , filename="logs.txt" , filemode="w")
def calculator():

    try:
        num1 = float(input("Введите первое число: "))
        operator = input("Выберите операцию (+, -, *, /): ")
        num2 = float(input("Введите второе число: "))

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                logging.error("Ошибка: Деление на ноль недопустимо.")
                return
            result = num1 / num2
        else:
            logging.error("Ошибка: Неправильная операция. Выберите +, -, *, или /.")
            return

        print(f"Результат: {result}")

    except :
        logging.error("Ошибка: Введите корректные числа.")

if __name__ == "__main__":
    calculator()

