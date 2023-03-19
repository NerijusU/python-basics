# Dictionaries: Key-Value pairs, unordered, mutable #

# my_dict = {"name": "Max", "age": 28, "isMale": True}
# my_dict2 = dict(name="Marry", age=27, isMale=False)
#
# # my_dict["email"] = "max@max.com" # add new element
# # print(my_dict) # {'name': 'Max', 'age': 28, 'isMale': True, 'email': 'max@max.com'}
#
# # del my_dict["isMale"] # delete element
# # print(4, my_dict) # {'name': 'Max', 'age': 28}
#
# # my_dict2.pop("age") # delete element
# # print(5, my_dict2) # {'name': 'Marry', 'isMale': False}
#
# # my_dict2.popitem() # delete last element
# # print(6, my_dict2) # {'name': 'Marry', 'age': 27}
#
# # try:
# #     print(7, my_dict["name"])
# # except:
# #     print(7, "Error")
#
# # for key in my_dict.keys():
# #     print(8, key)
# #
# # for value in my_dict.values():
# #     print(9, value)
# #
# # for key, value in my_dict.items():
# #     print(10, key, value)
#
# my_dict.update(my_dict2)
# print(11, my_dict)

# mytuple = (8, 7)
# mydict = {mytuple: 15}
# print(mydict) # {(8, 7): 15}