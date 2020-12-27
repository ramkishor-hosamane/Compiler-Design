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




operators = { '=': 'Assignment Operator','+': 'Additon Operator', '-' : 'Substraction Operator', '/' : 'Division Operator', '*': 'Multiplication Operator', '++' : 'increment Operator', '--' : 'Decrement Operator','%':'Modulus operator','==':'Equal to','!=':'Not equal to','&&':'Logical AND','||':'Logical OR','!':'Logical NOT'}
optr_keys = operators.keys()

comments = {r'//' : 'Single Line Comment',r'/*' : 'Multiline Comment Start', r'*/' : 'Multiline Comment End', '/**/' : 'Empty Multiline comment'}
comment_keys = comments.keys()

header = {'.h': 'header file'}
header_keys = header.keys()

sp_header_files = {'<stdio.h>':'Standard I/O Functions','<string.h>':'String Manipulation Library','<conio.h>':'Console I/O functions','<stdlib.h>':'General utility functions','<math.h>':'Mathematics function','<time.h>':'Time and Date functions'}

macros = {r'#\w+' : 'macro'}
macros_keys = macros.keys()

datatype = {'int': 'Integer','float' : 'Floating Point', 'char': 'Character','long': 'long int','string':'String'}
datatype_keys = datatype.keys()

keyword = {'return' : 'Return statement','for':'Loop','printf': "Printing function",'scanf':'Input function','auto':'Automatic variable','break':'Break statement','switch':'Switch statement','if':'condition statement','while':'Loop','continue':'Continue','default':'Default'}
keyword_keys = keyword.keys()

delimiter = {';':'Statement terminator'}
delimiter_keys = delimiter.keys()

blocks = {'{' : 'LPAREN', '}':'RPAREN'}
block_keys = blocks.keys()


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

