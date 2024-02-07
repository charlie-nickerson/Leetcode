# Evaluate Reverse Polish Notation
# Difficulty: Medium
# Description: You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

#Evaluate the expression. Return an integer that represents the value of the expression.

# Note that:

#    The valid operators are '+', '-', '*', and '/'.
#    Each operand may be an integer or another expression.
#    The division between two integers always truncates toward zero.
#    There will not be any division by zero.
#    The input represents a valid arithmetic expression in a reverse polish notation.
#    The answer and all the intermediate calculations can be represented in a 32-bit integer.


def evalRPN(tokens):
    operations = {"+", "-", "*", "/"}
    temp = []
    for t in tokens:
        if t not in operations:
            temp.append(int(t))
        elif t == "+":
            e = temp.pop() + temp.pop()
            temp.append(e)
        elif t == "-":
            e = (-temp.pop()) + temp.pop()
            temp.append(e)
        elif t == "*":
            e = temp.pop() * temp.pop()
            temp.append(e)
        elif t == "/":
            divisor = temp.pop()
            dividend = temp.pop()
            e = int(float(dividend)/float(divisor))
            temp.append(e)
    return temp.pop() 
    

def main():
    tokens = ["2","1","+","3","*"]
    evaluation = evalRPN(tokens)
    print(evaluation)

if __name__ == "__main__":
    main()