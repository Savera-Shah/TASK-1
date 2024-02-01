def validate_weight(weight):
    try:
        weight = float(weight)
        if weight <= 0:
            return False
        return True
    except ValueError:
        return False

def main():
    num_pupils = 30
    names = []
    weights_first_day = []
    weights_last_day = []
    weight_diff = []

    for i in range(num_pupils):
        name = input(f"Enter the name of pupil {i+1}: ")
        
        weight_first_day = input(f"Enter the weight of pupil {i+1} on the first day of term (in kilograms): ")
        while not validate_weight(weight_first_day):
            print("Invalid weight. Please enter a valid positive weight.")
            weight_first_day = input(f"Enter the weight of pupil {i+1} on the first day of term (in kilograms): ")

        weight_last_day = input(f"Enter the weight of pupil {i+1} on the last day of term (in kilograms): ")
        while not validate_weight(weight_last_day):
            print("Invalid weight. Please enter a valid positive weight.")
            weight_last_day = input(f"Enter the weight of pupil {i+1} on the last day of term (in kilograms): ")

        names.append(name)
        weights_first_day.append(float(weight_first_day))
        weights_last_day.append(float(weight_last_day))
        weight_diff.append(weights_last_day[i] - weights_first_day[i])

    print("\nNames, Weights, and Weight Differences of Pupils:")
    for i in range(num_pupils):
        print(f"{names[i]}: First Day - {weights_first_day[i]} kg, Last Day - {weights_last_day[i]} kg, Difference - {weight_diff[i]} kg")

if __name__ == "__main__":
    main()
