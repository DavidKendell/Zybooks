def CalculateMonthElectricCost(monthKWh: float, tier1Cutoff: float, tier1Cost: float,\
                               tier2Cutoff: float, tier2Cost: float, tier3Cost: float) -> float:
    remainingKWh = monthKWh
    monthCost = 0
    if remainingKWh - tier1Cutoff - tier2Cutoff > 0:
        tierKWh = remainingKWh - tier1Cutoff - tier2Cutoff
        monthCost += tierKWh * tier3Cost
        remainingKWh -= tierKWh
    if remainingKWh - tier1Cutoff > 0:
        tierKWh = remainingKWh - tier1Cutoff
        monthCost += tierKWh * tier2Cost
        remainingKWh -= tierKWh
    monthCost += remainingKWh * tier1Cost
    return monthCost
monthKWh, tier1Cutoff, tier1Cost, tier2Cutoff, tier2Cost, tier3Cost = [float(input()) for i in range(6)]
monthCost = CalculateMonthElectricCost(monthKWh, tier1Cutoff, tier1Cost, tier2Cutoff, tier2Cost, tier3Cost)
print(f"${monthCost:.2f}")

