test = {
    "a" : ["123"],
    "b" : ["234"],
    "c" : "456",
    "d" : "567"
}

print(test.values())

test["a"] = "[aaa]"

print(test["a"])
#print(test.values())

#test["a"] += ["ccc"]

#print(test.values())
