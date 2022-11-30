# 2_BMI_Calculator.py

### WARNING ###
# This is only a tool to be used for educational purposes for python coding.

# Formula retrieved from 'https://www.nhlbi.nih.gov/health/educational/lose_wt/BMI/bmi-m.htm'
# BMI = Weight(Kg) / Height(M)^2

# Copy and paste this code to your text editor / IDE and start making dilutions in your lab.
# This is written in a 'while' loop, just in case you are entering information for more than one person.
# Enter 'q' to exit loop!

# Eg. INPUT
  # Enter your weight in Kilograms: 94
  # Enter your height in Meters: 1.95
  
# Eg. OUTPUT
  # Your BMI is 24.720578566732414, you are within a 'normal weight' range.
  # Visualization

import matplotlib.pyplot as plt

while True:
    print("\nEnter 'q' at any time to exit!")
    weight = float(input("Enter your weight in Kilograms: "))
    if weight == 'q':
        break
    height = float(input("Enter your height in Meters: "))
    if height == 'q':
        break

    BMI = weight / (height ** 2 )

    if BMI <= 18.5:
        print(f"Your BMI is {BMI}, you are considered to be 'underweight'.")
    elif BMI < 24.9:
        print(f"Your BMI is {BMI}, you are within a 'normal weight' range.")
    elif BMI < 29.9:
        print(f"Your BMI is {BMI}, you are considered 'overweight'.")
    else:
        print(f"Your BMI is {BMI}, you are considered 'obese'.")
        break

    x_axis = ("Underweight", "Normal", "Overweight", "Obese", "YOU")
    y_axis = [18.5,24.9, 29.9, 40, float(BMI)]
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.scatter(x_axis, y_axis, c=y_axis, cmap = plt.cm.YlOrRd,s=1000, alpha = 0.7)
    ax.set_title("Visualizing Your BMI", fontsize=24)
    ax.set_xlabel("Weight Categories", fontsize=14)
    ax.set_ylabel("BMI Value", fontsize=14)
    plt.ylim([0,50])
    plt.show()
