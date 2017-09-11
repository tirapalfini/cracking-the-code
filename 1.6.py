# 1.6 String Compression
# Implement a method to perform basic string compression using the counts of repeated characters. 
# For example, the string 'aabcccccaaa' would become 'a2b1c5a3'.  If the "compressed" string
# would not become smaller than the original string, your method should return the original
# string.  You can assume the string has only uppercase and lowercase letters (a-z). 

# This solution will treat lowercase and uppercase letters as different characters
# as the problem did not specify

def string_compression(string):
    
    modify = ""
    modify += (string[0])
    
    counter = k = 1

    while k < len(string):
    	if string[k] == string[k-1]:
    		counter += 1
        else:
        	modify += str(counter)
        	counter = 1
        	modify += (string[k])
        k += 1
    
    modify += str(counter)

    if len(modify) == 2*len(string):
    	return string

    return modify

print(string_compression("aabcccccaaa"))


