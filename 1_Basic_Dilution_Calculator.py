# 1_Basic_Dilution_Calculator.py

# Copy and paste this code to your text editor / IDE and start making dilutions in your lab.
# This is written in a 'while' loop, just in case you are making more than one dilution.
# Enter 'q' to exit loop!

# M1 = The desired concentration you are hoping to end up with. (I want my final solution to be 1PPM)
# V1 = How much volume are you trying to end up with. (Eg. I want to make 5000mL of solution)
# M2 = What concentration are you starting off with in your lab. (Eg. My initial concentration is 5PPM)

# Eg. INPUT
  # What concentration is the original solution: 5
  # What is your desired concentration: 1
  # How much volume are you planning to make (mL): 5000
  
# Eg. OUTPUT
  # Add 1000.0 mL of your original solution to 4000.0 mL of water.

while True:
    print("\nEnter 'q' at any time to exit!")
    M2 = float(input("What concentration is the original solution: "))
    if M2 == 'q':
        break
    M1 = float(input("What is your desired concentration: "))
    if M1 == 'q':
        break
    V1 = float(input("How much volume are you planning to make (mL): "))
    if V1 == 'q':
        break
    else:
        V2 = (M1*V1) / M2
        H2O = V1 - V2
    print(f"\nAdd {V2} mL of your original solution to {H2O} mL of water.")
