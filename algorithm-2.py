def find_starting_city(city_distances, fuel, mpg):
    total_gas = 0
    total_distance = 0
    start_city = 0
    
    for i in range(len(city_distances)):
        total_gas += fuel[i]
        total_distance += city_distances[i]
        
        if total_gas * mpg < total_distance:
            start_city = i + 1
            total_gas = 0
            total_distance = 0
            
    return start_city % len(city_distances)

# Sample Input
city_distances = [5, 25, 15, 10, 15]
fuel = [1, 2, 1, 0, 3]
mpg = 10
print(f'case 1: {find_starting_city(city_distances, fuel, mpg)}')  # Output: 4

# case 2
city_distances = [10, 20, 30, 40]
fuel = [2, 4, 3, 2]
mpg = 5
print(f'case 2: {find_starting_city(city_distances, fuel, mpg)}')  # Output: 0

# case: minimum input
city_distances = [5]
fuel = [1]
mpg = 10
print(f'case 3: {find_starting_city(city_distances, fuel, mpg)}')  # Output: 0
