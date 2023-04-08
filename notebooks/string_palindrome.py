#!/usr/bin/python3
import math

def MinPalindromeIns(s: str, i: int, j: int, mem_table: list[list]):
    
    if i > j: # incase the pointers cross over resulting in substring size less than 0
        return math.inf
    if i == j: # string of len 1 is a palindrome
        return 0
    if i == j-1:
        if s[i] != s[j]: 
            mem_table[i][j] = 1
        return mem_table[i][j]
    
    if s[i] == s[j]: # first and last element is the same
        mem_table[i][j] = MinPalindromeIns(s, i+1, j-1, mem_table)
    else:
        mem_table[i][j] = 1 + min(MinPalindromeIns(s, i+1, j, mem_table), MinPalindromeIns(s, i, j-1, mem_table))
    
    return mem_table[i][j]

def iterative_approach(s:str, mem_table: list[list]):
    l, h, gap = 0, 0, 0
 
    # Fill the table
    for gap in range(1, len(s)):
        l = 0
        for h in range(gap, len(s)):
            if s[l] == s[h]:
                mem_table[l][h] = mem_table[l + 1][h - 1]
            else:
                mem_table[l][h] = (min(mem_table[l][h - 1],
                                   mem_table[l + 1][h]) + 1)
            l += 1
    return mem_table

def get_palindrome(s: str, mem_table: list[list]):
    n = len(s) 
    i, j = 0, n-1
    result = list(s)
    append_list = []
    prepend_list = []
    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        elif mem_table[i][j-1] <= mem_table[i+1][j]: # s[j] to be inserted to the beginning of the sub-string
            prepend_list.append((i, s[j]))
            j -= 1
        else: # s[i] to be inserted to end of the sub-string
            append_list.append((j+1, s[i]))
            i += 1
    for ind, char in append_list:
        result.insert(ind, char)
    for ind, char in reversed(prepend_list):
        result.insert(ind, char)

    return "".join(result)

def main():
    # s = "STAIR"
    s = "BEAKER"
    s = "BARBARIAN"
    # s = "abc"
    # s = "hello"
    n = len(s)
    mem_table = [[0 for _ in range(n)] for _ in range(n)]
    print("Recursive approach: ")
    MinPalindromeIns(s, 0, n-1, mem_table)
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in mem_table]))
    
    # print("Iterative approach")
    # mem_table = iterative_approach(s, mem_table)
    # print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in mem_table]))
    

    print(f"The palindrome string is: {get_palindrome(s, mem_table)}")

if __name__ == "__main__":
    main()


# To determine the actual palindrome string, you can use the memo table to backtrack from the end of the string to the beginning. 
# Start with the last character of the string and check if it is part of a palindrome. 
# If it is not, then insert the appropriate character(s) to make it a palindrome. 
# Repeat this process for the previous character(s) until you reach the beginning of the string.

# As you insert characters to form the palindrome, keep track of them in a separate string.
# Once you have processed the entire input string, the resulting string will be the palindrome with the minimum number of insertions.