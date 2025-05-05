


x = open("code.txt")


opcodes = ["LOAD", "STORE", "ADD"]
opcodes_bit = ["0001", "0010", "0011"]
registers = ["r1,", "r2,"]
registers_bit = ["0001", "0010"]




count = 0
with open("program.bin", "wb") as f:
    for line in x:
        instruction = ""
        line = line.strip()
        
        if line:
            line = line.split(" ")
            #print(line)
            #print the split line with spaces for debug
            
            
            #last 4 bits opcode
            if line[0] in opcodes:
                instruction += opcodes_bit[opcodes.index(line[0])]
            
            else:
                print("error0")
            
            
            
            #11-8 bits are register a or b    
            if line[1] in registers:
                instruction += registers_bit[registers.index(line[1])]
            else:
                print("error1")
            
            
            
            # 7-0 are the value or address
            if line[2][0] == "[":
                val = int(line[2].strip("[]"))
            else:
                val = int(line[2])
            
            if ((val > 255) or (val < 0)):
                print("error2")
                
            binary = format(val, '08b')
            instruction += binary
            print(count, instruction)
            count += 1
            instruction = int(instruction, 2) #converts the string of 0's and 1's to the integer equivalent of the binary value.
            f.write(instruction.to_bytes(2, byteorder='big'))
                
            
        
        



