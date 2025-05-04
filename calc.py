# prompt user for input
num_value1 = int(input("Input your first value: "))
num_value2 = int(input("Input your second value: "))


# add
op = input("Input your operator: ")
if (op == "+"):
    {
      
      print("Your answer is: " + str(num_value1 + num_value2))
    }
# subtract
elif(op == "-"):
      {
           print("Your answer is: " + str(num_value1 - num_value2))
      }
# multiply
elif(op == "*"):
      {
           print("Your answer is: " + str(num_value1 * num_value2))
      }
# divide
elif(op == "/"):
      {
           print("Your answer is: " + str(int(num_value1 / num_value2)))
      }