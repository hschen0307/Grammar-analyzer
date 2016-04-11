__author__ = 'Hsuan-Chih, Chen'

import json

class grammar:


    grammar = {}

    def __init__(self, file_name):
        
        self.grammar = json.load(open(file_name))
        
        


    def parser(self,input_string):
        stack = []
        string_list = []
        for ch in input_string:
            string_list.append(ch)
        stack.append("S")
        
        while(string_list):
            if not stack:
                return False
            
            element = stack.pop()
            if(element in self.grammar):
                temp = self.find(self.grammar[element], string_list)
                if(temp == -1):
                    return False
                else:
                    for ch in reversed(temp):
                        stack.append(ch)
            else:
                if(element == string_list[0]):
                    del string_list[0]
                else:
                    return False

        if not stack:
            return True
        else:
            return False

    def find(self,rules, string_list):
        for i in rules:
            if(i[0] == string_list[0]):
                return i

        return -1

    

if __name__ == "__main__":
    print ("file name")
    print ("1.  {a^n#b^n | n > 0}")
    print ("2.  {w#w^R | w is element of {0,1}*}")
    print ("3.  {a^i#b^j#c^k# | i = j and i,j,k > 0}")
    print ("4.  {1^i#0^j | i*2 = j and i, j > 0}")    
    filename = input("which file do you want to open?: ")+".json"
    
    grammar_object = grammar(filename)

    control = 0
    while(control == 0):
        input_string = input("Please type in a string: ")
        print(input_string)
        if(grammar_object.parser(input_string)== True):
            print("ACCEPT")
            print("\nThe string in the grammar.")        
        else:
            print("REJECT")
            print("\nThe string is not in the grammar")
        choice = input("continue (Y/N): ")
        if(choice == 'Y'):
            control = 0
        else:
            control = 1
        

    
