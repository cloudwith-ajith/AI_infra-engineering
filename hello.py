
# this is my first code 

# print is a function,you may ask what is function is - function is a tested code which is already stored for future uses 
'''print("hello world")'''

# input - is a function which is used to get input fromm the user 
'''input("what your name ?")
print("hello"+input)'''

# using variables- its a container which is used to stored the user data in memory and used for the future used 
'''name = input("what is your full name ? ")
print("hi"+ name ) '''

# here we used(,)instead od + to mention there are two argument because in python notes more then one argument space will automatically proved 
'''n=input("wht is yout name??")
print("hi",n)'''

#new way to print without +, use f{} - this could the python something happening here
'''n = input()
print (f"hello,{n}")'''

#this could happen when user used to print the many space button that not looks good.so we use the function called-
# strip(what actually do ,remove the white space)  
''' problem python hello.py
        ajith
hello,        ajith'''

'''n = input("what your name? ")
n = n.strip()
print(f"hello,{n}")'''

'''output
what your name?             ajith
hello,ajith'''

# capitalize( used to captialize the first letter) and tittle(which is used to do the tittle words)

'''name = input("what is your name? ").strip().title()
print(f"hi,{name}")
(or)
name =input("what is name? ")
name=name.strip()
name=name.title()
print(f"hello,{name}"'''

# split(which is used to split the name and print ) 
# below code just explain the variables hold the first and last name and split into two 
"""
name = input("what is your name? ").strip()
first,last=name.split()
print(f"hi{last}")"""

#def
"""
def ajith():
    return("hi")

print(ajith())"""

def main():
    n = input("what is your name ? ")
    hello(n)

def hello(to):
    print("hello, ",to)

main()
    