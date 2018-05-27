import ply.lex as lex


resultado_lexema = []

reservada = (
   
    'INCLUIR',
    'MOSTRAR',
    'LEER',
    'NUMERICO',
    'DEVUELVE',
    'VACIO',
    'ENTERO',
    'BOOL',
)
tokens = reservada + (
    'IDENTIFICADOR',
    'ASIGNADOR',
    'NOVARIABLE',

    'SUMADOR',
    'RESTANDO',
    'MULTIPLICADOR',
    'DIVISOR',
    'POTENCIADOR',
    'MODULO',

    'SI',
    'YSINO',
    
    'MIENTRAS',
    'PARA',
    'Y',
    'O',
    'NEGACION',
    'ELMENOR',
    'MENOROIGUAL',
    'ELMAYOR',
    'MAYOROIGUAL',
    'IGUAL',
    'DESIGUAL',
    
    'PARENIZQ',
    'PARENDER',
    'LLAVEIZQ',
    'LLAVEDER',
  
)



t_SUMADOR = r'\&'
t_RESTANDO = r'-'
t_MULTIPLICADOR = r'\*'
t_DIVISOR = r'/'
t_MODULO = r'\%'
t_POTENCIADOR = r'(\*{2} | \^)'
t_ASIGNADOR = r'='

t_Y= r'\&\&'
t_O = r'\|{2}'
t_NEGACION= r'\!'
t_ELMENOR = r'<'
t_ELMAYOR = r'>'
t_FINDESENTENCIA = ';'
t_PARENIZQ = r'\('
t_PARENDER = r'\)'
t_LLAVEIZQ = r'{'
t_LLAVEDER = r'}'
t_ignore =' \t'



def t_INCLUIR(t):
    r'incl'
    return t

def t_NUMERICO(t):
    r'num'
    return t

def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_MOSTRAR(t):
    r'msg'
    return t

def t_LEER(t):
    r'rec'
    return t

def t_BOOL(t):
    r'bool'
    return t

def t_YSINO(t):
    r'sino'
    return t

def t_SI(t):
    r'si'
    return t

def t_DEVUELVE(t):
   r'retorna'
   return t

def t_VACIO(t):
   r'vac'
   return t

def t_MIENTRAS(t):
    r'mtras'
    return t

def t_PARA(t):
    r'para'
    return t

def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][a-zA-Z0-9]*'
    return t

def t_MENOROIGUAL(t):
    r'<='
    return t

def t_MAYOROIGUAL(t):
    r'>='
    return t

def t_IGUAL(t):
    r'=='
    return t

def t_DESIGUAL(t):
    r'!='
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_comments(t):
    r'\$.*'
    pass

def t_error(t):
    global resultado_lexema
    estado = "Token no valido en la Linea: {:4} ".format(str(t.lineno))
    resultado_lexema.append(estado)
    t.lexer.skip(1)


class AnalizadorLexico:
    def __init__(self,tokens):
        self.tokens=tokens
    
    def getTokens(self):
        return self.tokens
    
    def prueba(self,data):
        global resultado_lexema
        analizador = lex.lex()
        analizador.input(data)
        resultado_lexema.clear()
        while True:
            tok = analizador.token()
            if not tok:
                break
            estado = "Linea {:4} Tipo {:16} ".format(str(tok.lineno),str(tok.type) )
            resultado_lexema.append(estado)
        return resultado_lexema




#pueba pa ve si sirve :v
analizador = lex.lex()
a=AnalizadorLexico(tokens)
arc=open('holamundo.arc','r')
data=arc.read() 
print(a.prueba(data))


        

        

