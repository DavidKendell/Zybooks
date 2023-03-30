def CostForMilesGas(miles: int) -> int:
    MILES_PER_GAL = 30
    CENTS_PER_GAL = 400
    return miles * CENTS_PER_GAL // MILES_PER_GAL
def CostForMilesMaintenance(miles: int) -> int:
    TIRES_CENTS = 50000
    TIRES_MILES = 20000
    SERVICE_CENTS = 30000
    SERVICE_MILES = 10000
    return (miles * TIRES_CENTS) // TIRES_MILES + miles * (SERVICE_CENTS // SERVICE_MILES)
def CostForMiles(miles: int) -> int:
    return CostForMilesGas(miles) + CostForMilesMaintenance(miles)

print(CostForMiles(int(input())), "cents")