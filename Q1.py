dict_1= {
    "a" : 1, "b" : 2, "c" : 3, "d" : 4, "e": 5, "g" : 32
}

dict_2= {
    "a" : 5, "b" : 4, "c" : 3,"d" : 2, "e": 1, "h" : 12
}

# using the star operator the two dictionaries will merge and dict_2 will override dict_1
new_dict = {**dict_1, **dict_2}

print(new_dict)

