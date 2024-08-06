print("Работа со словарями".upper())
my_dict = {"Alexandr": 1996, "Konstantin": 1999, "Yuri": 2003}
print("Dict:", my_dict)
print("Existing value:", my_dict["Alexandr"])
print("Not existing value:", my_dict.get("Vladislav"))
my_dict.update({"Alina": 1998,
                "Anna": 1975})
print("Dict:", my_dict)

a = my_dict.pop("Konstantin")
print("Deleted value:", a)
print("Dict:", my_dict)
#
print("Работа с множествами:".upper())
my_set = {1, 9, 9, 6, True, (1, 3, 3, 7), 0, False, "Alexandr"}
print("Set:", my_set)
print(my_set.add(2024))
print(my_set.add("Yuri"))
print("Modified set:", my_set)
print(my_set.discard((1, 3, 3, 7)))
print("Modified set:", my_set)