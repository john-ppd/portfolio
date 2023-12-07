# this is as good as it gets to sort multiple types of data, there are better ones for numbers only
# Big O time complex is O(n log n)
# space is On

list_i = [2, 5, 7, 8, 22]
list_j = [3, 75, 77, 88, 99]


def merge(list1, list2):
    combined = []
    i = 0
    j = 0
    # while both lists still have index variables
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1

    while i < len(list1):
        combined.append(list1[i])
        i += 1
    while j < len(list2):
        combined.append(list2[j])
        j += 1
    return combined


def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list
    mid_index = int(len(my_list) / 2)
    # this takes the left half of indexes starting at index 0 and goes up to but not including
    left = merge_sort(my_list[:mid_index])
    # this takes the right half of the indexes starting at mid_index and going up until the last index
    right = merge_sort(my_list[mid_index:])

    return merge(left, right)

og_list = [3,1,4,2]
sorted_list = merge_sort(og_list)
print('og list', og_list)
print('sorted', sorted_list)
