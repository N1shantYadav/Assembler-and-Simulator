import sys

f = sys.stdin.readlines()

commandList = []
registers = []
lineCount = -1
varCount = 0
varList = []
varAddress = []
labelList = []
labelCount = 0
standard = ['add', 'sub', 'mov', 'ld', 'st', 'mul', 'div',"xor","or","and","addf","subf","rs","ls","jmp","jlt","jgt","je",'not','cmp','hlt']

#reading the file
for line in f:
    if line[-1] == '\n':
        commandList.append(line[:-1])
    else:
        commandList.append(line)
        
for command in commandList:
    wordList = command.split()

    if wordList[0] == 'var':
        pass
    else:
        lineCount += 1

#creating register_list
for i in range(0,16):
    registers.append(-1)
    
#function to convert decimal to 7-bit binary in string format
def bin_func(dec):
    
    if len(str(bin(dec).replace("0b", ""))) == 1:
        return '000000' + str(bin(int(dec)).replace("0b", ""))
    elif len(str(bin(dec).replace("0b", ""))) == 2:
        return '00000' + str(bin(int(dec)).replace("0b", ""))
    elif len(str(bin(dec).replace("0b", ""))) == 3:
        return '0000' + str(bin(int(dec)).replace("0b", ""))
    elif len(str(bin(dec).replace("0b", ""))) == 4:
        return '000' + str(bin(int(dec)).replace("0b", ""))
    elif len(str(bin(dec).replace("0b", ""))) == 5:
        return '00' + str(bin(int(dec)).replace("0b", ""))
    elif len(str(bin(dec).replace("0b", ""))) == 6:
        return '0' + str(bin(int(dec)).replace("0b", ""))
    elif len(str(bin(dec).replace("0b", ""))) == 7:
        return str(bin(int(dec)).replace("0b", ""))

#function for returning register address
def reg(r):
    
    if r == 'R0':
        return '000'
    elif r == 'R1':
        return '001'
    elif r == 'R2':
        return '010'
    elif r == 'R3':
        return '011'
    elif r == 'R4':
        return '100'
    elif r == 'R5':
        return '101'
    elif r == 'R6':
        return '110'
    elif r == 'FLAGS':
        return '111'
    
count1 = lineCount    
labelDict = {}

for command in commandList:
    wordList = command.split()

    if wordList[0] == 'jmp' or wordList[0] == 'jlt' or wordList[0] == 'jgt' or wordList[0] == 'je':
        labelList.append(wordList[1])
        
newCount = -1

for command in commandList:
    wordList = command.split()
    
    if wordList[0] == 'var':
        pass
    
    else:
        newCount += 1
    
        if wordList[0][:-1] in labelList:
            labelDict[wordList[0][:-1]] = bin_func(newCount)
        
for command in commandList:
    wordList = command.split()
    
    if wordList[0] == 'var':
        
        varList.append(wordList[1])
               
for var in varList:
    
    count1 += 1
    varAddress.append(bin_func(count1))
    
for command in commandList:
    wordList = command.split()

    if wordList[0] == 'mov':
        
        if wordList[2][0] == '$':
            
            r = wordList[1]
            imm = int(wordList[2][1:])
            
            #mov_imm(r, imm)
            
            sys.stdout.write('00010' + '0' + reg(r) + bin_func(imm) + '\n')
        
        else:
            
            r1 = wordList[1]
            r2 = wordList[2]
            
            #mov_reg(r1, r2)
            
            sys.stdout.write('00011' + '00000' + reg(r1) + reg(r2) + '\n')
                      
    elif wordList[0] == 'add':
        
        r1 = wordList[1]
        r2 = wordList[2]
        r3 = wordList[3]
        
        #add(r1, r2, r3)
        
        sys.stdout.write('00000' + '00' + reg(r1) + reg(r2) + reg(r3) + '\n')
        
    elif wordList[0] == 'sub':
        
        r1 = wordList[1]
        r2 = wordList[2]
        r3 = wordList[3]
        
        #sub(r1, r2, r3)
        
        sys.stdout.write('00001' + '00' + reg(r1) + reg(r2) + reg(r3) + '\n')
        
    elif wordList[0] == 'ld':
    
        r = wordList[1]
        var = wordList[2]
        varIndex = varList.index(var)
        
        sys.stdout.write('00100' + '0' + reg(r) + str(varAddress[varIndex]) + '\n')
        
    elif wordList[0] == 'st':
        
        r = wordList[1]
        var = wordList[2] 
        varIndex = varList.index(var)
        
        sys.stdout.write('00101' + '0' + reg(r)  + str(varAddress[varIndex]) + '\n')
        
    elif wordList[0] == 'mul':
        
        r1 = wordList[1]
        r2 = wordList[2]
        r3 = wordList[3]
        
        sys.stdout.write('00110' + '00' + reg(r1) + reg(r2) + reg(r3) + '\n')
        
    elif wordList[0] == 'div':
        
        r1 = wordList[1]
        r2 = wordList[2]
        r3 = wordList[3]
        
        sys.stdout.write('00111' + '00' + reg(r1)  + reg(r2) + reg(r3) + '\n')
        
    elif wordList[0] == 'rs':
        
        r = wordList[1]
        imm = int(wordList[2][1:])
        
        sys.stdout.write('01000' + '0' + reg(r) + bin_func(imm) + '\n')
        
    elif wordList[0] == 'ls':
        
        r = wordList[1]
        imm = int(wordList[2][1:])
        
        sys.stdout.write('01001' + '0' + reg(r) + bin_func(imm) + '\n')
        
    elif wordList[0] == 'xor':
        
        r1 = wordList[1]
        r2 = wordList[2]
        r3 = wordList[3]
        
        sys.stdout.write('01010' + '00' + reg(r1) + reg(r2) + reg(r3) + '\n')
        
    elif wordList[0] == 'or':
        
        r1 = wordList[1]
        r2 = wordList[2]
        r3 = wordList[3]
        
        sys.stdout.write('01011' + '00' + reg(r1) + reg(r2) + reg(r3) + '\n')
        
    elif wordList[0] == 'and':
        
        r1 = wordList[1]
        r2 = wordList[2]
        r3 = wordList[3]
        
        sys.stdout.write('01100' + '00' + reg(r1) + reg(r2) + reg(r3) + '\n')
        
    elif wordList[0] == 'not':
        
        r1 = wordList[1]
        r2 = wordList[2]
            
        sys.stdout.write('01101' + '00000' + reg(r1) + reg(r2) + '\n')
        
    elif wordList[0] == 'cmp':
        
        r1 = wordList[1]
        r2 = wordList[2]
            
        sys.stdout.write('01110' + '00000' + reg(r1) + reg(r2) + '\n')
        
    elif wordList[0] == 'jmp':
    
        var = wordList[1] 
        
        sys.stdout.write('01111' + '0000' + str(labelDict[var]) + '\n')
        
    elif wordList[0] == 'jlt':
        
        var = wordList[1] 
        
        sys.stdout.write('11100' + '0000' + str(labelDict[var]) + '\n')
        
    elif wordList[0] == 'jgt':
        
        var = wordList[1] 
        
        sys.stdout.write('11101' + '0000' + str(labelDict[var]) + '\n')
        
    elif wordList[0] == 'je':
        
        var = wordList[1] 
        
        sys.stdout.write('11111' + '0000' + str(labelDict[var]) + '\n')
        
    elif wordList[0] == 'addf':
        
        r1 = wordList[1]
        r2 = wordList[2]
        r3 = wordList[3]
        
        #add(r1, r2, r3)
        
        sys.stdout.write('10000' + '00' + reg(r1) + reg(r2) + reg(r3) + '\n')
        
    elif wordList[0] == 'subf':
        
        r1 = wordList[1]
        r2 = wordList[2]
        r3 = wordList[3]
        
        #add(r1, r2, r3)
        
        sys.stdout.write('10001' + '00' + reg(r1) + reg(r2) + reg(r3) + '\n')
    
    elif wordList[0] == 'hlt':
        
        sys.stdout.write('1101000000000000')
        
    elif wordList[0][:-1] in labelList:
        wordList.remove(wordList[0])
        
        if wordList[0] == 'mov':
        
            if wordList[2][0] == '$':
            
                r = wordList[1]
                imm = int(wordList[2][1:])
            
                #mov_imm(r, imm)
                
                sys.stdout.write('00010' + '0' + reg(r) + bin_func(imm) + '\n')
        
            else:
            
                r1 = wordList[1]
                r2 = wordList[2]
            
                #mov_reg(r1, r2)
            
                sys.stdout.write('00011' + '00000' + reg(r1) + reg(r2) + '\n')
                      
        elif wordList[0] == 'add':
        
            r1 = wordList[1]
            r2 = wordList[2]
            r3 = wordList[3]
        
            #add(r1, r2, r3)
        
            sys.stdout.write('00000' + '00' + reg(r1) + reg(r2) + reg(r3) + '\n')
        
        elif wordList[0] == 'sub':
        
            r1 = wordList[1]
            r2 = wordList[2]
            r3 = wordList[3]
        
            #sub(r1, r2, r3)
        
            sys.stdout.write('00001' + '00' + reg(r1) + reg(r2) + reg(r3) + '\n')
        
        elif wordList[0] == 'ld':
    
            r = wordList[1]
            var = wordList[2]
            varIndex = varList.index(var)
        
            sys.stdout.write('00100' + '0' + reg(r) + str(varAddress[varIndex]) + '\n')
        
        elif wordList[0] == 'st':
        
            r = wordList[1]
            var = wordList[2] 
            varIndex = varList.index(var)
        
            sys.stdout.write('00101' + '0' + reg(r)  + str(varAddress[varIndex]) + '\n')
        
        elif wordList[0] == 'mul':
        
            r1 = wordList[1]
            r2 = wordList[2]
            r3 = wordList[3]
        
            sys.stdout.write('00110' + '00' + reg(r1) + reg(r2) + reg(r3) + '\n')
        
        elif wordList[0] == 'div':
        
            r1 = wordList[1]
            r2 = wordList[2]
            r3 = wordList[3]
        
            sys.stdout.write('00111' + '00' + reg(r1)  + reg(r2) + reg(r3) + '\n')
        
        elif wordList[0] == 'rs':
        
            r = wordList[1]
            imm = int(wordList[2][1:])
        
            sys.stdout.write('01000' + '0' + reg(r) + bin_func(imm) + '\n')
        
        elif wordList[0] == 'ls':
        
            r = wordList[1]
            imm = int(wordList[2][1:])
        
            sys.stdout.write('01001' + '0' + reg(r) + bin_func(imm) + '\n')
        
        elif wordList[0] == 'xor':
        
            r1 = wordList[1]
            r2 = wordList[2]
            r3 = wordList[3]
        
            sys.stdout.write('01010' + '00' + reg(r1) + reg(r2) + reg(r3) + '\n')
        
        elif wordList[0] == 'or':
        
            r1 = wordList[1]
            r2 = wordList[2]
            r3 = wordList[3]
        
            sys.stdout.write('01011' + '00' + reg(r1) + reg(r2) + reg(r3) + '\n')
        
        elif wordList[0] == 'and':
        
            r1 = wordList[1]
            r2 = wordList[2]
            r3 = wordList[3]
        
            sys.stdout.write('01100' + '00' + reg(r1) + reg(r2) + reg(r3) + '\n')

        elif wordList[0] == 'not':
        
            r1 = wordList[1]
            r2 = wordList[2]
            
            sys.stdout.write('01101' + '00000' + reg(r1) + reg(r2) + '\n')
        
        elif wordList[0] == 'cmp':
        
            r1 = wordList[1]
            r2 = wordList[2]
            
            sys.stdout.write('01110' + '00000' + reg(r1) + reg(r2) + '\n')
        
        elif wordList[0] == 'jmp':
        
            var = wordList[1] 
        
            sys.stdout.write('01111' + '0000' + str(varAddress[varIndex]) + '\n')
        
        elif wordList[0] == 'jlt':
        
            var = wordList[1] 
        
            sys.stdout.write('11100' + '0000' + str(varAddress[varIndex]) + '\n')

        elif wordList[0] == 'jgt':
        
            var = wordList[1] 
        
            sys.stdout.write('11101' + '0000' + str(varAddress[varIndex]) + '\n')
        
        elif wordList[0] == 'je':
        
            var = wordList[1] 
        
            sys.stdout.write('11111' + '0000' + str(varAddress[varIndex]) + '\n')
        
        elif wordList[0] == 'addf':
        
            r1 = wordList[1]
            r2 = wordList[2]
            r3 = wordList[3]
        
            #add(r1, r2, r3)
        
            sys.stdout.write('10000' + '00' + reg(r1) + reg(r2) + reg(r3) + '\n')

        elif wordList[0] == 'subf':
        
            r1 = wordList[1]
            r2 = wordList[2]
            r3 = wordList[3]
        
            #add(r1, r2, r3)
        
            sys.stdout.write('10001' + '00' + reg(r1) + reg(r2) + reg(r3) + '\n')
        
        elif wordList[0] == 'hlt':
        
            sys.stdout.write('1101000000000000')