import re

def tokenize(expression):
    # 匹配数字（包括负数和小数）、运算符、括号
    tokens = re.findall(r'(-?\d+\.?\d*)|(-?\.\d+)|([+\-*/()])', expression)
    # 将匹配结果展平并过滤空字符串
    tokens = [t for group in tokens for t in group if t]
    return tokens

def infix_to_postfix(tokens):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    stack = []
    for token in tokens:
        if token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if not stack:
                raise ValueError("括号不匹配")
            stack.pop()  # 弹出左括号
        elif token in precedence:
            while stack and stack[-1] != '(' and precedence[token] <= precedence.get(stack[-1], 0):
                output.append(stack.pop())
            stack.append(token)
        else:  # 数字
            output.append(token)
    # 将剩余运算符弹出
    while stack:
        if stack[-1] == '(':
            raise ValueError("括号不匹配")
        output.append(stack.pop())
    return output

def evaluate_postfix(postfix):
    stack = []
    for token in postfix:
        if token in {'+', '-', '*', '/'}:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                if b == 0:
                    raise ZeroDivisionError("除数不能为零")
                stack.append(a / b)
        else:
            try:
                num = float(token)
            except ValueError:
                raise ValueError(f"无效数字: {token}")
            stack.append(num)
    if len(stack) != 1:
        raise ValueError("无效表达式")
    return stack[0]

def calculate(expression):
    expression = expression.replace(' ', '')  # 去除空格
    tokens = tokenize(expression)
    if not tokens:
        raise ValueError("空表达式")
    postfix = infix_to_postfix(tokens)
    return evaluate_postfix(postfix)

def main():
    print("简易计算器（输入'exit'退出）")
    while True:
        try:
            expr = input("请输入表达式: ").strip()
            if expr.lower() == 'exit':
                break
            result = calculate(expr)
            print(f"结果: {result}")
        except Exception as e:
            print(f"错误: {e}")

if __name__ == "__main__":
    main()