# import math
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


#1- Calculate your age based on the current year and your birth year.
print(f"Program No : 1 -- {pro_1}")

def yourAge(x:int):
 Curent_year:int = 2024    
 yourAge = Curent_year-int(x)
 print("your age is  = "+str(yourAge))

birthYear = int(input("Please Enter Your Birthday Year :"))
yourAge(birthYear)

  

 #2- Write a program that calculates the area of a rectangle using length and width variables.
print(f"Program No :2 -- {pro_2}")

def rec_area(x,y):
 rec_area =float(x)*float(y)
 return rec_area
  
     
width = float(input("Please Enter Width of Rectangle :"))
length = float(input("Please Enter hight of Rectangle :"))
area= rec_area(width,length)
print(f"area of a rectangle is  = {area}")


    #3 - Write a program that calculates the area of a circle. A=πr**2 
print(f"Program No : 3 -- {pro_3}")
   
def area_circle(x):
      area_circle:float =3.14*(float(x)**2)
      print(f"area of a Circle is  = {area_circle}")  # print(" area of a Circle is  = "+str(area_circle))
    #   return rec_area

radius_value:str = input("Please Enter Circcle Radius :")
area_circle(radius_value)


    #4 - Write a program that calculates the area of the cube.             A=6a**2

print(f"Program No : 4 -- {pro_4}")

def area_cube(x):
 area_cube:float =(6*float(x)**2)     
 return(area_cube) 

cube_length:str = input("Please Enter Length of Cube  :")
area_cube = area_cube(cube_length)
print(f"area of a Cube is  = {area_cube}") 


    # 5 - Create a program that converts a temperature from Fahrenheit to Celsius and vice versa using a variable.
    # Celsius= 9/5 × (Fahrenheit−32)
    # Fahrenheit=(Celsius × 5/9 )+32
print(f"Program No : 5 -- {pro_5}")
def conv_temp(temp,scale):   
  if scale.upper() == 'C':
   fahrenheit_to_celsius = (temp-32)*5/9
   print(f"{temp}°F is Equal to  {fahrenheit_to_celsius:.2f}°C")
  elif scale.upper() == 'F':
   elsius_to_fahrenheit = (temp*9/5)+32
   print(f"{temp}°C is Equal to {elsius_to_fahrenheit:.2f}°F")
  else:
   print("Invalid scale entered. Please enter 'F' for Fahrenheit or 'C' for Celsius.")

temperature:float = float(input("Enter the temperature value: "))
scale:str = input("Enter the scale to convert from (F for Fahrenheit, C for Celsius): ")
conv_temp(temperature,scale)
 
    # 6 - Convert a given number of seconds into minutes and seconds using variables.

def convert_seconds(x:int):
  totalMinuts:int = int(x)//60
  newSeconds:int =  int(x)%60
  print(f"{x} seconds is equal to {totalMinuts} minutes and {newSeconds} seconds.")

totalSeconds:int = input("Please Enter Number  of Seconds  :")
convert_seconds(totalSeconds)

    # 7- Write a program that calculates the percentage.

print(f"Program No : 7 -- {pro_7}")

def calculate_percentage(x:int,y:int):
  percentage =(int(y)/int(x))*100
  return(percentage)

totalNumver = int(input("Please Enter Total Numver :"))
obtainNumber =  int(input("Please Enter Obtain Numvers :"))
your_percentage = calculate_percentage(totalNumver,obtainNumber)
print(f"You have Obtaind  {your_percentage} % Numvbers")  

    # 8- Write a program that calculates the BMI using height (in meters) and weight (in kilograms) variables.

print(f"Program No : 8 -- {pro_8}")

def calculate_Bmi(w:float,h:float):
  return(w/(h**2))

weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
yourbmi = calculate_Bmi(weight,height)
print(f"Your BMI is: {yourbmi:.2f}")
    # 9- Write a program that calculates the volume of a cylinder using the formula . 

print(f"Program No : 9 -- {pro_9}")

def cal_cylinder_vol(r:float,h:float):
  return(3.14159*r**2*h)
  
cylinderRadius = float(input("Enter the radius of the cylinder: "))
cylinderHeight = float(input("Enter the height of the cylinder: "))
cylinderVolume =cal_cylinder_vol(cylinderRadius,cylinderHeight)
print(f"The volume of the cylinder with radius {cylinderRadius} and height {cylinderHeight} is {cylinderVolume:.2f} cubic units.")
