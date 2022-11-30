# Реализуйте алгоритм перемешивания списка.
import random

lst = ["klj", "8jkh7", 1, "khf", "98sd,f"]

random.shuffle(lst)
print(lst)

# for i in range(len(lst)):
#     index_new = random.randrange(0,len(lst))
#     temp = lst[i]
#     lst[i] = lst[index_new]
#     lst[index_new] = temp
# print(lst)
