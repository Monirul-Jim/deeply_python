# def print_pattern(rows):
#     for i in range(1, rows + 1):
#         print(str(i) * i)
#
# try:
#     rows = int(input("Enter the number of rows: "))
#     if rows <= 0:
#         print("Please enter a positive integer.")
#     else:
#         print_pattern(rows)
# except ValueError:
#     print("Please enter a valid integer for the number of rows.")
def pattern_rows(rows):
    for i in range(1,rows+1):
        print(str(i)*i)
try:
    rows = int(input("Enter a number : "))
    if rows <= 0 :
        print("please enter a positive number")
    else:
       pattern_rows(rows)
except ValueError:
    print("Please enter a valid number")