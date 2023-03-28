instructorlist = input().split(" ")
instructorlist = [instructor for instructor in instructorlist if instructor != "none"]
if len(instructorlist) == 0:
    print("TBD")
elif len(instructorlist) == 2:
    print(f"{instructorlist[0][0]}. {instructorlist[1]}")
else:
    print(f"{instructorlist[1]} / {instructorlist[3]} / ...")