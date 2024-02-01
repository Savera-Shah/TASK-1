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
    weights = []

    for i in range(num_pupils):
        name = input(f"Enter the name of pupil {i+1}: ")
        weight = input(f"Enter the weight of pupil {i+1} in kilograms: ")

        while not validate_weight(weight):
            print("Invalid weight. Please enter a valid positive weight.")
            weight = input(f"Enter the weight of pupil {i+1} in kilograms: ")

        names.append(name)
        weights.append(float(weight))

    print("\nNames and Weights of Pupils:")
    for i in range(num_pupils):
        print(f"{names[i]}: {weights[i]} kg")

if __name__ == "__main__":
    main()
