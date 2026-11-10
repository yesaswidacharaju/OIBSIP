
# BMI Calculator
# Oasis Infobyte Python Internship - Task 2

try:
    # Get user input
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in metres: "))

    # Validate input
    if weight <= 0 or height <= 0:
        print("Error: Weight and height must be positive numbers.")

    else:
        # Calculate BMI
        bmi = weight / (height ** 2)

        # Display BMI
        print("\nYour BMI is:", round(bmi, 2))

        # Classify BMI
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        print("BMI Category:", category)

except ValueError:
    print("Error: Please enter valid numeric values.")
