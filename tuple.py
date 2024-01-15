myTuple = (1, 2, 3, 4, 5, 6, )
print("tuple length: ", len(myTuple))
morefibs = myTuple + (20, 30)

print("20 in tuple: ", 20 in morefibs)

for i in morefibs:
    print(i)


print("min: ", min(morefibs))
print("max: ", max(morefibs))