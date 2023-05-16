#!/usr/bin/env python3

def admin_login(username, password):
    if (username == 'admin' or username == 'admin'.upper()) and password == '12345':
        return "Access granted"
    else:
        return "Access denied"

    # if username == "ADMIN" and password == "12345":
    #     return "Access granted"
    # else:
    #     return "Access denied"
    

def hows_the_weather(temperature):
    if (temperature < 40):
        return "It's brisk out there!"
    if (temperature < 65):
        return "It's a little chilly out there!"
    if (temperature > 85):
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"
    pass

def fizzbuzz(num):
  if num % 3 == 0 and num % 5 == 0:
    return "FizzBuzz"
  elif num % 3 == 0:
    return "Fizz"
  elif num % 5 == 0:
    return "Buzz"
  else:
    return num 
    

# def add(num1, num2):
#     return num1 + num2

# def subtract(num1, num2):
#     return num1 - num2

# def multiply(num1, num2):
#     return num1 * num2

# def divide(num1, num2):
#     if num2 != 0:
#         return num1 / num2
#     else:
#         print("Invalid operation!")
#         return None

# operations = {
#     "+": add,
#     "-": subtract,
#     "*": multiply,
#     "/": divide
# }

# def calculator(operation, num1, num2):
#     func = operations.get(operation)
#     if func:
#         return func(num1, num2)
#     else:
#         print("Invalid operation!")
#         return None
    


def calculator(operation, num1, num2):
   if (operation == "+"):
      return num1 + num2
   elif (operation == "-"):
      return num1 - num2
   elif (operation == "*"):
      return num1 * num2
   elif (operation == "/"):
      return num1 / num2
   else:
      print("Invalid operation!")
      return None



    # my python version does not support this method i wonder why 
    # def calculator(operation, num1, num2):
    # match operation:
    #     case "+":
    #         return num1 + num2
    #     case "-":
    #         return num1 - num2
    #     case "*":
    #         return num1 * num2
    #     case "/":
    #         if num2 != 0:
    #             return num1 / num2
    #         else:
    #             print("Invalid operation!")
    #             return None
        
