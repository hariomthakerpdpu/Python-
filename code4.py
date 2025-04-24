#4)	Write a function that removes one string from another string,
#  if present. E.g. Onestring = “abcdef”, removestring = “cd”. 
# The finalstring should contain “abef”.

def removestring(s1,s2):
    m,n=len(s1),len(s2)

    for i in range(m-n+1):
        match =True

        for j in range(n):
            if s1[i+j] != s2[j]:
                match =False
                break

        if(match): #if match is found remove substring
            return s1[:i]+s1[i+n:]     #reconstruct new string
    
    return s1 #IF NOT FOUND RETURN ORIGINAL

s1=input("enter ths main string:")
s2=input("enter the string to remove:")

print("final string:",removestring(s1,s2))