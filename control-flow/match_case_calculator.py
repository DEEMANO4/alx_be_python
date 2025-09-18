num1_prompt = input("Enter the first number:")
num2_prompt = input("Enter the second number:")
num1 = int(num1_prompt)
num2 = int(num2_prompt)
operator = input("Choose the operation (+,-,*,/):")

match operator:
    case "+":
        Addition = num1 + num2
        print("The result is", Addition)
    case "-":
        Subtraction = num1 - num2
        print("The result is", Subtraction)
    case "*":
        Multiplication = num1 * num2
        print("The result is", Multiplication)
    case "/":
        if num2 != 0:
            Division = num1/num2
            print("The result is", Division)
        else:
            print("Cannot divide by zero.")
 

    
         


        
