import sys

#file = open(r"C:\Users\nisha\Downloads\trial.txt")
#f = file.readlines()

#memory = open(r"C:\Users\nisha\Downloads\trial_mem.txt", "w")

commandList = []
registers = []
lineCount = -1
varCount = 0
varList = []
varAddress = []
labelList = []
labelCount = 0
standard = ['add', 'sub', 'mov', 'ld', 'st', 'mul', 'div',"xor","or","and","addf","subf","rs","ls","jmp","jlt","jgt","je",'not','cmp','hlt']
temp_count = 0

#reading the file
#for line in f:
#    if line[-1] == '\n':
#        commandList.append(line[:-1])
#    else:
#        commandList.append(line)
        
#for command in commandList:
#    wordList = command.split()

#    if wordList[0] == 'var':
#        pass
#    else:
#        lineCount += 1
    
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
            
#simulator section

registers = []
for i in range(0,7):
    registers.append('0000000000000000')

memory = sys.stdin.readlines()
mem_list = []

v = 0
l = 0
g = 0
e = 0

for line in memory:
    
    if line[-1] == "\n":
        mem_list.append(line[:-1])
    else:
        mem_list.append(line)

#function to convert decimal to 16-bit binary in string format
def bin_func_16(dec):
    
    if dec == 0:
        return '0000000000000000'
    else:
        if len(str(bin(dec).replace("0b", ""))) == 1:
            return '000000000000000' + str(bin(int(dec)).replace("0b", ""))
        elif len(str(bin(dec).replace("0b", ""))) == 2:
            return '00000000000000' + str(bin(int(dec)).replace("0b", ""))
        elif len(str(bin(dec).replace("0b", ""))) == 3:
            return '0000000000000' + str(bin(int(dec)).replace("0b", ""))
        elif len(str(bin(dec).replace("0b", ""))) == 4:
            return '000000000000' + str(bin(int(dec)).replace("0b", ""))
        elif len(str(bin(dec).replace("0b", ""))) == 5:
            return '00000000000' + str(bin(int(dec)).replace("0b", ""))
        elif len(str(bin(dec).replace("0b", ""))) == 6:
            return '0000000000' + str(bin(int(dec)).replace("0b", ""))
        elif len(str(bin(dec).replace("0b", ""))) == 7:
            return '000000000' + str(bin(int(dec)).replace("0b", ""))
        elif len(str(bin(dec).replace("0b", ""))) == 8:
            return '00000000' + str(bin(int(dec)).replace("0b", ""))
        elif len(str(bin(dec).replace("0b", ""))) == 9:
            return '0000000' + str(bin(int(dec)).replace("0b", ""))
        elif len(str(bin(dec).replace("0b", ""))) == 10:
            return '000000' + str(bin(int(dec)).replace("0b", ""))
        
def print_flags(v, l, g, e):
    return '000000000000' + str(v) + str(l) + str(g) + str(e) 
        
mem_size = len(mem_list)
mem_num = 128 - mem_size

pc = 0
def execute(pc, v, l, g, e):

    sys.stdout.write(bin_func(pc) + '        ') 
    
    for i in registers:
        sys.stdout.write(i + ' ')
    
    sys.stdout.write(print_flags(v, l, g, e))
    
    prev_flag = print_flags(v, l, g, e)
    
    v_ = v
    l_ = l
    g_ = g
    e_ = e
    
    v = 0
    l = 0
    g = 0
    e = 0
    
    sys.stdout.write('\n')
    
def cmp_execute(pc):

    sys.stdout.write(bin_func(pc) + '        ') 
    
    for i in registers:
        sys.stdout.write(i + ' ')
    
    sys.stdout.write(print_flags())
    
    sys.stdout.write('\n')

for line in mem_list:
    
    if line[:5] == '00000':
        
        r1 = line[7:10]
        r2 = line[10:13]
        r3 = line[13:16]
        
        r1_dec = int(r1, 2)
        r2_dec = int(r2, 2)
        r3_dec = int(r3, 2)
        
        add_res = int(registers[r2_dec], 2) + int(registers[r3_dec], 2)
        
        if add_res > 65535:
            v = 1
            registers[r1_dec] = '0000000000000000'
        else:
            registers[r1_dec] = bin_func_16(int(add_res))
            
        execute(pc, v, l, g, e)
        v = 0
        l = 0
        g = 0
        e = 0
        pc += 1
        
    elif line[:5] == '00001':
        
        r1 = line[7:10]
        r2 = line[10:13]
        r3 = line[13:16]
        
        r1_dec = int(r1, 2)
        r2_dec = int(r2, 2)
        r3_dec = int(r3, 2)
        
        sub_res = int(registers[r2_dec], 2) - int(registers[r3_dec], 2)
        
        if r2 > r3:
            v = 1
            registers[r1_dec] = '0000000000000000'
        else:
            registers[r1_dec] = bin_func_16(int(sub_res))
        
        execute(pc, v, l, g, e)
        v = 0
        l = 0
        g = 0
        e = 0
        pc += 1
        
    elif line[:5] == '00010':
        r = line[6:9]
        imm = line[9:16]
        
        r_dec = int(r, 2)
        imm_dec = int(imm, 2)
        
        registers[r_dec] = bin_func_16(int(imm_dec))
        
        execute(pc, v, l, g, e)
        v = 0
        l = 0
        g = 0
        e = 0
        pc += 1
        
    elif line[:5] == '00011':
        r1 = line[10:13]
        r2 = line[13:16]
        
        if r2 == '111':
            r1_dec = int(r1, 2)
            registers[r1_dec] = print_flags(v_, l_, g_, e_)
        else:
            r1_dec = int(r1, 2)
            r2_dec = int(r2, 2)
        
            registers[r1_dec] = bin_func_16(int(r2_dec))
        
        execute(pc, v, l, g, e)
        v = 0
        l = 0
        g = 0
        e = 0
        pc += 1
        
    elif line[:5] == '00100':
        
        execute(pc, v, l, g, e)
        v = 0
        l = 0
        g = 0
        e = 0
        pc += 1
        
    elif line[:5] == '00101':
        
        r = line[6:9]
        r_dec = int(r, 2)
        
        memory = open(r"C:\Users\nisha\Downloads\trial_mem.txt", "a")
        memory.write(registers[r_dec])
        memory.write('\n')
        memory.close()
        
        execute(pc, v, l, g, e)
        v = 0
        l = 0
        g = 0
        e = 0
        pc += 1
        
    elif line[:5] == '00110':
        
        r1 = line[7:10]
        r2 = line[10:13]
        r3 = line[13:16]
        
        r1_dec = int(r1, 2)
        r2_dec = int(r2, 2)
        r3_dec = int(r3, 2)
        
        mul_res = int(registers[r2_dec], 2) * int(registers[r3_dec], 2)
        
        if mul_res > 65535:
            v = 1
            registers[r1_dec] = '0000000000000000'
        else:
            registers[r1_dec] = bin_func_16(int(mul_res))
            
        execute(pc, v, l, g, e)
        v = 0
        l = 0
        g = 0
        e = 0
        pc += 1
        
    elif line[:5] == '00111':
        
        r1 = line[10:13]
        r2 = line[13:16]
        
        r1_dec = int(r1, 2)
        r2_dec = int(r2, 2) 
        
        if r2_dec == 0:
            v = 1
            registers[0] = '0000000000000000'
            registers[1] = '0000000000000000'
        else:
            registers[0] = int(registers[r1_dec], 2) // int(registers[r2_dec], 2)
            registers[1] = int(registers[r1_dec], 2) %  int(registers[r2_dec], 2)
            
        execute(pc, v, l, g, e)
        v = 0
        l = 0
        g = 0
        e = 0
        pc += 1
        
    elif line[:5] == '01000':
        
        r = line[6:9]
        imm = line[9:16]
        
        r_dec = int(r, 2)
        imm_dec = int(imm, 2)
        
        registers[r_dec] = bin_func_16(int(registers[r_dec], 2)) >> imm_dec
        
        execute(pc, v, l, g, e)
        v = 0
        l = 0
        g = 0
        e = 0
        pc += 1
        
    elif line[:5] == '01001':
        
        r = line[6:9]
        imm = line[9:16]
        
        r_dec = int(r, 2)
        imm_dec = int(imm, 2)
        
        registers[r_dec] = bin_func_16(int(registers[r_dec], 2)) << imm_dec
        
        execute(pc, v, l, g, e)
        v = 0
        l = 0
        g = 0
        e = 0
        pc += 1
        
    elif line[:5] == '01010':
        
        r1 = line[7:10]
        r2 = line[10:13]
        r3 = line[13:16]
        
        r1_dec = int(r1, 2)
        r2_dec = int(r2, 2)
        r3_dec = int(r3, 2)
        
        registers[r3_dec] = bin_func_16(r2_dec ^ r3_dec)
                                       
        execute(pc, v, l, g, e)
        v = 0
        l = 0
        g = 0
        e = 0
        pc += 1
        
    elif line[:5] == '01011':
        
        r1 = line[7:10]
        r2 = line[10:13]
        r3 = line[13:16]
        
        r1_dec = int(r1, 2)
        r2_dec = int(r2, 2)
        r3_dec = int(r3, 2)
        
        registers[r3_dec] = bin_func_16(r2_dec | r3_dec)
                                       
        execute(pc, v, l, g, e)
        v = 0
        l = 0
        g = 0
        e = 0
        pc += 1
        
    elif line[:5] == '01100':
        
        r1 = line[7:10]
        r2 = line[10:13]
        r3 = line[13:16]
        
        r1_dec = int(r1, 2)
        r2_dec = int(r2, 2)
        r3_dec = int(r3, 2)
        
        registers[r3_dec] = bin_func_16(r2_dec & r3_dec)
                                       
        execute(pc, v, l, g, e)
        v = 0
        l = 0
        g = 0
        e = 0
        pc += 1
        
    elif line[:5] == '01101':
        
        r1 = line[10:13]
        r2 = line[13:16]
        
        r1_dec = int(r1, 2)
        r2_dec = int(r2, 2) 
        
        registers[r1_dec] = bin_func_16(~r2_dec)
            
        execute(pc, v, l, g, e)
        v = 0
        l = 0
        g = 0
        e = 0
        pc += 1
        
    elif line[:5] == '01110':
        
        r1 = line[10:13]
        r2 = line[13:16]
        
        r1_dec = int(r1, 2)
        r2_dec = int(r2, 2)
        
        if registers[r1_dec] < registers[r2_dec]:
            l = 1
        elif registers[r1_dec] > registers[r2_dec]:
            g = 1
        elif registers[r1_dec] == registers[r2_dec]:
            e = 1
            
        execute(pc, v, l, g, e)
        v_ = v
        l_ = l
        g_ = g
        e_ = e
        v = 0
        l = 0
        g = 0
        e = 0
        pc += 1
        
    elif line[:5] == '01111':
        
        execute(pc, v, l, g, e)
        v = 0
        l = 0
        g = 0
        e = 0
        pc += 1
        
    elif line[:5] == '11100':
        
        execute(pc, v, l, g, e)
        v = 0
        l = 0
        g = 0
        e = 0
        pc += 1
        
    elif line[:5] == '11101':
        
        execute(pc, v, l, g, e)
        v = 0
        l = 0
        g = 0
        e = 0
        pc += 1
        
    elif line[:5] == '11111':
        
        execute(pc, v, l, g, e)
        v = 0
        l = 0
        g = 0
        e = 0
        pc += 1
           
    elif line[:5] == '11010':
        
        execute(pc, v, l, g, e)
        v = 0
        l = 0
        g = 0
        e = 0
        
memory = open(r"C:\Users\nisha\Downloads\trial_mem.txt", "a")

for i in mem_list:
    sys.stdout.write(i + '\n')

for i in range(0, mem_num):
    sys.stdout.write("0000000000000000" + "\n")