# will be a helper function in quick sort
# how pivot works
# takes 1st index, makes everything smaller next and then everything bigger after that, then swaps first index with
# the index that will properly sort that one item
# example 4,2,3,7,6 -> 2,3,4,7,6
# base case is when will the recursion be satisfied? i.e if left > right or int_1 > int_2 etc
def swap(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp


def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index

    for i in range(pivot_index + 1, end_index + 1):
        # we go +1 so that it goes upto and including last index
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index)
    return swap_index


def quick_sort_helper(my_list, left, right):
    if left < right:
        pivot_index = pivot(my_list, left, right)
        quick_sort_helper(my_list, left, pivot_index - 1)
        quick_sort_helper(my_list, pivot_index + 1, right)
    return my_list

def quick_sort(my_list):
    print(my_list)
    return quick_sort_helper(my_list, 0, len(my_list) - 1)
my_list = [4, 6, 1, 7, 3, 2, 5, 24, 55]

print(quick_sort(my_list))
