my_dict = {"name": "Patrika", "age": 21}


print(my_dict["name"])           # Patrika
print(my_dict.get("age"))        # 21


my_dict["college"] = "BPPIMT"
my_dict["age"] = 22


my_dict.pop("college")           # Remove by key
# my_dict.popitem()              # Remove last inserted item

# Keys, Values, Items
print(my_dict.keys())            # dict_keys(['name', 'age'])
print(my_dict.values())          # dict_values(['Patrika', 22])
print(my_dict.items())           # dict_items([('name', 'Patrika'), ('age', 22)])


print("name" in my_dict)         # True


for key, value in my_dict.items():
    print(key, "->", value)


my_dict.clear()
