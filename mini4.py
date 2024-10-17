
def invert(district: dict) -> dict:
    ansDict = {}
    for key in district:
        if district[key] in ansDict:
            print(type(ansDict[district[key]]))
            if type(ansDict[district[key]]) == tuple:
                ansDict[district[key]] = ansDict[district[key]] + (key,)
            else:
                ansDict[district[key]] = (ansDict[district[key]], key)
        else:
            ansDict[district[key]] = key
    return ansDict


a = {12:"121", 13:"121", 1:"1213", 14:"121", 63:"1221"}
invert(a)
