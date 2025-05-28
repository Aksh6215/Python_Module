# Car Rental System

car = {
"1" : {
    "car_name": "Toyota",
    "car_id": "1",
    "model_name": "Toyota Corolla",
    "car_price": "1000",
},
"2" : {
    "car_name": "Honda",
    "car_id": "2",
    "model_name": "Honda Civic",
    "car_price": "2000",
},
"3" : {
    "car_name": "Suzuki",  
    "car_id": "3",
    "model_name": "Suzuki Cultus",
    "car_price": "3000",
}
}

car_list = ["1","2","3"]
rented_cars = {}
rental_history = {}
while True:
    request = int(input("\n1. Show available Cars\n2. Rent a Car\n3. View rented cars\n4. Return a car\n5. Rental History\n6. Exit\nEnter your choice: "))
    
    if request == 1:
        print("\nAvailable Cars:")
        for i in car:
            print(i, car[i]['model_name'], car[i]['car_price'])

    elif request == 2:
        car_id = input("Enter car ID: ")
        if car_id in car_list:
            customer = input("Enter your name: ").strip().lower()
            duration = int(input("Enter rental duration(days): ").strip())
            price = duration*int(car[car_id]['car_price'])
            print("Total price for the rental car: ", price)
            print("Car rented successfully")
            car_list.remove(car_id)
            rented_cars[customer] = [car_id,duration,price]
            rental_history[customer] = [car_id,duration,price]
        else:
            print("Enter valid Id")

    elif request == 3:
        print("Rented cars are:\n")
        if len(rented_cars) == 0:
            print("No cars rented yet")
        for x,y in rented_cars.items():
            print("{} :  {}".format(x,y))

    elif request == 4:
        name = input("Enter your name: ").strip()
        car_list.append(rented_cars[name][0])
        rented_cars.pop(name)
    
    elif request == 5:
        print("Rental History is:\n")
        for x,y in rental_history.items():
            print("{} :  {}".format(x,y))
    
    elif request == 6:
        print("Exiting...")
        break

    else:
        print("Invalid choice")
        break
