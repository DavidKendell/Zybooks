runwayDeg = 10 * int(input())
runwayDeg = runwayDeg % 360
angledifferences = [abs(i - runwayDeg) for i in range(0, 360, 45)]
angles = ("north", "northeast", "east", "southeast", "south", "southwest", "west", "northwest")
print(f"{runwayDeg} degrees ({angles[angledifferences.index(min(angledifferences))]})")