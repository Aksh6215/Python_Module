'''
Flight Reservation System

Objective:
Create a Flight Reservation System where users can:
Search available flights
✔Book a flight ticket
Cancel a booking
✔View flight details
Requirements:
Use a list of dictionaries to store flight details (Flight No, Destination, Price).
Use a dictionary to manage passenger bookings.
Implement functions for searching flights, booking, and cancellation.
Use lambda functions to filter flights based on price.
'''
'''
flights = []
bookings = {}

def add_flight():
    flight_no = input("Enter flight number: ")
    destination = input("Enter destination: ")
    price = int(input("Enter price: "))
    flights.append({"Flight No": flight_no, "Destination": destination, "Price": price})

def view_flights():
    print("Available Flights:")
    for flight in flights:
        print(f"Flight No: {flight['Flight No']}, Destination: {flight['Destination']}, Price: {flight['Price']}")

def search_flights():
    max_price = int(input("Enter maximum price: "))
    print("Flights within your budget:")
    for flight in filter(lambda f: f["Price"] <= max_price, flights):
        print(f"Flight No: {flight['Flight No']}, Destination: {flight['Destination']}, Price: {flight['Price']}")

def book_ticket():
    view_flights()
    flight_no = input("Enter the flight number to book: ")
    user_name = input("Enter your name: ")
    if flight_no not in bookings:
        bookings[flight_no] = []
    bookings[flight_no].append(user_name)
    print("Ticket booked successfully!")

def cancel_booking():
    user_name = input("Enter your name to cancel booking: ")
    flight_no = input("Enter flight number: ")
    if flight_no in bookings and user_name in bookings[flight_no]:
        bookings[flight_no].remove(user_name)
        print("Booking cancelled successfully!")
    else:
        print("Booking not found.")

def view_booking():
    user_name = input("Enter your name to view booking: ")
    print("Your Bookings:")
    for flight_no, passengers in bookings.items():
        if user_name in passengers:
            print(f"Flight No: {flight_no}")

while True:
    print("\n----- Flight Reservation System -----")
    choice = int(input("\n1. Add Flight\n 2. View Available Flights\n 3. Search Flights\n 4. Book Ticket\n 5. Cancel Booking\n 6. View Booking\n 7. Exit\nEnter your choice: "))

    if choice == "1":
        add_flight()
    elif choice == "2":
        view_flights()
    elif choice == "3":
        search_flights()
    elif choice == "4":
        book_ticket()
    elif choice == "5":
        cancel_booking()
    elif choice == "6":
        view_booking()
    elif choice == "7":
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
'''
"""
Flight Reservation System
Objective:
Create a Flight Reservation System where users can:
-> Search available flights
-> Book a flight ticket
-> Cancel a booking
-> View flight details
Requirements:
 Use a list of dictionaries to store flight details (Flight No, Destination, Price).
 Use a dictionary to manage passenger bookings.
 Implement functions for searching flights, booking, and cancellation.
 Use lambda functions to filter flights based on price.
"""

FlightDetails = [{"flight_no": 4, "destination": "Delhi", "price": 5000}, {"flight_no": 5, "destination": "Jaipur", "price": 2000}, {"flight_no": 6, "destination": "Gurgaon", "price": 3000}]
bookings = {}

def SearchFlight():
    dest = input("Enter destination: ")
    available_f = []
    for f in FlightDetails:
        if dest.lower() == f["destination"].lower():
            available_f.append(f)
    if available_f:
        available_f.sort(key=lambda x: x["price"])
        print("Available flights are:")
        for i in available_f:
            print(str(i["flight_no"]), i["destination"], str(i["price"]), "\n")
    else:
        print("No flights available.")


def FlightBooking():
    name = input("Enter your name: ")
    flight_no = int(input("Enter flight number: "))

    for f in FlightDetails:
        if f["flight_no"] == flight_no:
            bookings[name] = f
            print(f"Booking confirmed!")
            break


def CancelFlight():
    name = input("Enter your name to cancel booking: ")

    if name in bookings:
        del bookings[name]
        print("Booking cancelled.")
    else:
        print("No booking found.")


def ViewFlight():
    print("Flight Details:")
    for flight in FlightDetails:
        print(f"Flight No: {flight['flight_no']}, Destination: {flight['destination']}, Price: {flight['price']}")


while True:
    print("****** Welcome to Flight Reservation System ******")
    request = int(input("\n 1. Search flight \n 2. Book flight \n 3. Cancel flight \n 4. View flight details \n 5. Exit \nEnter your choice: "))
    if request == 1:
        SearchFlight()
    elif request == 2:
        FlightBooking()
    elif request == 3:
        CancelFlight()
    elif request == 4:
        ViewFlight()
    elif request == 5:
        print("Thank You")
        break
    else:
        print("Invalid request.")
