import ply.yacc as yacc
from Lexer import tokens
from Lexer import analizador

# resultado del analisis
resultado_gramatica = []

precedence = (
    ('right','ASIGNADOR'),
    ('left', 'SUMADOR', 'RESTANDO'),
    ('left', 'MULTIPLICADOR', 'DIVISOR'),
)
nombres = {}

def p_declaracion_asignar(t):
    'declaracion : IDENTIFICADOR ASIGNADOR expresion'
    nombres[t[1]] = t[3]

def p_declaracion_expr(t):
    'declaracion : expresion'
    # print("Resultado: " + str(t[1]))
    t[0] = t[1]

def p_expresion_operaciones(t):
    '''
    expresion  :   expresion SUMADOR expresion
                |   expresion RESTANDO expresion
                |   expresion MULTIPLICADOR expresion
                |   expresion DIVISOR expresion
                |   expresion POTENCIADOR expresion
                |   expresion MODULO expresion

    '''
    if t[2] == '&':
        t[0] = t[1] + t[3]
    elif t[2] == '-':
        t[0] = t[1] - t[3]
    elif t[2] == '*':
        t[0] = t[1] * t[3]
    elif t[2] == '/':
        t[0] = t[1] / t[3]
    elif t[2] == '%':
        t[0] = t[1] % t[3]
    elif t[2] == '**':
        i = t[3]
        t[0] = t[1]
        while i > 1:
            t[0] *= t[1]
            i -= 1


def p_expresion_grupo(t):
    '''
    expresion  : PARENIZQ expresion PARENDER
                | LLAVEIZQ expresion LLAVEDER
    '''
    t[0] = t[2]
# sintactico de expresiones logicas
def p_expresion_logicas(t):
    '''
    expresion   :  expresion ELMENOR expresion 
                |  expresion ELMAYOR expresion 
                |  expresion MENOROIGUAL expresion 
                |   expresion MAYOROIGUAL expresion 
                |   expresion IGUAL expresion 
                |   expresion DESIGUAL expresion
                |  PARENIZQ expresion PARENDER ELMENOR PARENIZQ expresion PARENDER
                |  PARENIZQ expresion PARENDER ELMAYOR PARENIZQ expresion PARENDER
                |  PARENIZQ expresion PARENDER MENOROIGUAL PARENIZQ expresion PARENDER 
                |  PARENIZQ  expresion PARENDER MAYOROIGUAL PARENIZQ expresion PARENDER
                |  PARENIZQ  expresion PARENDER IGUAL PARENIZQ expresion PARENDER
                |  PARENIZQ  expresion PARENDER DESIGUAL PARENIZQ expresion PARENDER
    '''
    if t[2] == "<": t[0] = t[1] < t[3]
    elif t[2] == ">": t[0] = t[1] > t[3]
    elif t[2] == "<=": t[0] = t[1] <= t[3]
    elif t[2] == ">=": t[0] = t[1] >= t[3]
    elif t[2] == "==": t[0] = t[1] is t[3]
    elif t[2] == "!=": t[0] = t[1] != t[3]
    elif t[3] == "<":
        t[0] = t[2] < t[4]
    elif t[2] == ">":
        t[0] = t[2] > t[4]
    elif t[3] == "<=":
        t[0] = t[2] <= t[4]
    elif t[3] == ">=":
        t[0] = t[2] >= t[4]
    elif t[3] == "==":
        t[0] = t[2] is t[4]
    elif t[3] == "!=":
        t[0] = t[2] != t[4]


# gramatica de expresiones booleanadas
def p_expresion_booleana(t):
    '''
    expresion   :   expresion Y expresion 
                |   expresion O expresion 
                |   expresion NEGACION expresion 
                |  PARENIZQ expresion Y expresion PARENDER
                |  PARENIZQ expresion O expresion PARENDER
                |  PARENIZQ expresion NEGACION expresion PARENDER
    '''
    if t[2] == "&&":
        t[0] = t[1] and t[3]
    elif t[2] == "||":
        t[0] = t[1] or t[3]
    elif t[2] == "!":
        t[0] =  t[1] is not t[3]
    elif t[3] == "&&":
        t[0] = t[2] and t[4]
    elif t[3] == "||":
        t[0] = t[2] or t[4]
    elif t[3] == "!":
        t[0] =  t[2] is not t[4]



def p_expresion_numero(t):
    'expresion : ENTERO'
    t[0] = t[1]

def p_expresion_nombre(t):
    'expresion : IDENTIFICADOR'
    try:
        t[0] = nombres[t[1]]
    except LookupError:
        print("Nombre desconocido ", t[1])
        t[0] = 0

def p_error(t):
    global resultado_gramatica
    if t:
        resultado = "Error sintactico "
    else:
        resultado = "Error sintactico {}".format(t)
        print(resultado)

parser = yacc.yacc()

def prueba_sintactica(data):
    global resultado_gramatica
    resultado_gramatica.clear()

    for item in data.splitlines():
        if item:
            gram = parser.parse(item)
            if gram:
                resultado_gramatica.append(str(gram))
        else: print("data vacia")

    print("resultado: ", resultado_gramatica)
    return resultado_gramatica



arc=open('holamundo.arc','r')
data=arc.read() 
gram = parser.parse(data)
prueba_sintactica(data)
