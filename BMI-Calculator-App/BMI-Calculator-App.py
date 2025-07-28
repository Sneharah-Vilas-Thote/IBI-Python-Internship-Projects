# BMI-Calculator-App.py

"""
BMI Calculator App
---------------------
This app takes user input for height and weight, calculates the BMI, and tells the user their body category.
"""

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("📏 Welcome to the BMI Calculator App!")
    try:
        weight = float(input("Enter your weight in kilograms (kg): "))
        height = float(input("Enter your height in meters (m): "))

        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)

        print(f"\nYour BMI is: {bmi}")
        print(f"Category: {category}")

    except ValueError:
        print("❌ Please enter valid numerical values for weight and height.")

# Run the app
if __name__ == "__main__":
    main()
