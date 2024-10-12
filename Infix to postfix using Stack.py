# Function to return precedence of operators
def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '^':
        return 3
    return 0

# Function to convert infix expression to postfix expression
def infix_to_postfix(expression):
    stack = []  # Stack to hold operators
    postfix = []  # List for output
    for char in expression:
        if char.isalnum():  # If the character is an operand, add it to output
            postfix.append(char)
        elif char == '(':  # If it's a '(', push to stack
            stack.append(char)
        elif char == ')':  # If it's a ')', pop until '(' is found
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()  # Pop the '('
        else:  # Operator encountered
            # Handle the right-associativity for '^'
            while (stack and precedence(char) < precedence(stack[-1])) or \
                  (char != '^' and stack and precedence(char) == precedence(stack[-1])):
                postfix.append(stack.pop())
            stack.append(char)  # Push the current operator onto the stack

    # Pop all the operators left in the stack
    while stack:
        postfix.append(stack.pop())

    return ''.join(postfix)

# Test the function
infix_expression = input("Enter Expression : ")
print("Infix Expression: ", infix_expression)
print("Postfix Expression: ", infix_to_postfix(infix_expression))
