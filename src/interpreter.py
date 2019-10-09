import path
import os

stack = []

def C0_run(orders): #key: 下一个执行的指令序号
    key = 0
    while key < len(orders):
        key = C0_execute(orders[key],key)

def C0_execute(order,key):
    if order[0]=="LIT":
        stack.append(order[2])
        key+=1
    elif order[0]=="LOD":
        pass
    elif order[0]=="STO":
        pass
    elif order[0]=="CAL":
        pass
    elif order[0]=="INT":
        pass
    elif order[0]=="JMP":
        key = order[2]
    elif order[0]=="JPC":
        if stack[-1]==0:
            key = order[2]
        else:
            key += 1
    elif order[0]=="ADD":
        num = stack[-2] + stack[-1]
        stack.pop()
        stack.pop()
        stack.append(num)
        key+=1
    elif order[0]=="SUB":
        num = stack[-2] - stack[-1]
        stack.pop()
        stack.pop()
        stack.append(num)
        key+=1
    elif order[0]=="MUL":
        num = stack[-2] * stack[-1]
        stack.pop()
        stack.pop()
        stack.append(num)
        key+=1
    elif order[0]=="DIV":
        num = stack[-2] / stack[-1]
        stack.pop()
        stack.pop()
        stack.append(num)
        key+=1
    elif order[0]=="RED":
        num = input()
        stack.append(num)
        key+=1
    elif order[0]=="WRT":
        print(stack[-1])
        stack.pop()
        key+=1
    elif order[0]=="RET":
        pass

    return key


if __name__ == "__main__":
    sentence = []
    orders = []

    print("请输入c0temp文件地址")
    filepath = input()
    with open(filepath,"r") as f:
        for line in f:
            sentence.append(line)

    for str in sentence:
        orders.append([str[0:3],int(str[4]),int(str[6:])])

    C0_run(orders)
