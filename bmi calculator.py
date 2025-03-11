weight = float(input("Enter Weight(in Kg)"))
height = float(input("Enter Height(in Meter)"))

BMI = weight/(height)**2
print("BMI: ", BMI)

if BMI <= 18.5:
    print("You are skinny!")
elif BMI <= 24.9:
    print("You are Healthy!")
elif BMI <= 29.9:
    print("You are OverWeight!")
elif BMI <= 34.9:
    print("You are fat")