rocketHeight = 0
initialVelocity = int(input())
timeSinceLaunch = 0
while rocketHeight >= 0:
    print(f"{timeSinceLaunch} {rocketHeight}")
    timeSinceLaunch += 1
    rocketHeight = initialVelocity * timeSinceLaunch - 5 * timeSinceLaunch ** 2