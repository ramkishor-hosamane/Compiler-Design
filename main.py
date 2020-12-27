from essentials import *
import pprint
import re
'''
1) missing semicoln ------ done
2) datatype error
3) mismatch parenthisis ---- done, Vinnu
if(condition);
for(i=0;i<n;i++);


'''
'''Checks if statement(line) is termianted or not
    exceptional case:
                     ->function definition
                     ->Header files
                     ->Blank lines
                     ->Flower braces

'''
identifiers = set()

def is_statement_terminated(exceptional_case_for_termination,line):
    if exceptional_case_for_termination:
        return True

    if len(line.strip())==0:
        return True
    else:
        if line[-1] ==";":
            return True
    return False

def is_datatype_error(exceptional_case_for_missing_datatype,line):
    if exceptional_case_for_missing_datatype:
        return False
    
    if len(line.strip()) == 0:
        return False
    
    if ("=" in line and line.split("=")[0].strip() in identifiers):
        print(line.split("=")[0])
        return False

    return True

def is_bracket_error(bracket_stack, bracket, line):    #function to check bracket error
    if (not bracket_stack and bracket == "}"):
        print(f"Parenthesis error for line {line_count}")
        print("\n\n")
    elif bracket_stack:
        if bracket_stack[-1] == "{" and bracket == "}":
            bracket_stack.pop()
        elif bracket == "=":
            print(f"Missing Parenthesis error")
            print("\n\n")
        else:
            bracket_stack.append(bracket)
    else:
        bracket_stack.append(bracket)

def is_identifier(token):
    pass



bracket_stack = []   #stack for bracket checks
data_flag = False
stmt_termination_flag =  False
tokens_list = []
exceptional_case_for_termination = False
exceptional_case_for_missing_datatype = False

with open('InputProg.c','r') as f:
    
    whole_program = f.read()

    #Dividing entire program w r t lines
    program =  whole_program.split('\n')

    for line_count,line in enumerate(program,1):
        
        tokens = line.split(' ')

        for token in tokens:
            
            #Block keys : {,}
            if token in block_keys:

                exceptional_case_for_termination = True
                exceptional_case_for_missing_datatype = True
                is_bracket_error(bracket_stack,token,line_count)   #check for bracket error
                tokens_list.append((blocks[token],token,line_count))
 
                
            elif token in optr_keys:
                tokens_list.append((operators[token],token,line_count))
                
                
            elif token in comment_keys:
                tokens_list.append((comments[token],token,line_count))
                exceptional_case_for_termination = True
                exceptional_case_for_missing_datatype = True
                
            elif token in macros_keys:
                exceptional_case_for_termination = True
                tokens_list.append((macros[token],token,line_count))

                exceptional_case_for_missing_datatype = True
                
            elif '.h' in token:
                exceptional_case_for_termination = True
                tokens_list.append((sp_header_files[token],token,line_count))

                exceptional_case_for_missing_datatype = True
                
            elif '()' in token:
                exceptional_case_for_termination  =True
                exceptional_case_for_missing_datatype = True
                tokens_list.append(('Function',str(token),line_count))
                #print ("Function named "+ str(token))
            
        
                    


            #function definition 
            elif data_flag == True and '()' in token:
                exceptional_case_for_termination = True

            #function call  a= (1+2) * 4 
            elif (re.search(r'([a-zA-Z_{1}][a-zA-Z0-9_]+)(?=\()',line)) and '(' in token and line.strip()[-1]==";":
                exceptional_case_for_missing_datatype = True
                check = token.split('(')[0]
                if (check in keyword):
                    tokens_list.append((keyword[check],check,line_count))
                else:
                    tokens_list.append(("User defined function",check,line_count))

              

            elif token in datatype_keys:
                tokens_list.append((datatype[token],token,line_count))
                data_flag = True
            
            elif token in keyword_keys: 
                exceptional_case_for_missing_datatype = True
                tokens_list.append((keyword[token],token,line_count))

                
            elif '#' in token:
                match = re.search(r'#\w+', token)
                exceptional_case_for_termination  =True
                tokens_list.append(('Header',str(match.group()),line_count))

            elif token.strip().strip(";") in numerals:
                exceptional_case_for_missing_datatype = True

            
            
            elif re.search(r'[_a-zA-Z][_a-zA-Z0-9]{0,30}', line) and len(token.strip().strip(";")) != 0:
                stripped_token = token.strip().strip(";")
                if not stripped_token[0].isdigit() :
                    if data_flag == True:
                        #print("Identifier: " , stripped_token)
                        identifiers.add(stripped_token)
                        tokens_list.append(('Identifier',str(token),line_count))
                        exceptional_case_for_missing_datatype = True
                    else:
                        if stripped_token not in identifiers:
                            pass
                            #print(f"Identifier {stripped_token} is not declared")
                            #print(f"This is identifiers {identifiers} und diese ist {stripped_token}")
        #print("Exceptional case now",exceptional_case_for_termination)
        stmt_termination_flag = is_statement_terminated(exceptional_case_for_termination,line)

        if not stmt_termination_flag:
            print("Statement not termiated at line :",line_count)
            print("\n\n");        

        if is_datatype_error(exceptional_case_for_missing_datatype,line):
           print(f"Datatype error for line {line_count}")
           print("\n\n");        
        stmt_termination_flag = False
        exceptional_case_for_termination = False
        exceptional_case_for_missing_datatype = False
        data_flag = False
        
is_bracket_error(bracket_stack, "=", line_count)  #checking if all brackets have their pairs even after pgm is done

print ("________________________________________________")
print("Name \t \t \t Token \t \t \t Line number")        
pprint.pprint(tokens_list)
print ("________________________________________________")
print()
