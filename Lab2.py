list1 = []
list1Size = int(input("enter the lenth of list"))
for i in range(list1Size):
    num = int(input("enter the number you want to enter "))
    list1.append(num)

list2 = []
list2Size = int(input("enter the size of second list"))
for i in range(list2Size):
    num = int(input("enter the number you want to enter "))
    list2.append(num)
totalList = list1+list2
print(totalList)
sortedList = totalList.sort()
print(max(totalList))
print(min(totalList))