import sys

def test(token):    #tonken: 标识符序列

    tab_var_glo = []    #全局变量表
    tab_var_loc = []    #全局变量表
    tab_fun = []    #函数表
    isGlo = True    #判断是否在全局作用域
    #指令
    var_glo = []    #全局变量定义指令
    fun_main = []   #主函数指令

    def error(type):    #错误处理
        sys.exit(0)

    def program_deal(): #入口
        t = 0
        #变量定义部分
        if token[t].type == "INT" and token[t+1].type == "ID" and token[t+2].type != "(":
            t,var_glo = var_deal(t)
        isGlo = False
        while True: #自定义函数定义部分
            if token[t].type == "INT" and token[t+1].type == "ID" and token[t+2].type == "(":
                t = fun_int_deal(t)
            elif token[t].type == "VOID" and token[t+1].type == "ID":
                t = fun_void_deal(t)
            else:
                break
        if token[t].type == "VOID" and token[t+1].type == "MAIN":
            t = fun_main_deal(t)
        else:
            error(0)

    def var_add(id):    #创建变量
        if isGlo is True:   #全局变量
            if id not in tab_var_glo:
                tab_var_glo.append(id)
        else:   #局部变量
            if id not in tab_var_loc:
                tab_var_loc.append(id)

    def var_find(id):   #查找变量 返回变量地址 0or1,a
        #先查找局部变量,再查找全局变量
        if id in tab_var_loc:
            return 0,tab_var_loc.index(id)
        elif id in tab_var_glo:
            return 1,tab_var_glo.index(id)
        else:
            error(0)

    def var_deal(start):    #变量定义 返回指针位置，指令
        t = start+1
        var_add(token[t].value)
        t = t+1
        flag = False
        while True:
            if token[t].type == ";":
                if flag == False:
                    break
                else:
                    error(0)
            elif token[t].type == ",":
                if flag == False:
                    flag = True
                else:
                    error(0)
            elif token[t].type == "id":
                if flag == True:
                    var_add(token[t].value)
                    flag = False
                else:
                    error(0)
            t = t+1
        order = ["INT",0,len(tab_var_glo) if isGlo is True else len(tab_var_loc)]
        return t+1,order
        
        

    def fun_int_deal(start):    #int函数 返回指针位置
        pass

    def fun_void_deal(start):   #void函数 返回指针位置
        pass

    def fun_main_deal(start):   #主函数 返回指针位置
        t = start+1
        if token[t+2].type=="(" and token[t+3].type==")" and token[t+4].type=="{":
            t = t+4
            t,fun_main = block_deal(t)
        else:
            error(0)
        return t+1

    def block_deal(start):  #分程序 返回指针位置，指令
        t = start+1
        tab_var_loc = []    #初始化局部变量表
        orders = []
        if token[t].type == "INT" and token[t+1].type == "ID" and token[t+2].type != "(":
            t,order = var_deal(t)
            orders.append(order)
        while True: #语句处理
            if token[t].type == "}":
                break
            else:
                t,order = sentence_deal(t)
                orders.append(order)
        return t+1,orders


    def sentence_deal(start):   #语句处理入口 返回指针位置，指令
        t = start
        if token[t].type == "IF":
            t,order = sen_if_deal(t)
            return t+1,order
        elif token[t].type == "WHILE":
            t,order = sen_while_deal(t)
            return t+1,order
        elif token[t].type == "RETURN":
            t,order = sen_return_deal(t)
            return t+1,order
        elif token[t].type == "SCANF":
            t,order = sen_scanf_deal(t)
            return t+1,order
        elif token[t].type == "PRINTF":
            t,order = sen_printf_deal(t)
            return t+1,order
        elif token[t].type == "ID":
            if token[t+1].type == "=":
                t,order = sen_eval_deal(t)
                return t+1,order
            elif token[t+1].type == "(" and token[t+2].type == ")":
                t,order = sen_fun_deal(t)
                return t+1,order
            else:
                error(0)
        else:
            error(0)

    #语句处理
    def sen_if_deal(start):
        pass

    def sen_while_deal(start):
        pass

    def sen_eval_deal(start):
        pass

    def sen_return_deal(start):
        pass

    def sen_scanf_deal(start):
        t = start
        if token[t].type=="SCANF" and token[t+1].type=="(" and token[t+2].type=="ID" and token[t+3].type==")" and token[t+4]==";":
            id = token[t+2].value
            a,b = var_find(id)
            order = []
            order.append(["RED",0,0])
            order.append(["STO",a,b])
            return t+5,order
        else:
            error(0)


    def sen_printf_deal(start):
        pass

    def sen_fun_deal(strat):
        pass

    #表达式处理 TODO