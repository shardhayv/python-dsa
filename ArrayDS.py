# PROPERTIES

# Array can store data of similar type
# Elements in array are located in a contiguous
# Each element of an array has a unique index
# The size of an array is predefined and cannot be modified

# TYPES

# 1)One Dimensional
# e.g a=[1,4,3,7,5]
# indexing-- a[n]

# 2)Multi-dimensional(i.e 2d,3d,4d.........nd)
#           0 1 2 3 4
# e.g  a= 0[[2,4,5,7,3],
#         1[4,5,2,6,7]]

# to access 6 we need to write a[1,3]


from array import *

a = array('i', [1, 2, 3, 4, 5])


# INSERTING ELEMENT IN AN ARRAY

# a.insert(2,9)
#
# print(a)

# ARRAY TRAVERSAL

# def traverse_array(array):
#     for i in array:
#         print(i)
#
#
# traverse_array(a)

# ACCESSING AN ELEMENT OF AN ARRAY
# TIME COMPLEXITY ==> O(1)

# def element_index(array, index):
#     if index > len(array):
#         print("There is no element at this index")
#     else:
#         print(array[index])
#
#
# element_index(a, 3)

# SEARCHING FOR AN ELEMENT IN AN ARRAY


def searching(array, value):
    for i in array:
        if i == value:
            return a.index(value)
    return "The element doesn't exist in the array"


print(searching(a, 2))
