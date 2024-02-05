class CarDatabase:
    def __init__(self):
        self.car_data = {}

    def add_car(self, number_plate, color, passengers, length):
        # Check if the number plate is already in the database
        if number_plate in self.car_data:
            print(f"Car with number plate {number_plate} already exists in the database.")
        else:
            # Add new car information to the database as a tuple
            self.car_data[number_plate] = (color, passengers, length)
            print(f"Car with number plate {number_plate} successfully added to the database.")

    def get_car_info(self, number_plate):
        # Retrieve car information based on the number plate
        if number_plate in self.car_data:
            return self.car_data[number_plate]
        else:
            return f"No information found for the car with number plate {number_plate}."

    def print_database(self):
        # Print the entire database
        print("Car Database:")
        for number_plate, car_info in self.car_data.items():
            print(
                f"Number Plate: {number_plate}, Color: {car_info[0]}, Passengers: {car_info[1]}, Length: {car_info[2]}")
# Example usage
storebaeltsbroen_database = CarDatabase()

# Add data for a new car
storebaeltsbroen_database.add_car("ABC123", "Blue", 4, 5.2)


# Retrieve information for a specific car
print('Car Info:')
car_info = storebaeltsbroen_database.get_car_info("ABC123")

print(car_info)
storebaeltsbroen_database.print_database()
