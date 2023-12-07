# insertion sort starts at the 2nd index and checks if its smaller than the left, if smaller it swaps
# then moves to next index, if smaller than the left index it'll check the left of that until its not smaller
import random


def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i - 1
        while temp < my_list[j] and j > -1:
            my_list[j + 1] = my_list[j]
            my_list[j] = temp
            j -= 1
    return my_list


list_3 = [43, 2, 5, 646, 7, 2, 1, 0, 89]

# print(insertion_sort(list_3))
listy = []
for i in range(0,101):
    listy.append(random.randint(0,1001))
print()
print(listy)
print()
print(insertion_sort(listy))
