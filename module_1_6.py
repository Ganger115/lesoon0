#Работа со словарями:
my_dict = {"Alex": 1999, "Anastfsia": 1997, "Alevtina": 1998}
print("Dict:", my_dict)
print("Existing value:", my_dict["Alex"])
my_dict.update({"Mom": 1975,
                "Dad": 1970})
F = my_dict.pop("Mom")
print("Not existing value:", my_dict.get("Mom"))
print("Deleted value:", F)
print("Modified dictionary:", my_dict)

#Работа с множествами:
my_set = {1, 2, 2.145, 3, 3, 'Hunt', 'Hunt', 2.145, True, 1, True, 2}
print("Set:", my_set)
my_set.add(5.544)
my_set.add((1, 2, 4))
my_set.remove(2.145)
print("Modified set", my_set)