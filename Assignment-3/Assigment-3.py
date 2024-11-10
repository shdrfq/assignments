import math
#Assignment 3 dated 18/08/24 BATCH 65
pro_1 ="Calculate your age based on the current year and your birth year"
pro_2 ="Write a program that calculates the area of a rectangle using length and width variables."
pro_3 ="Write a program that calculates the area of a circle."
pro_4 ="Write a program that calculates the area of the cube."
pro_5 ="Create a program that converts a temperature from Fahrenheit to Celsius and vice versa using a variable."
pro_6 ="Convert a given number of seconds into minutes and seconds using variables."
pro_7 ="Write a program that calculates the percentage."
pro_8 ="Write a program that calculates the BMI using height (in meters) and weight (in kilogram1s) variables."
pro_9 ="Write a program that calculates the volume of a cylinder using the formula ."

programNo:int = int(input(" Please Enter Program NO [1-9] :  "))
#1- Calculate your age based on the current year and your birth year.
if programNo==1:
  print(f"Program No : {programNo} -- {pro_1}")
  Curent_year:int = 2024
  birthYear:str = input("Please Enter Your Birthday Year :")
  yourAge = Curent_year-int(birthYear)
  print("your age is  = "+str(yourAge))

    # Curent_year:int = 2024
    # Birth_year:str = input("Please Enter Your Birthday Year :")
    # try:
    #     Age = Curent_year-int(Birth_year)
    #     print ("your age is  = "+str(Age))
    # except ValueError:
    #     print("Invalid input! Please enter a valid integer.")
    #     Birth_year:str = input("Please Enter Your Birthday Year :")



 #2- Write a program that calculates the area of a rectangle using length and width variables.
elif programNo==2:
    print(f"Program No : {programNo} -- {pro_2}")
    width:str = input("Please Enter Width of Rectangle :")
    length:str =  input("Please Enter hight of Rectangle :")
    area =float(width)*float(length)
    print(f"area of a rectangle is  = {area}")   # print (" area of a rectangle is  = "+str(area))


    #3 - Write a program that calculates the area of a circle. A=πr**2 
elif(programNo==3):
    print(f"Program No : {programNo} -- {pro_3}")
    pi_value:float = 3.14
    radius_value:str = input("Please Enter Circcle Radius :")
    area_circle:float =pi_value*(float(radius_value)**2)
    print(f"area of a Circle is  = {area_circle}")  # print(" area of a Circle is  = "+str(area_circle))


    #4 - Write a program that calculates the area of the cube.             A=6a**2
elif(programNo==4):
    print(f"Program No : {programNo} -- {pro_4}")
    cube_length:str = input("Please Enter Length of Cube  :")
    area_cube:float =(6*float(cube_length)**2)
    print(f"area of a Cube is  = {area_cube}") # print(" area of a Cube is  = "+str(area_cube))
elif(programNo==5):
    print(f"Program No : {programNo} -- {pro_5}")
    # 5 - Create a program that converts a temperature from Fahrenheit to Celsius and vice versa using a variable.
    # Celsius= 9/5 × (Fahrenheit−32)
    # Fahrenheit=(Celsius × 5/9 )+32
    temperature = float(input("Enter the temperature value: "))
    scale = input("Enter the scale to convert from (F for Fahrenheit, C for Celsius): ")
    if scale.upper() == 'C':
     fahrenheit_to_celsius = (temperature-32)*5/9
     print(f"{temperature}°F is {fahrenheit_to_celsius:.2f}°C")
    elif scale.upper() == 'F':
     elsius_to_fahrenheit = (temperature*9/5)+32
     print(f"{temperature}°C is {elsius_to_fahrenheit:.2f}°F")
    else:
     print("Invalid scale entered. Please enter 'F' for Fahrenheit or 'C' for Celsius.")
 
    # 6 - Convert a given number of seconds into minutes and seconds using variables.
elif(programNo==6):
    print(f"Program No : {programNo} -- {pro_6}")
    totalSeconds:str = input("Please Enter Number  of Seconds  :")
    totalMinuts:int = int(totalSeconds)//60
    newSeconds:int =  int(totalSeconds)%60
    print(f"{totalSeconds} seconds is equal to {totalMinuts} minutes and {newSeconds} seconds.")

    # 7- Write a program that calculates the percentage.
elif(programNo==7):
    print(f"Program No : {programNo} -- {pro_7}")
    totalNumver:str = input("Please Enter Total Numver :")
    obtainNumber:str =  input("Please Enter Obtain Numvers :")
    percentage =(int(obtainNumber)/int(totalNumver))*100
    print(f"You have Obtaind  {percentage} % Numvbers")   # print (" area of a rectangle is  = "+str(area))


    # 8- Write a program that calculates the BMI using height (in meters) and weight (in kilograms) variables.
elif(programNo==8):
    print(f"Program No : {programNo} -- {pro_8}")
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    yourBmi = weight / (height ** 2)
    print(f"Your BMI is: {yourBmi:.2f}")
    # 9- Write a program that calculates the volume of a cylinder using the formula . 
elif(programNo==9):
    print(f"Program No : {programNo} -- {pro_9}")
    cylinderRadius = float(input("Enter the radius of the cylinder: "))
    cylinderHeight = float(input("Enter the height of the cylinder: "))
    cylinderVolume = math.pi*cylinderRadius**2*cylinderHeight
    print(f"The volume of the cylinder with radius {cylinderRadius} and height {cylinderHeight} is {cylinderVolume:.2f} cubic units.")
else:
  print("Please Enter Program Number Within Rang ie [1-9]")
