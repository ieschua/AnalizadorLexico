#Principal.py
#Programado por Ieschua S.  - Compiladores / 4NV50

import re

class AnalizadorLexico:
    # Fila de Token
    lin_num = 1

    def tokenizar(self, codigo):
        reglas = [
            ('MAIN', r'main'),          # main
            ('INT', r'int'),            # int
            ('FLOAT', r'float'),        # float
            ('IF', r'if'),              # if
            ('ELSE', r'else'),          # else
            ('WHILE', r'while'),        # while
            ('READ', r'read'),          # read
            ('PRINT', r'print'),        # print
            ('LBRACKET', r'\('),        # (
            ('RBRACKET', r'\)'),        # )
            ('LBRACE', r'\{'),          # {
            ('RBRACE', r'\}'),          # }
            ('COMMA', r','),            # ,
            ('PCOMMA', r';'),           # ;
            ('EQ', r'=='),              # ==
            ('NE', r'!='),              # !=
            ('LE', r'<='),              # <=
            ('GE', r'>='),              # >=
            ('OR', r'\|\|'),            # ||
            ('AND', r'&&'),             # &&
            ('ATTR', r'\='),            # =
            ('LT', r'<'),               # <
            ('GT', r'>'),               # >
            ('PLUS', r'\+'),            # +
            ('MINUS', r'-'),            # -
            ('MULT', r'\*'),            # *
            ('DIV', r'\/'),             # /
            ('ID', r'[a-zA-Z]\w*'),     # IDENTIFICADORES
            ('FLOAT_CONST', r'\d(\d)*\.\d(\d)*'),   # FLOAT
            ('INTEGER_CONST', r'\d(\d)*'),          # INT
            ('NEWLINE', r'\n'),         # NUEVA LINEA
            ('SKIP', r'[ \t]+'),        # SPACIO Y TABS
            ('MISMATCH', r'.'),         # OTRO CARACTER
        ]

        tokens_unidos = '|'.join('(?P<%s>%s)' % x for x in reglas)
        lin_inicio = 0

        # Listas de salida del programa
        token = []
        lexema = []
        fila = []
        columna = []
        total = []

        # Analiza el código para encontrar los lexemas y sus respectivos Tokens
        for m in re.finditer(tokens_unidos, codigo):
            token_tipo = m.lastgroup
            token_lexema = m.group(token_tipo)

            if token_tipo == 'NEWLINE':
                lin_inicio = m.end()
                self.lin_num += 1
            elif token_tipo == 'SKIP':
                continue
            elif token_tipo == 'MISMATCH':
                raise RuntimeError('%r unexpected on line %d' % (token_lexema, self.lin_num))
            else:
                    col = m.start() - lin_inicio
                    columna.append(col)
                    token.append(token_tipo)
                    lexema.append(token_lexema)
                    fila.append(self.lin_num)
                    
                    # Imprimir información sobre un Token
                    total += ["Token = {0}, Lexema = '{1}', Fila = {2}, Columna = {3}".format(token_tipo, token_lexema, self.lin_num, col)]
                    

        totalT = '\n'.join(map(str, total))
        return token, lexema, fila, columna, totalT
