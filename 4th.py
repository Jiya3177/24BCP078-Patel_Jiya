#Write a function that removes one string from another string, if present. 
# E.g. Onestring = “abcdef”, removestring = “cd”. The finalstring should contain “abef"

def remove_substring(main_string, remove_string):
    if remove_string in main_string:
        return main_string.replace(remove_string, "")
    else:
        return main_string

onestring = input("Enter the main string: ")
removestring = input("Enter the string to remove: ")

finalstring = remove_substring(onestring, removestring)

print("The final string after removal is:", finalstring)
