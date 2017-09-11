# 1.4 Palindrome Permutations
# Given a string, write a function to check if it is a permutation of a palindrome.  
# A palindrome is a word or phrase that is the same forwards and backward.  
# A permutation is a rearrangement of letters.  The palindrome does not need to be limited to just
# dictionary words. EXAMPLE Input: "Tact Coa" Output: True (Permutations: "taco cat", atco cta")

def check_palindrome(string):
    
    #remove spaces and make all letters lowercase
    string = string.replace(" ", "").lower()

    dict = {} 
    oddLetters = 0 

    #determine frequency of the letters by adding them to a dictionary
    for letter in string:
        if letter in dict:
            dict[letter] += 1
        else:
            dict[letter] = 1

    #iterate through dictionary to determine how many letters have odd frequencies
    for key, value in dict.items():
        if not value % 2 == 0:
            oddLetters += 1

    # a palindrome will only have 1 odd frequency, so it will only be true if that condition is met
    if oddLetters == 1:
        return True

    return False

print(check_palindrome("Tact Coa"))

