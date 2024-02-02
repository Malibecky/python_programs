try:
    myFile = open("mydata2.txt", encoding="utf-8")

except FileNotFoundError as ex:
    print("That file was not found")
    print(ex.args)

else:
    print("file :", myFile.read())
    myFile.close()

finally:
    print("finished working with the file")