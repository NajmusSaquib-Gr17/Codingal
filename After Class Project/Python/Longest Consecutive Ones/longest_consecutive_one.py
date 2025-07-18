def longest_consecutive_ones(n):
    
    binary = bin(n)[2:]    
    
    ones_groups = binary.split('0')
    max_ones = max(len(group) for group in ones_groups)    
    return max_ones


num = int(input("Enter a number: "))

print("Longest consecutive 1:", longest_consecutive_ones(num))
