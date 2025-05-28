
# car rental system 
'''
Functions

1. Rented_Cars
2. Return_Car
3. Rental_History
4. Exit
'''

available_cars = {
    "101" : ["Honda Civic",1000],
    "102" : ["Maruti Suzuki",1000],
    "103" : ["Chevrolet",1000]
}

car_list = ["101","102","103"]
rented_cars ={}
rental_history = {}

def Rented_Cars():
    print("Rented cars are:\n")
    if len(rented_cars) == 0:
        print("No cars rented yet")
    for x,y in rented_cars.items():
        print("{} :  {}".format(x,y))

def Return_Car():
    name = input("Enter your name: ").strip()
    car_list.append(rented_cars[name][0])
    rented_cars.pop(name)

def Rental_History():
    print("Rental History is:\n")
    for x,y in rental_history.items():
        print("{} :  {}".format(x,y))

def Exit():
    print("Exiting...")

while True:
    # request()
    request = int(input("Enter request: \n 1. View available cars \n 2. Rent a car \n 3. View rented cars \n 4. Return a car \n 5. Rental History \n 6. Exit\n"))

    # Show available cars
    if request == 1:
        for i in car_list:
            print(i,available_cars[i][0],available_cars[i][1])

    # Rent a car
    elif request == 2:
        car_id = input("Enter car ID: ")
        if car_id in car_list:
            customer = input("Enter your name: ").strip().lower()
            duration = int(input("Enter rental duration(days): ").strip())
            price = duration*available_cars[car_id][1]
            print("Total price for the rental car: ", price)
            car_list.remove(car_id)
            rented_cars[customer] = [car_id,duration,price]
            rental_history[customer] = [car_id,duration,price]
        else:
            print("Enter valid Id")

    # View rented cars
    elif request == 3:
        Rented_Cars()

    # Return a car
    elif request == 4:
        Return_Car()
    
    # Rental History
    elif request == 5:
        Rental_History()

    # Exit
    elif request == 6:
        Exit()
        break

    else:
        print("Enter valid request.")

