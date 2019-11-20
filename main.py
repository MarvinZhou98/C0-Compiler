import src.lex as lex

token = []  #标识符序列
t = 0 #标记当前位置
print("请输入c0文件地址")
filepath = input()
with open(filepath,"r") as f:
    str = ""
    for line in f:
        str = str + line
    lexer = lex.buildLex()
    lexer.input(str)
    for tok in lexer:
        token.append(tok)
print(token)