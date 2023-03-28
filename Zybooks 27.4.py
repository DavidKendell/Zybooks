passengerAge = int(input())
carryOns = int(input())
checkedBags = int(input())

airFair = 0
if passengerAge >= 60:
    airFair = 290
elif passengerAge > 2:
    airFair = 300

airFair += max(checkedBags-2, 0) * 50
if checkedBags > 1:
    airFair += 25
airFair += carryOns * 10
print(airFair)