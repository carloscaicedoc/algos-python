# SQUARES OF A SORTED ARRAY
# Given an integer array nums sorted in non-decreasing order, 
# return an array of the squares of each number sorted in non-decreasing order.

sorted1 = [-4,-1,0,3,10];
expected1 = [0,1,9,16,100];

sorted2 = [-7,-3,2,3,11];
expected2 = [4,9,9,49,121];

def sorted_squares(nums):
    squares = []

    for num in nums:
        squares.append(num * num)

    return sorted(squares)

print(sorted_squares(sorted1))
print(sorted_squares(sorted2))

# Alternative Solution - Short
def sorted_squares2(nums):
    return (sorted(x*x for x in nums))

print(sorted_squares2(sorted1))
print(sorted_squares2(sorted2))
