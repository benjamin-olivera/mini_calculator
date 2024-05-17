

def add(n1, n2):
    return n1 + n2 
def substract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2

operations = {
    "+": add, 
    "-": substract,
    "*": multiply,
    "/": divide
}

num1 = int(input("Enter the first number: "))

for symbol in operations:
    print(symbol)
operation_symbol = input("Pick an operation from the line above: ")
num2 = int(input("Enter the second number: "))
calculation_function = operations[operation_symbol]
first_answer = calculation_function(num1,num2)
#if operation_symbol in operations:
    #answer = operations[operation_symbol](num1,num2)
print(f"{num1} {operation_symbol} {num2} = {answer}")
operation_symbol = input("Pick another operation: ")
num3 = int(input("Enter the next number: "))
calculation_function = operations[operation_symbol]
second_answer = calculation_function(first_answer,num3)
print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")