#!/usr/bin/python3
# London Academy of IT
# Python Exercise 15
'''
Write a program to calculate yourBMI and give weight status.
Body Mass Index (BMI)
BMI = weight(kg)/height(m2)
'''
print("*" * 50)
print("BMI")
print("*" * 50)
name = input("Enter your name: ")
weight = float(input("Enter your weight(KG): "))
height = float(input("Enter your height(M): "))
BMI = round((weight/(height ** 2)), 2)
if BMI < 18.5:
    print("Mr. {} your BMI is {} and you're underweight".format(name, BMI))
elif BMI >= 18.5 and BMI <=24.9:
    print("Mr. {} your BMI is {} and you're Normal".format(name, BMI))
elif BMI >= 25 and BMI <=29.9:
    print("Mr. {} your BMI is {} and you're Overweight".format(name, BMI))
else:
    print("Mr. {} your BMI {} is and you're Obese".format(name, BMI))