import random
import math

# 1. an outer loop decreases in size each time
# 2. The goal is to have the largest number at the end of the list when the outer loop completes one cycle
# 3. The inner loop starts comparing indexes at the beginning of the loop
# 4. check if list[j] > list[j + 1]
# 5. If so swap the index values
# 6. When the inner loop completes the largest number is at the end of the list
# 7. Decrement the outer loop by 1

list1 = []
for i in range(4):
    list1.append(random.randrange(1, 10))

i = len(list1) - 1

while i > 1:

    j = 0

    while j < i:

        print("\nIs {} > {}".format(list1[j], list1[j + 1]))

        if list1[j] > list1[j + 1]:
            print("switch")
            temp = list1[j]
            list1[j] = list1[j + 1]
            list1[j + 1] = temp
        else:
            print("Don't switch")

        j += 1

        for k in list1:
            print(k, end=", ")
        print()

    print("END OF ROUND")

    i -= 1

for k in list1:
    print(k, end=", ")
print()
