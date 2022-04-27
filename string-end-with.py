# STRING ENDS WITH 

# Complete the solution so that it returns true if the first argument(string) 
# passed in ends with the 2nd argument (also a string).

def stringEndsWith(string, ending):
    return string.endswith(ending)

# Test cases:
print(stringEndsWith('Tacoma', 'oma'))
print(stringEndsWith('Argument', 'ment'))
print(stringEndsWith('Balance', 'once'))
print(stringEndsWith('Chicago', 'ego'))

