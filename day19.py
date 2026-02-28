# dictionarory few function and for loop
dict={
    "name":["saha","sabuj"],
    18:[18,19],
    "vill":["utter sherpur""jadurhati"]
}
print(dict["name"])
print(dict.values())
for key in dict.keys():
    print(f"{(key)} : {dict[key]}")
print(dict.keys())
print(dict.items())
for key,velu in dict.items():
    print(key , velu)
print(dict["name"][1])
dict.popitem()
print(dict)
