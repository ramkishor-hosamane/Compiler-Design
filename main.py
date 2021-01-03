from essentials import *
import pprint
import TableIt
import sys
import re

#Taking input program from commandline
input_program = sys.argv[1]

identifiers = set()

#Function to check if statement is terminated by ';'
def is_statement_terminated(exceptional_case_for_termination,line):
    if exceptional_case_for_termination:
        return True

    #Blank lines
    if len(line.strip())==0:
        return True
    else:
        if line[-1] ==";":
            return True
    return False

#
def is_datatype_error(exceptional_case_for_missing_datatype,line):
    if exceptional_case_for_missing_datatype:
        return False
    
    if len(line.strip()) == 0:
        return False

    if ("=" in line and line.split("=")[0].strip() in identifiers):
        print(line.split("=")[0])
        return False

    return True


#function to check bracket error
def is_bracket_error(bracket_stack, bracket, line):    
    if (not bracket_stack and bracket == "}"):
        print(f"Parenthesis error for line {line_no}")
        print("\n\n")
    elif bracket_stack:
        if bracket_stack[-1] == "{" and bracket == "}":
            bracket_stack.pop()
        elif bracket == "program_ended":
            print(f"Missing Parenthesis error {line_no}")
            print("\n\n")
        else:
            bracket_stack.append(bracket)
    else:
        bracket_stack.append(bracket)


#stack for bracket checks
bracket_stack = []   
data_flag = False
stmt_termination_flag =  False
tokens_list = []
exceptional_case_for_termination = False
exceptional_case_for_missing_datatype = False

with open(input_program,'r') as f:
    
    whole_program = f.read()

    #Dividing entire program w r t lines
    program =  whole_program.split('\n')

    for line_no,line in enumerate(program,1):
        
        tokens = line.split(' ')

        for token in tokens:
            
            #Block keys : {,}
            if token in block_keys:

                exceptional_case_for_termination = True
                exceptional_case_for_missing_datatype = True
                
                #check for bracket error
                is_bracket_error(bracket_stack,token,line_no)   
                tokens_list.append((blocks[token],token,line_no))
 
                
            elif token in optr_keys:
                tokens_list.append((operators[token],token,line_no))
                
                
            elif token in comment_keys:
                tokens_list.append((comments[token],token,line_no))
                exceptional_case_for_termination = True
                exceptional_case_for_missing_datatype = True
                
            elif token in macros_keys:
                exceptional_case_for_termination = True
                tokens_list.append((macros[token],token,line_no))

                exceptional_case_for_missing_datatype = True
                
            elif '.h' in token:
                exceptional_case_for_termination = True
                tokens_list.append((sp_header_files[token],token,line_no))

                exceptional_case_for_missing_datatype = True
                
            #Function    
            elif '()' in token:
                exceptional_case_for_termination  =True
                exceptional_case_for_missing_datatype = True
                tokens_list.append(('Function',str(token),line_no))
            
        
                    


            #function definition 
            elif data_flag == True and '()' in token:
                exceptional_case_for_termination = True
            #function call  a= (1+2) * 4 
            elif (re.search(r'([a-zA-Z_{1}][a-zA-Z0-9_]+)(?=\()',line)) and '(' in token and line.strip()[-1]==";":
                exceptional_case_for_missing_datatype = True
                check = token.split('(')[0]
                if (check in keyword):
                    tokens_list.append((keyword[check],check,line_no))
                else:
                    tokens_list.append(("User defined function",check,line_no))

              

            elif token in datatype_keys:
                tokens_list.append((datatype[token],token,line_no))
                data_flag = True
            
            elif token in keyword_keys: 
                exceptional_case_for_missing_datatype = True
                tokens_list.append((keyword[token],token,line_no))

            elif token.strip().strip(";") in numerals:
                exceptional_case_for_missing_datatype = True

            
            #Identifying identifier
            elif re.search(r'[_a-zA-Z][_a-zA-Z0-9]{0,30}', line) and ')' not in token and '#' not in token and '(' not in token  and len(token.strip().strip(";")) != 0:
                stripped_token = token.strip().strip(";")
                #print(stripped_token,"is identifier")
                if not stripped_token[0].isdigit() :
                    #If token(variable) is declaring
                    if data_flag == True :
                        identifiers.add(stripped_token)
                        tokens_list.append(('Identifier',str(token),line_no))
                        exceptional_case_for_missing_datatype = True

                    else:
                        #Check if the token is already defined
                        if stripped_token not in identifiers:
                            print(f"Identifier {stripped_token} is not declared")
        stmt_termination_flag = is_statement_terminated(exceptional_case_for_termination,line)

        if not stmt_termination_flag:
            print("Statement not termiated at line :",line_no)
            print("\n\n");        

        if is_datatype_error(exceptional_case_for_missing_datatype,line):
           print(f"Datatype error for line {line_no}")
           print("\n\n");        
        stmt_termination_flag = False
        exceptional_case_for_termination = False
        exceptional_case_for_missing_datatype = False
        data_flag = False

#checking if all brackets have their pairs even after pgm is done        
is_bracket_error(bracket_stack, "program_ended", line_no)  

print ("-------------------------------------------------------------------------------------")
print("|     \tName\t\t\t\t Token \t\t\t Line number\t    | ")        
#pprint.pprint(tokens_list)
TableIt.printTable(tokens_list)
print()
