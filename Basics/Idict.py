idict = {"eddie": 345154,
         "harvey": 13123123}
try:
    item = idict["lennie"]
except KeyError:
    idict["lennie"] = set()
else:
    raise Exception("already exits")

print(idict)