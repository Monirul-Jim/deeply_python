# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
#
# try:
#     num = int(input("Enter a number: "))
#     if num < 0:
#         print("Factorial is not defined for negative numbers.")
#     else:
#         print("Factorial of", num, "is", factorial(num))
# except ValueError:
#     print("Please enter a valid integer.")
def factorial(n):
   if n == 0:
    return 1
   else:
       return n*factorial(n-1)
try:
    num = int(input("Enter a number : "))
    if num < 0 :
        print("Factorial is not defined for negative number")
    else:
        print(f"the number of f {num} is  f{factorial(num)}")
except ValueError:
    print("Please Enter a valid number")