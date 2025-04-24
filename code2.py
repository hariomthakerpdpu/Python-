#Write your own functions (without using built-in functions) to convert all
#  characters of a string into lower case/upper case/toggle case.


def toggle_case(string):
    newstr='' #because string is immutable so we need to change the letter and input them in new string
    for i in string:
        if (i >= 'A' and i <='Z'):
            i = chr(ord(i) + 32)
        elif(i >='a' and i <='z'):
            i = chr(ord(i)-32)
        newstr+=i  #to make the string in reverse we can     newstr = c + newstr #example of operator overloading   
    return newstr        

def lower_case(s):
    newstr=''
    for i in s:
        if 'A'<= i <= 'Z':
            i=chr(ord(i)+32)
        newstr+=i  
    return newstr           

def upper_case(s):
    newstr=''
    for i in s:
        if 'a'<= i <='z':
            i=chr(ord(i)-32)
        newstr+=i    
    return newstr    


input_string=input("enter the string:")

print("original:",input_string)
print("Lowercase:",lower_case(input_string))
print("Uppercase",upper_case(input_string))
print("Toggle case:",toggle_case(input_string))