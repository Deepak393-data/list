'''
Write a Python Program to find the largest number in a list
Input & Output Format:
Input consists of one list and one integer.
First input consists of a size of a list.
Second inputs corresponds to the size of the list.
Output consists of the largest element.
Sample Input:
5
1
2
3
6
5
Sample Output:
6
'''
# Input the size of the list
n = int(input())

# Initialize an empty list
my_list = []

# Input the elements of the list
for _ in range(n):
    element = int(input())
    my_list.append(element)

# Find the largest element in the list
largest = max(my_list)

# Output the largest element
print(largest)
