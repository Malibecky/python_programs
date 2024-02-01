try:

    alist = [1, 2, 3]

    print(alist[3])

except IndexError:
    print("sorry the index doesn't exist")

except:
    print("An unknown error occurred")
    