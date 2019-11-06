import ply.lex as lex

def buildLex():
    tokens = (
        'NUMBER',
        'PLUS',
        'MINUS',
        'TIMES',
        'DIVIDE',
        'LPAREN',
        'RPAREN',
    )

    t_PLUS = r"\+"
    t_MINUS = r"-"
    t_TIMES = r"\*"
    t_DIVIDE = r"/"
    t_LPAREN = r"\("
    t_RPAREN = r"\)"

    def t_NUMBER(t):
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
    str = "1+2 3*4"
    lexer = buildLex()
    lexer.input(str)
    for tok in lexer:
        print(tok)