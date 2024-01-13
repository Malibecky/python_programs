# create a list
customer_list = []
# create a loop
while True:
    enter_customer = input("enter customer(Yes/No): ").lower()

    if enter_customer == "no":
        break
    elif enter_customer == "yes":
        fname, lname = input("enter customer name: ").split()
        customer_list.append({"fname": fname, "lname": lname})

for cust in customer_list:
    print(cust["fname"], cust["lname"])
