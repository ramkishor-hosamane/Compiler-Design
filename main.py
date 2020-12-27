from essentials import *
import pprint

import re
'''
1) missing semicoln ------ done
2) datatype error
3) mismatch parenthisis
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

def is_identifier(token):
    pass



    return True

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
<<<<<<< HEAD
<<<<<<< HEAD
                exceptional_case_for_missing_datatype = True
                tokens_list.append(Token(blocks[token],token,line_count))
                print(blocks[token])
                
            elif token in optr_keys:
                
                print("Operator is: " + str(operators[token]))
                
            elif token in comment_keys:
                exceptional_case_for_termination = True
                exceptional_case_for_missing_datatype = True
                print("Comment Type: " + str(comments[token]))
                
            elif token in macros_keys:
                exceptional_case_for_termination = True
                exceptional_case_for_missing_datatype = True
                print("Macro is: " + str(macros[token]))
                
            elif '.h' in token:
                exceptional_case_for_termination = True
                exceptional_case_for_missing_datatype = True
                print("Header File is: " + str(token) + str(sp_header_files[token]))
                
            elif '()' in token:
                #exceptional_case_for_termination  =True
                exceptional_case_for_missing_datatype = True
                print ("Function named"+ str(token))
            
        
                    

=======
=======
>>>>>>> 7c470d051d141bae5c2ab6c623daed987e2bde27
                tokens_list.append((blocks[token],token,line_count))

                #print (blocks[token])
            if token in optr_keys:
                tokens_list.append((operators[token],token,line_count))
                #print ("Operator is: "+ str(operators[token]))
            if token in comment_keys:
                exceptional_case_for_termination = True
                tokens_list.append((comments[token],token,line_count))
                #print ("Comment Type: "+ str(comments[token]))
            if token in macros_keys:
                exceptional_case_for_termination = True
                tokens_list.append((macros[token],token,line_count))
                #print ("Macro is: "+ str(macros[token]))
            if '.h' in token:
                exceptional_case_for_termination = True
                tokens_list.append((sp_header_files[token],token,line_count))
                #print ("Header File is: "+str(token)+str(sp_header_files[token]))
            if '()' in token:
                #exceptional_case_for_termination  =True
                tokens_list.append(('Function',str(token),line_count))
                #print ("Function named"+ str(token))

            if (token not in non_identifiers) and ('()' not in token):
                if data_flag == True :
                    tokens_list.append(('Identifier',str(token),line_count))
                    #print ("Identifier: "+str(token))
<<<<<<< HEAD
>>>>>>> 400b581491aab5cc22cd153690177a777045b035

            #function definition 
            elif data_flag == True and '()' in token:
                exceptional_case_for_termination = True

            #function call
            elif (re.search(r'([a-zA-Z_{1}][a-zA-Z0-9_]+)(?=\()',line)):
                exceptional_case_for_missing_datatype = True
               

<<<<<<< HEAD
            elif token in datatype_keys:
                print ("type is: "+ str(datatype[token]))
=======
            if token in datatype_keys:
                tokens_list.append((datatype[token],token,line_count))
                #print ("type is: "+ str(datatype[token]))
>>>>>>> 400b581491aab5cc22cd153690177a777045b035
                data_flag = True
            
            elif token in keyword_keys: 
=======

            #function definition 
            if data_flag == True and '()' in token:
                exceptional_case_for_termination = True

            #function call
            if (re.search(r'([a-zA-Z_{1}][a-zA-Z0-9_]+)(?=\()',line)):
                exceptional_case_for_missing_datatype = True
               

            if token in datatype_keys:
                tokens_list.append((datatype[token],token,line_count))
                #print ("type is: "+ str(datatype[token]))
                data_flag = True
            
            if token in keyword_keys: 
>>>>>>> 7c470d051d141bae5c2ab6c623daed987e2bde27
                exceptional_case_for_missing_datatype = True
                tokens_list.append((keyword[token],token,line_count))
                #print (keyword[token])

                
            elif '#' in token:
                match = re.search(r'#\w+', token)
                exceptional_case_for_termination  =True
<<<<<<< HEAD
<<<<<<< HEAD

                print ("Header"+ str(match.group()))
            elif token.strip().strip(";") in numerals:
=======
                tokens_list.append(('Header',str(match.group()),line_count))
                #print ("Header"+ str(match.group()))
            if token in numerals:
>>>>>>> 400b581491aab5cc22cd153690177a777045b035
                exceptional_case_for_missing_datatype = True
                
            
            
            elif re.search(r'[_a-zA-Z][_a-zA-Z0-9]{0,30}', line) and len(token.strip().strip(";")) != 0:
                stripped_token = token.strip().strip(";")
                if not stripped_token[0].isdigit() :
                    if data_flag == True:
                        print("Identifier: " , stripped_token)
                        identifiers.add(stripped_token)
                        print(f"{stripped_token} added")
                        exceptional_case_for_missing_datatype = True
                    else:
                        if stripped_token not in identifiers:
                            print(f"Identifier {stripped_token} is not declared")
                            print(f"This is identifiers {identifiers} und diese ist {stripped_token}")
=======
                tokens_list.append(('Header',str(match.group()),line_count))
                #print ("Header"+ str(match.group()))
            if token in numerals:
                exceptional_case_for_missing_datatype = True
                print (str(token))
        
>>>>>>> 7c470d051d141bae5c2ab6c623daed987e2bde27
        #print("Exceptional case now",exceptional_case_for_termination)
        stmt_termination_flag = is_statement_terminated(exceptional_case_for_termination,line)

        if not stmt_termination_flag:
            print("Statement not termiated at line :",line_count)
        
        if is_datatype_error(exceptional_case_for_missing_datatype,line):
           print(f"DAtatype error for line {line_count}")
        
        stmt_termination_flag = False
        exceptional_case_for_termination = False
        exceptional_case_for_missing_datatype = False
<<<<<<< HEAD
        data_flag = False
        
        
        
#print(tokens_list)
=======
        data_flag = False   
        
#print(tokens_list)
print ("________________________________________________")
print ("name \t \t \t Token \t \t \t Line number")
>>>>>>> 7c470d051d141bae5c2ab6c623daed987e2bde27
pprint.pprint(tokens_list)            
print ("________________________________________________")
print()
