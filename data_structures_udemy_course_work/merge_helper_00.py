# merge is a helper function, takes 2 sorted lists and combines them into a new sorted list
# we will set i to first index of list_1 and j to first of list_2, since they are sorted adding the lower value
# of the current i or j will add the next lowest value
# once one list is empty add the rest of the remaining list

list_i = [2,5,7,8,22]
list_j = [3,75,77,88,99]

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

print(merge(list_i, list_j))