import json


def JsonParser(file):
    pdata = dict()
    with open(file, mode="r", encoding="utf-8") as inf:
        pdata = json.load(inf)
    return pdata


def test():
    test_data = JsonParser("jsonData.json")
    pdit = {}
    for pd in test_data:
        print(pd["batters"]["batter"])
        for item in pd["batters"]["batter"]:
            print(item["id"])

if __name__ == '__main__':
    test()
