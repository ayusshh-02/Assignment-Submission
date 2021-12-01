global address_list, label_list, relocation_list
address_list = []
label_list = []
relocation_list = []

# function to display the table.
def display_Table(label_list, address_list, relocation_list):
    print("-----------Symbol table------------")
    print("{0:10s} | {1:<7} | {2:<4}".format(
        "labels", "address", "Relocation"))
    for i in range(len(address_list)):
        print("{0:10s} | {1:<7} | {2:<4}".format(
            label_list[i], address_list[i], relocation_list[i]))


def symbolTable(input_file):
    global address_list, label_list, relocation_list
    four_bytes = ['LA', 'L', 'A', 'ST', 'C']
    two_bytes = ['SR', 'AR', 'BNE', 'LR', 'BR']
    declare = ['DS', 'DC']
    zero_bytes = ['USING']
    file = open(input_file, 'r')
    line = file.readline()
    while(line):
        relocation = 'R'
        words = line.split()
        if(words[0] == 'NULL'):
            if(words[1] == 'START'):
                address = int(words[2])
            if(words[1] in four_bytes):
                address += 4
            elif (words[1] in two_bytes):
                address += 2

        else:
            label_list.append(words[0])
            if(words[1] == 'START'):
                address = int(words[2])
                address_list.append(address)
            elif(words[1] in four_bytes):
                address_list.append(address)
                address += 4
            elif(words[1] in two_bytes):
                address_list.append(address)
                address += 2
            elif(words[1] in declare):
                i = 0
                while True:
                    if(words[2][i] == 'F' or words[2][i] == 'H'):
                        break
                    i += 1
                if(words[1] == 'DS'):
                    address_list.append(address)
                    no_of_words = int(words[2][:i])
                    if(words[2][i] == 'F'):
                        address += no_of_words*4
                    else:
                        address += no_of_words * 2
                else:
                    address_list.append(address)
                    if(words[2][i] == 'F'):
                        address += 4
                    else:
                        address += 2
            elif(words[1] == 'EQU'):
                value = words[2]
                relocation = 'A'
                address_list.append(value)
            relocation_list.append(relocation)
        line = file.readline()

#Function calls.

symbolTable('assembly.txt')
display_Table(label_list, address_list, relocation_list)
