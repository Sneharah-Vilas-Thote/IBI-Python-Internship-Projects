# ✅ Calculator-App (calculator.py)

def calculator():
    print("Simple Calculator")
    print("Operations: +  -  *  /")
    num1 = float(input("Enter first number: "))
    op = input("Enter operator: ")
    num2 = float(input("Enter second number: "))

    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"
    else:
        result = "Invalid operator"

    print("Result:", result)

calculator()


# ✅ Weather-Forecast-App (weather_forecast.py)

import requests

def get_weather(city):
    api_key = "https://wttr.in/"
    url = f"{api_key}{city}?format=3"
    response = requests.get(url)
    if response.status_code == 200:
        print("Weather:", response.text)
    else:
        print("Error fetching weather data")

city = input("Enter city name: ")
get_weather(city)


# ✅ Todo-List-App (todo_list.py)

todo_list = []

while True:
    print("\nTo-Do List:")
    for i, task in enumerate(todo_list, 1):
        print(f"{i}. {task}")

    print("\nOptions: 1.Add  2.Remove  3.Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter task: ")
        todo_list.append(task)
    elif choice == '2':
        task_num = int(input("Enter task number to remove: "))
        if 0 < task_num <= len(todo_list):
            todo_list.pop(task_num - 1)
    elif choice == '3':
        break
    else:
        print("Invalid choice")


# ✅ QR-Code-Generator (qr_code_generator.py)

import qrcode

link = input("Enter the URL or text to generate QR code: ")
qr = qrcode.make(link)
qr.save("my_qrcode.png")
print("QR Code generated and saved as 'my_qrcode.png'")
