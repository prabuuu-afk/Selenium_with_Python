#Reverse the given tuple
def reverse_tuple(tpl):
    return tpl[::-1]

t = (10,20,30,40)
print("Reversed tuple:", reverse_tuple(t))

#Access value 20 from tuple
def access_20(tpl):
    return tpl[tpl.index(20)]

t = (10,20,30,40)
print("Access 20:", access_20(t))

#Copy specific elements from tuple
def copy_elements(tpl, indices):
    return tuple(tpl[i] for i in indices)

t = (10,20,30,40)
print("Copied elements:", copy_elements(t,[1,3]))

#Check if all items in tuple are same
def all_same(tpl):
    return all(x == tpl[0] for x in tpl)

t = (5,5,5)
print("All same:", all_same(t))

#Create a tuple with single item 50
def single_tuple():
    return (50,)

print("Single tuple:", single_tuple())

#Swap two tuples
def swap_tuples(t1, t2):
    return t2, t1

print("Swapped:", swap_tuples((1,2),(3,4)))

#Unpack tuple into 4 variables
def unpack_tuple(tpl):
    a, b, c, d = tpl
    return a, b, c, d

t = (10,20,30,40)
print("Unpacked:", unpack_tuple(t))