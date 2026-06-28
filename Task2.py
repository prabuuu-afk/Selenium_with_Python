# 1. Sum all items in a list
def sum_list(lst):
    return sum(lst)
l=[1,2,3,4,5]
print(sum_list(l))

# 2. Largest number
def max_list(lst):
    return max(lst)
l=[1,2,3,4,5]
print(max_list(l))
# 3. Smallest number
def min_list(lst):
    return min(lst)
l=[1,2,3,4,5]
print(min_list(l))

# 4. Remove duplicates
def remove_duplicates(lst):
    return list(set(lst))
l=[1,2,3,4,5,1,3,5,6]
print(remove_duplicates(l))

# 5. Clone or copy a list
def clone_list(lst):
    return lst.copy()
l=[1,2,3,4,5]
print(clone_list(l))

# 6. Reverse a list
def reverse_list(lst):
    return lst[::-1]
l=[1,2,3,4,5]
print(reverse_list(l))

# 7. Create list with random data types
l=[1, "hello", 3.14, True, [5,6], {"a":1}]

# 8. Remove empty element
def remove_empty(lst):
    return [x for x in lst if x != ""]

# 9. Append second list to first
def append_lists(lst1, lst2):
    lst1.extend(lst2)
    return lst1
l1=[1,2,3,4,5]
l2=[4,5,6,7,8]
print(append_lists(l1,l2))

# 10. Choose random item
import random
def random_item(lst):
    return random.choice(lst)
l=[0,23,56,55342,64543,33,1]
print(random_item(l))
# 11. Separate odd and even
def separate_odd_even(lst):
    odd = [x for x in lst if x % 2 != 0]
    even = [x for x in lst if x % 2 == 0]
    return odd, even
l=[0,1,2,3,4,5,6,7,8,9,10]
print(separate_odd_even(l))

# 12. Sort ascending
def sort_list(lst):
    return sorted(lst)
