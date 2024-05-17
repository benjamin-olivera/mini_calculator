n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

def add(n1, n2):
    return n1 + n2 
def substract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2

operation = {
    "+": add, 
    "-": substract,
    "*": multiply,
    "/": divide
}
