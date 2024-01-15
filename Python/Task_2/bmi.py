print("This is a command line BMI calculator\n")
name= input("Enter the name:" )
weight= float(input("Enter the weight: "))
height= float(input("Enter the height: "))

bmi= weight/ (height**2)

if bmi < 18.5:
    print(f"{name} is underweight by {bmi} BMI")
elif bmi > 18 and bmi < 24.9:
    print(f"Congratulations! {name} is healthy.You have normal weight by {bmi} BMI.")
elif bmi >25 and bmi < 29.9:
    print(f"{name} is overweight by {bmi} BMI")
else:
    print(f"{name} is obese by {bmi} BMI")

    