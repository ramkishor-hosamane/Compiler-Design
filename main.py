from essentials import *

import re

data_flag = False

with open('InputProg.c','r') as f:
    
    whole_program = f.read()
    #Dividing entire program w r t lines
    program =  whole_program.split('\n')

    for line_count,line in enumerate(program,1):

        #print ("Line #"+str(line_count)+"\n"+ str(line))        
        tokens = line.split(' ')
        print ("Tokens are"+str(tokens))
        print ("\n Individual Properties of Line #"+str(line_count))
        for token in tokens:
            
            if '\r' in token:
                print("Got it",token)
                position = token.find('\r')
                token=token[:position]
            
            #Block keys : {,}
            if token in block_keys:
                print (blocks[token])
            if token in optr_keys:
                print ("Operator is: "+ str(operators[token]))
            if token in comment_keys:
                print ("Comment Type: "+ str(comments[token]))
            if token in macros_keys:
                print ("Macro is: "+ str(macros[token]))
            if '.h' in token:
                print ("Header File is: "+str(token)+str(sp_header_files[token]))
            if '()' in token:
                print ("Function named"+ str(token))           
            if data_flag == True and (token not in non_identifiers) and ('()' not in token):
                print ("Identifier: "+str(token))
            if token in datatype_keys:
                print ("type is: "+ str(datatype[token]))
                data_flag = True
            
            if token in keyword_keys:
                print (keyword[token])
                
            if token in delimiter:
                print ("Delimiter" + str(delimiter[token]))
            if '#' in token:
                match = re.search(r'#\w+', token)
                print ("Header"+ str(match.group()))
            if token in numerals:
                print (str(token)+ str(type(int(token))))
                
        data_flag = False   
            
print ("________________________________________________")
print()
