class Flight:
    def __init__(self, flight_id, from_city, to_city, price):
        self.flight_id = flight_id
        self.from_city = from_city
        self.to_city = to_city
        self.price = price

class Flight__Table:
    def __init__(self):
        self.flights = []

    def adding_flight(self, flight):
        # for adding flight
        self.flights.append(flight)

    def search_by_city(self, city):

        # for searching cities
        result = []
        for flight in self.flights:
            if flight.from_city == city or flight.to_city == city:
                result.append(flight)
        return result

    def search_by_from_to_city(self, from_city, to_city):
        result = []
        for flight in self.flights:
            if flight.from_city == from_city and flight.to_city == to_city:
                result.append(flight)
        return result

def main():
    flight_tables = Flight__Table()

    # Adding flights to the flight table
    flight_tables.adding_flight(Flight("AI161E90", "BLR", "BOM", 5600))
    flight_tables.adding_flight(Flight("BR161F91", "BOM", "BBI", 6750))
    flight_tables.adding_flight(Flight("AI161F99", "BBI", "BLR", 8210))
    flight_tables.adding_flight(Flight("VS171E20", "JLR", "BBI", 5500))
    flight_tables.adding_flight(Flight("AS171G30", "HYD", "JLR", 4400))
    flight_tables.adding_flight(Flight("AI131F49", "HYD", "BOM", 3499))

    print("Search options:")
    print("1. Flights for a particular City : ")
    print("2. Flights From a city : ")
    print("3. Flights between 2 cities : ")

    Selected_choice = int(input("Enter your choice : "))

    if Selected_choice == 1:
        city = input("Enter the city : ")
        result = flight_tables.search_by_city(city)
    elif Selected_choice == 2:
        city = input("Enter the city : ")
        result = flight_tables.search_by_city(city)
    elif Selected_choice == 3:
        from_city = input("Enter the source city : ")
        to_city = input("Enter the destination city : ")
        result = flight_tables.search_by_from_to_city(from_city, to_city)
    else:
        print("Invalid choice !!!")
        print("Select from the given options")
        return

    if not result:
        print("No flights found.")
        print("Sorry for the inconvience.")
    else:
        print("Flight ID\tFrom\tTo\tPrice")
        for flight in result:
            print(f"{flight.flight_id}\t{flight.from_city}\t{flight.to_city}\t{flight.price}")

if __name__ == "__main__":
    main()
