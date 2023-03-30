def SimulateLine(customerArrivals: list[int]) -> None:
    linelength = 0
    for customer in customerArrivals:
        linelength = max(0, linelength-1) + customer
        print(linelength, end=" ")
    print()

customerArrivals = [int(input()) for i in range(10)]
SimulateLine(customerArrivals)