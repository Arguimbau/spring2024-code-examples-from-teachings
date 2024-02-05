class CarDatabase:
    def __init__(self):
        self.car_data = {}

    def add_car(self, number_plate, color, passengers, length):
        # Check if the number plate is already in the database
        if number_plate in self.car_data:
            print(f"Car with number plate {number_plate} already exists in the database.")
        else:
            # Add new car information to the database
            self.car_data[number_plate] = {
                'Color': color,
                'Passengers': passengers,
                'Length': length
            }
            print(f"Car with number plate {number_plate} successfully added to the database.")

    def get_car_info(self, number_plate):
        # Retrieve car information based on the number plate
        if number_plate in self.car_data:
            return self.car_data[number_plate]
        else:
            return f"No information found for the car with number plate {number_plate}."

# Example usage
storebaeltsbroen_database = CarDatabase()

# Add data for a new car
storebaeltsbroen_database.add_car("ABC123", "Blue", 4, 5.2)

# Retrieve information for a specific car
car_info = storebaeltsbroen_database.get_car_info("ABC123")
print(car_info)
# Pseudo code for keeping track of cars that have crossed all bridges

# Create sets for each bridge to store unique number plates
bridge1_cars = set()
bridge2_cars = set()
# ... (add more bridges as needed)

# Assume each bridge has its own CarDatabase instance
bridge1_database = CarDatabase()
bridge2_database = CarDatabase()
# ... (initialize databases for other bridges)

# Register cars for each bridge
bridge1_database.add_car("ABC123", "Blue", 4, 5.2)
bridge1_cars.add("ABC123")

bridge2_database.add_car("ABC123", "Red", 2, 4.8)
bridge2_cars.add("ABC123")

# ... (register cars for other bridges)

# Find cars that have crossed all bridges
cars_crossed_all_bridges = bridge1_cars.intersection(bridge2_cars)

# Print or use the information as needed
print(f"Cars that have crossed all bridges: {cars_crossed_all_bridges}")
