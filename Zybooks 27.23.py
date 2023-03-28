customerDbdottxt = "42 Mike Jones 16 Al Garcia 27 Sarah Lee 12 Stan Lee 99 Amy Hernandez"
custId = input()
found = False
first = False
custlist = customerDbdottxt.split(" ")
for i in range(0, len(custlist), 3):
    if custlist[i] == custId:
        print(f"{custlist[i+1]} {custlist[i+2]}")
        break
else:
    print("Not found")