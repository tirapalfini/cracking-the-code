# 1.2
# Implement an algorithm to determine if a string has all unique characters. 

def is_unique(string):
    
    count = {}

    for letter in string:
        if letter in count:
            return False
        else:
            count[letter] = 1
    return True

print(is_unique("hello")) #should output False
print(is_unique("world")) #should output True
