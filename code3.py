#3)	Accept two strings. 
# Check whether one string is there in another string.

def check_strs(s1,s2):
    m,n=len(s1),len(s2)

    for i in range(m-n+1): #size of( mainstring - substring) to check bloack of substring in main string
                            #and +1 to manage range function 
        match=True

        for j in range(n): #runs for the size of substring 
            if s1[i+j] != s2[j]: #check each element of main string (starting from the outer loop iteration)with the substring
                match=False
            break

        if(match):
            return True
    
    return False

s1=input("Enter the main string:")
s2=input("Enter the string to search:")

if (check_strs):
    print("yes the string is present in the first string")
else:
    print("no the string is not present in the ain string")    
