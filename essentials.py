##########################################
##                 Constants
##########################################
INT = 'INT'
FLOAT = 'FLOAT'
PLUS = 'PLUS'
MINUS = 'MINUS'
MUL = 'MUL'
DIV = 'DIV'
LPAREN = 'LPAREN'
RPAREN = 'RPAREN'




operators = { '=': 'Assignment Operator','+': 'Additon Operator', '-' : 'Substraction Operator', '/' : 'Division Operator', '*': 'Multiplication Operator', '++' : 'increment Operator', '--' : 'Decrement Operator'}
optr_keys = operators.keys()

comments = {r'//' : 'Single Line Comment',r'/*' : 'Multiline Comment Start', r'*/' : 'Multiline Comment End', '/**/' : 'Empty Multiline comment'}
comment_keys = comments.keys()

header = {'.h': 'header file'}
header_keys = header.keys()

sp_header_files = {'<stdio.h>':'Standard Input Output Header','<string.h>':'String Manipulation Library'}

macros = {r'#\w+' : 'macro'}
macros_keys = macros.keys()

datatype = {'int': 'Integer','float' : 'Floating Point', 'char': 'Character','long': 'long int'}
datatype_keys = datatype.keys()

keyword = {'return' : 'keyword that returns a value from a block','for':'For'}
keyword_keys = keyword.keys()

delimiter = {';':'terminator symbol semicolon (;)'}
delimiter_keys = delimiter.keys()

blocks = {'{' : 'LPAREN', '}':'RPAREN'}
block_keys = blocks.keys()

builtin_functions = {'printf':'printf prints its argument on the console'}

non_identifiers = ['_','-','+','/','*','`','~','!','@','#','$','%','^','&','*','(',')','=','|','"',':',';','{'
,'}','[',']','<','>','?','/']

numerals = ['0','1','2','3','4','5','6','7','8','9','10']









##########################################
##                 Tokens
##########################################

class Token(object):
    '''
        type  : INT,FLOAT, PLUS, or EOF
        value : 1, 2. 3,'+', Null
    '''
    def __init__(self, type, value,line_no):
        
        self.type = type   
        self.value = value
        self.line_no = line_no
    def __str__(self):
        """String representation of the class instance.

        Eg:
            Token(INTEGER, 3)
            Token(PLUS '+')
        """
        return f'Token<{self.type}, {self.value},{self.line_no}>'

    def __repr__(self):
        return self.__str__()

