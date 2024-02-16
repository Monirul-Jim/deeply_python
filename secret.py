# import random
# import string
#
# user_input = input("Enter a string: ")
#
# # Check if input length is at least 3 characters
# if len(user_input) < 3:
#     print("Input length should be at least 3 characters.")
# else:
#     # Move the first letter to the end
#     modified_string = user_input[1:] + user_input[0]
#
#     # Generate 3 random letters for the beginning and end
#     random_letters_start = ''.join(random.choices(string.ascii_lowercase, k=3))
#     random_letters_end = ''.join(random.choices(string.ascii_lowercase, k=3))
#
#     # Add random letters at the beginning and end
#     modified_string = random_letters_start + modified_string + random_letters_end
#
#     print("Modified string:", modified_string)
import random
import string
user_input=input("Enter your secret key : ")
if len(user_input)<3:
    print("Enter key should at least three charecter")
else:
    modified_number = user_input[1:]+user_input[0]
    generate_first_string = ''.join(random.choices(string.ascii_lowercase, k=3))
    generate_last_string = ''.join(random.choices(string.ascii_lowercase, k=3))

    last_output = generate_first_string + modified_number + generate_last_string
    print(last_output)