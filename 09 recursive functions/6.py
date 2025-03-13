# A list contains some negative and some positive values. Write a recursive function 
# that sanitizes the list by replacing all negative numbers with 0

def sanitize_list(lst):
    if not lst:
        return []
    elif lst[0] < 0:
        return [0] + sanitize_list(lst[1:])
    else:
        return [lst[0]] + sanitize_list(lst[1:])
    
print(sanitize_list([9,99,-8,-6]))