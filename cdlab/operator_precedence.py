import re
def isOperatorPrecedence(production):
    characters_in_production = production.split()
    for i in range(2,len(characters_in_production)-1):
        if(characters_in_production[i]=="epsilon"):
            return 0
        else:
            nonterminals = re.compile('[A-Z]')
            if(nonterminals.match(characters_in_production[i]) and nonterminals.match(characters_in_production[i+1])):
                return 0
    return 1
            
production = input("Enter Production write each character with a space: ")
flag=isOperatorPrecedence(production)

if flag == 1:
    print("The grammar is operator precedence.")
else:
    print("The grammar is not operator grammar.")