import copy

lst = [1, [2, 1], 3, 4]

new_list = copy.copy(lst)

print(lst is new_list)

new_list[1][0] = 2

print(lst)
print(new_list)
