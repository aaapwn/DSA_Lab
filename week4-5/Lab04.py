from Lab03 import ArrayStacks

def is_parentheses_matching(expression):
    check = ArrayStacks()
    for i in expression:
        if i == '(':
            check.push(i)
        elif i == ')':
            if not check.is_empty():
                check.pop()
            else:
                print("Parentheses in %s are not matching" % expression)
                return False
    if check.is_empty():
        return True
    else:
        print("Parentheses in %s are not matching" % expression)
        return False

# result = is_parentheses_matching("((A+B)*C)")
# result = is_parentheses_matching("(((A+B)*C))))))))))")
# print(result)

def copyStacks(stack1, stack2):
    while not stack2.is_empty():
        stack2.pop()
    copy = ArrayStacks()
    while not stack1.is_empty():
        copy.push(stack1.pop())
    while not copy.is_empty():
        data = copy.pop()
        stack1.push(data)
        stack2.push(data)

# s1 = ArrayStacks()
# s1.push(10)
# s1.push(20)
# s1.push(30)
# s2 = ArrayStacks()
# s2.push(15)
# s1.printStack()
# s2.printStack()
# copyStacks(s1, s2)
# s1.printStack()
# s2.printStack()

def infixToPostfix(expression):
    operatorList = ArrayStacks()
    postfix = ""
    def compareOperator(operator):
        compare1 = compare2 = 0
        if operator in ["*", "/"]:
            compare1 = 2
        elif operator in ["+", "-"]:
            compare1 = 1
        if operatorList.stackTop() in ["*", "/"]:
            compare2 = 2
        elif operatorList.stackTop() in ["+", "-"]:
            compare2 = 1
        if compare1 > compare2:
            return True
        else:
            return False
    for i in expression:
        if i.isalpha():
            postfix += i
        elif i == "(":
            operatorList.push(i)
        elif i == ")":
            while operatorList.stackTop() != "(":
                postfix += operatorList.pop()
            operatorList.pop()
        else:
            if operatorList.is_empty():
                operatorList.push(i)
                continue
            while not operatorList.is_empty() and not compareOperator(i):
                postfix += operatorList.pop()
            operatorList.push(i)
    while not operatorList.is_empty():
        postfix += operatorList.pop()
    return postfix

exp = "A+B*C/D-F"
postfix = infixToPostfix(exp)
print(postfix)

