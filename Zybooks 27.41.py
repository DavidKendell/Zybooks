def ActivityCalories(activity: str, mins: int) -> float:
    factor: float
    match(activity):
        case "sit":
            factor = 1.4
        case "walk":
            factor = 5.4
        case "run":
            factor = 13.0
        case "bike":
            factor = 6.8
        case "swim":
            factor = 8.7
    return mins * factor
userActivity, userMinutes = (input(), int(input()))
print(ActivityCalories(userActivity, userMinutes))