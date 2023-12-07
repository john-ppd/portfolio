# bubble sort checks if current index is > than next index, if so they switch, now go to next index until end
def bubble_sort(my_list):
    # start at length -1 and next run will be len -2 until the list is done
    for i in range(len(my_list) - 1, 0, -1):
        # go through length -1 all the way through and sort
        for j in range(i):
            # check if current index is > than next index
            if my_list[j] > my_list[j + 1]:
                # create temp for current index
                temp = my_list[j]
                # swap to the next index since its bigger
                my_list[j] = my_list[j + 1]
                # swap next index for temp
                my_list[j + 1] = temp
    # return the list
    return my_list


list_to_sort = [27, 5, 6, 2, 6, 2, 1, 44, 55, 63, 53]

print(bubble_sort(list_to_sort))
