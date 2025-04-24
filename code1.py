#1)	Count how many vowels are 
# there in a string. Accept the string from the user



# def count_vowels(string):

#     string=string.upper()
#     vowel=string.count('A')+string.count('E')+string.count('I')+string.count('O')+string.count('U')

#     return vowel

            #2nd method

def count_vowels(string):
    string = string.lower()
    vowels="aeiou"
    vowel_count=0

    for i in string:
        if i in vowels:
            vowel_count += 1

    return vowel_count        



input_string= input("Enter a string:")
vowels= count_vowels(input_string)
print(vowels)