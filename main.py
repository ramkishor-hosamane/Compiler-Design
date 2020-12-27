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
                exceptional_case_for_missing_datatype = True
                tokens_list.append((keyword[token],token,line_count))
                #print (keyword[token])

                
            if '#' in token:
                match = re.search(r'#\w+', token)
                exceptional_case_for_termination  =True
                tokens_list.append(('Header',str(match.group()),line_count))
                #print ("Header"+ str(match.group()))
            if token in numerals:
                exceptional_case_for_missing_datatype = True
                print (str(token))
        
        #print("Exceptional case now",exceptional_case_for_termination)
        stmt_termination_flag = is_statement_terminated(exceptional_case_for_termination,line)

        if not stmt_termination_flag:
            print("Statement not termiated at line :",line_count)
        
        if is_datatype_error(exceptional_case_for_missing_datatype,line):
           print(f"DAtatype error for line {line_count}")
        
        stmt_termination_flag = False
        exceptional_case_for_termination = False
        exceptional_case_for_missing_datatype = False
        data_flag = False   
        
#print(tokens_list)
pprint.pprint(tokens_list)            
print ("________________________________________________")
print()
