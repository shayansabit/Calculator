# Prompt the user about what does he want to do
user_input = input("What do you want to do? \n 1. Addition \n 2. Subtration \n 3. Multiplication \n 4. Division \n Type 1 for Addition, 2 for Subtraction, 3 for Multiplication and 4 for Division. \n Type your answer here: ")




# Add
if user_input == "1" :
    
   first_num = int(input("Type your first number: "))
   second_num = int(input("Type your second number: "))
   print ("Your Answer is: " + str(first_num + second_num))
    
# Subtract
if user_input == "2" :
    
   first_num = int(input("Type your largest number: "))
   second_num = int(input("Type your smallest number: "))
   print ("Your Answer is: " + str(first_num - second_num))
# Multiply
if user_input == "3" :
    
   first_num = int(input("Type your first number: "))
   second_num = int(input("Type your second number: "))
   print ("Your Answer is: " + str(first_num * second_num))
# Divide
if user_input == "4" :
    
   first_num = int(input("Type your first number: "))
   second_num = int(input("Type your second number: "))
   print ("Your Answer is: " + str(first_num / second_num))