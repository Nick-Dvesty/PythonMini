
def addition(firstList: list, secondList: list) -> list:
    minLenth = min(len(firstList), len(secondList))
    ansList = []
    for i in range(minLenth):
        ansList.append((firstList[i], secondList[i]))
        print(ansList)
    return ansList



list1 = ["1","2","4"]
list2 = [1,2,3,4]
addition(list1, list2)