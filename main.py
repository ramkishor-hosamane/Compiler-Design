from essentials import *

import re

dataFlag = False

with open('InputProg.c','r') as f:
    
    whole_program = f.read()
    line_count = 0
    program =  whole_program.split('\n')

    for line in program:
        line_count +=+1
        #print ("Line #"+str(line_count)+"\n"+ str(line))        
        tokens = line.split(' ')
        print ("Tokens are"+str(tokens))
        print ("\n Individual Properties of Line #"+str(line_count))
        for token in tokens:
            
            if '\r' in token:
                position = token.find('\r')
                token=token[:position]
            # print 1
            
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
            if dataFlag == True and (token not in non_identifiers) and ('()' not in token):
                print ("Identifier: "+str(token))
            if token in datatype_keys:
                print ("type is: "+ str(datatype[token]))
                dataFlag = True
            
            if token in keyword_keys:
                print (keyword[token])
                
            if token in delimiter:
                print ("Delimiter" + str(delimiter[token]))
            if '#' in token:
                match = re.search(r'#\w+', token)
                print ("Header"+ str(match.group()))
            if token in numerals:
                print (str(token)+ str(type(int(token))))
                
        dataFlag = False   
            
print ("________________________________________________")
print()
