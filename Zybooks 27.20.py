oneletter = False
onenum = False
onespecial = False
specialchars = "!#%"
password = input()
for char in password:
    onenum = onenum or char.isdigit()
    onespecial = onespecial or char in specialchars
    
if len(password) < 8:
    print("Too short")
if not onenum:
    print("Missing number")
if not onespecial:
    print("Missing special")