import src.lex as lex
import src.compiler as compiler

token = []  #标识符序列
t = 0 #标记当前位置
print("请输入c0文件地址")
filepath = input()
with open(filepath,"r") as f:
    s = ""
    for line in f:
        s = s + line
    lexer = lex.buildLex()
    lexer.input(s)
    for tok in lexer:
        token.append(tok)

print(token)
order = compiler.test(token)
with open("temp.txt","w") as f:
    for o in order:
        s = o[0] + " " + str(o[1]) + " " + str(o[2]) + "\n"
        f.write(s)