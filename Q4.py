dict1 = {
    "ali" : 10, "john": 19, "mohammed" : 10, "zahraa": 19, "george" : 16, "nabiha": 13
}

dict2 = {}

for key, value in dict1.items():
    if value in dict2:
        dict2[value].append(key)
    else:
        dict2[value] = [key]


print(dict2)