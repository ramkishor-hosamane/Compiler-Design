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



##########################################
##                 Tokens
##########################################

class Token(object):
    '''
        type  : INT,FLOAT, PLUS, or EOF
        value : 1, 2. 3,'+', Null
    '''
    def __init__(self, type, value):
        
        self.type = type   
        self.value = value
        
    def __str__(self):
        """String representation of the class instance.

        Eg:
            Token(INTEGER, 3)
            Token(PLUS '+')
        """
        return f'Token<{self.type}, {self.value}>'

    def __repr__(self):
        return self.__str__()





##########################################
##                 LEXER
##########################################

class Lexer(object):
    '''
        type  : INT,FLOAT, PLUS, or EOF
        value : 1, 2. 3,'+', Null
    '''
    def __init__(self, text):
        self.text = text   
        self.pos=-1
        self.current_char =  None

    def advance(self):
        self.pos+=1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None
        