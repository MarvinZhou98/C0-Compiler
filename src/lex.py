import ply.lex as lex

#返回lex和tokens
def buildLex():
    reserved = {
        'if' : 'IF',
        'else' : 'ELSE',
        'void' : 'VOID',
        'int' : 'INT',
        'while' : 'WHILE',
        'return' : 'RETURN',
        'scanf' : 'SCANF',
        'printf' : 'PRINTF'
    }

    tokens = [
        'NUM',
        'ID'
    ] + list(reserved.values())

    literals = "+-*/=(){},;"

    def t_ID(t):
        r"[a-zA-Z_]\w*"
        t.type = reserved.get(t.value,"ID")
        return t

    def t_NUM(t):
        r"\d+"
        t.value = int(t.value)
        return t

    def t_newline(t):
        r"\n+"
        t.lexer.lineno += len(t.value)

    t_ignore = ' \t'

    def t_error(t):
        print("无法识别的字符",t)
        t.lexer.skip(1)

    return lex.lex()


if __name__ == "__main__":
    str = "int a=1;\nprintf(a)"
    lexer = buildLex()[0]
    lexer.input(str)
    for tok in lexer:
        print(tok)