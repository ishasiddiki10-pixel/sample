class Node:
    def __init__(self, v, l = None, r = None):
        self.value, self.left, self.right = v, l, r 
reg = 0
def generate(root):
    global reg
    if not root.left and not root.right:
        r = reg
        reg += 1
        print(f"MOVE R{r} {root.value}")
        return r
    a, b = generate(root.left), generate(root.right)
    r =  reg
    reg += 1
    ops = {'+' : 'ADD', '-' : 'SUB', '*' : 'MUL', '=' : 'MOV'}
    if root.value == '=':
        print(f"MOV {root.left.value} R{b}")
        return b
    else:
        print(f"{ops[root.value]} R{r} R{a} R{b}")
        return r  
def postfix(expr):
    prec = {'=': 0, '*':2, '/':2, '+':1,'-':1}
    stack, output = [], []
    for c in expr:
        if c.isalnum():
            output.append(c)
        elif c == '(':
            stack.append(c)
        elif c == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] in prec and prec[stack[-1]] >= prec[c]:
                output.append(stack.pop())
            stack.append(c)
    while stack:
        output.append(stack.pop())
    return ''.join(output)
def ast(post):
    stack = []
    for c in post:
        if c in '+-*/=':
            b = stack.pop()
            a = stack.pop()
            stack.append(Node(c, a, b))
        else:
            stack.append(Node(c))
    return stack[0]
print("Enter input expr : ")
expr = input().replace(" ", "")
post = postfix(expr)
root = ast(post)
generate(root)
    
