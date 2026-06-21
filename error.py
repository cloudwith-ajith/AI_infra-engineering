# into to try,except,else with error like name error ,value error
"""
def main():
    num=get_num()
    print(num)

def get_num():

    while True:
        try:
            x = int(input("enter the vale of x? ")) 
            return x
        
        except ValueError:
            print("please enter the interger")
"""        
 

def main():
    num=get_num("what is x? ")
    print(f"x is {num}")

def get_num(prompt):

    while True:
        try:
             return int(input(prompt)) 
            
        
        except ValueError:
            print("please enter the interger")
        
        """ else:
            break"""




main()
