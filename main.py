from essentials import *

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
def is_statement_terminated(exceptional_case_for_termination,line):
    if exceptional_case_for_termination:
        return True

    if len(line)==0:
        return True
    else:
        if line[-1] ==";":
            return True
    return False



data_flag = False
stmt_termination_flag =  False
tokens_list = []
exceptional_case_for_termination = False
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
                tokens_list.append(Token(blocks[token],token,line_count))

                print (blocks[token])
            if token in optr_keys:
                print ("Operator is: "+ str(operators[token]))
            if token in comment_keys:
                exceptional_case_for_termination = True
                print ("Comment Type: "+ str(comments[token]))
            if token in macros_keys:
                exceptional_case_for_termination = True
                print ("Macro is: "+ str(macros[token]))
            if '.h' in token:
                exceptional_case_for_termination = True
                print ("Header File is: "+str(token)+str(sp_header_files[token]))
            if '()' in token:
                #exceptional_case_for_termination  =True
                print ("Function named"+ str(token))

            if (token not in non_identifiers) and ('()' not in token):
                if data_flag == True :
                    print ("Identifier: "+str(token))

            if data_flag == True and '()' in token:
                exceptional_case_for_termination  =True
            if token in datatype_keys:
                print ("type is: "+ str(datatype[token]))
                data_flag = True
            
            if token in keyword_keys:
                print (keyword[token])

                
            if '#' in token:
                match = re.search(r'#\w+', token)
                exceptional_case_for_termination  =True

                print ("Header"+ str(match.group()))
            if token in numerals:
                print (str(token)+ str(type(int(token))))
        
        #print("Exceptional case now",exceptional_case_for_termination)
        stmt_termination_flag = is_statement_terminated(exceptional_case_for_termination,line)

        if not stmt_termination_flag:
            print("Statement not termiated at line :",line_count)

        stmt_termination_flag = False
        exceptional_case_for_termination = False
        data_flag = False   
        
print(tokens_list)            
print ("________________________________________________")
print()
