# Function to calculate taxes and on-road price
def calculate_vehicle_details(vehicle_type, weight, basic_price):
    if vehicle_type.upper() == 'P':  # Private
        vt = 0.05 * basic_price
        wt_tax = 0.01 * weight
        ip = 0.01 * basic_price
    elif vehicle_type.upper() == 'B':  # Business
        vt = 0.10 * basic_price
        wt_tax = 0.03 * weight
        ip = 0.02 * basic_price
    else:
        raise ValueError("Invalid vehicle type. Use 'P' for Private or 'B' for Business.")

    on_road_price = basic_price + vt + wt_tax + ip

    return {
        "Type": vehicle_type.upper(),
        "Weight": weight,
        "Basic Price": basic_price,
        "Vehicle Tax": vt,
        "Weight Tax": wt_tax,
        "Insurance": ip,
        "On-Road Price": on_road_price
    }

# Input: Details for N vehicles
vehicles = []
n = int(input("Enter number of vehicles: "))
for i in range(n):
    print(f"\nEnter details for Vehicle {i+1}:")
    v_type = input("Type (P for Private, B for Business): ")
    weight = float(input("Weight of vehicle: "))
    basic_price = float(input("Basic price: "))

    vehicle_dict = calculate_vehicle_details(v_type, weight, basic_price)
    vehicles.append(vehicle_dict)

# a. Dictionary already created for each vehicle
print("\nAll Vehicle Details:")
for idx, v in enumerate(vehicles, 1):
    print(f"Vehicle {idx}:", v)

# c.i. Vehicle(s) with highest on-road price
max_price = max(v["On-Road Price"] for v in vehicles)
highest_priced_vehicles = [v for v in vehicles if v["On-Road Price"] == max_price]
print("\nVehicle(s) with highest on-road price:")
for v in highest_priced_vehicles:
    print(v)

# c.ii. Vehicle(s) with least weight
min_weight = min(v["Weight"] for v in vehicles)
lightest_vehicles = [v for v in vehicles if v["Weight"] == min_weight]
print("\nVehicle(s) with least weight:")
for v in lightest_vehicles:
    print(v)

# d.i. Average on-road price
avg_price = sum(v["On-Road Price"] for v in vehicles) / n
print(f"\nAverage On-Road Price: Rs.{avg_price:.2f}")

# d.ii. Count of vehicles with on-road price > average
count_above_avg = sum(1 for v in vehicles if v["On-Road Price"] > avg_price)
print(f"Vehicles with on-road price above average: {count_above_avg}")

# d.iii. Count of vehicles with weight above a given value
given_weight = float(input("\nEnter a weight value to compare: "))
count_weight_above = sum(1 for v in vehicles if v["Weight"] > given_weight)
print(f"Vehicles with weight above {given_weight}: {count_weight_above}")

# d.iv. Count of vehicles with on-road price <= given budget
budget = float(input("Enter your budget: "))
count_within_budget = sum(1 for v in vehicles if v["On-Road Price"] <= budget)
print(f"Vehicles with on-road price within Rs.{budget}: {count_within_budget}")
