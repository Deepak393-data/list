'''
Write a program to count the number of times the given value is repeated.
Input Format:
First line of input consists of our list elements.
Second line of input consists of value to count.
Output Format:
Print thr number of times the given value is repeated in the list.
Sample Input:
10 20 10 40 10
10
Sample Output:
3
'''
# Input the list elements
elements = list(map(int, input().split()))

# Input the value to count
value_to_count = int(input())

# Count the occurrences of the value in the list
count = elements.count(value_to_count)

# Output the count
print(count)
