import copy

lst = [1, 2, 3, 4]

new_list = copy.deepcopy(lst)

print(lst is new_list)

new_list[0] = 2

print(lst)
print(new_list)
