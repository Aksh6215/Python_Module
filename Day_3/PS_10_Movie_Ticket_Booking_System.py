'''
Online Movie Ticket Booking System

Objective:
Develop an Online Movie Ticket Booking System where users can:
✔View available movies
✔Book tickets
✔Cancel tickets
✔Check booking history
Requirements:
Use a list of tuples to store movie details (Movie Name, Show Timing).
Use a dictionary to manage ticket bookings.
Implement functions for booking, cancellation, and history tracking.
Use sets to maintain unique seat numbers.
'''

MovieDetails = [("1", "Chhaava", "9:00 AM"),("2", "Sikandar", "12:00 PM"), ("3", "Deva", "3:00 PM"), ("4", "Dhamaal", "6:00 PM"), ("5", "Sholay", "9:00 PM"), ("6", "Avengers", "12:00 AM")]

TicketBooked = {}
seat_no = set()
def ShowMovies():
    for i in MovieDetails:
        print(i[0], i[1], i[2])

def BookTicket():
    movie_id = int(input("Enter movie id: "))
    if movie_id not in range(1,len(MovieDetails)+1):
        print("Enter valid movie id.")
        return
    else:
        if movie_id in TicketBooked:
            print("Movie already booked.")
            return
        else:
            user_id = int(input("Enter user id: "))
            user_name = input("Enter your name: ").strip().lower()
            seat_no = int(input("Enter seat number: "))
            TicketBooked[movie_id] = [user_id, user_name, seat_no]
            MovieDetails.pop(movie_id-1)
            print("Ticket booked successfully.")

def ShowBookedTickets():
    if TicketBooked == {}:
        print("No tickets booked yet.")
    for i, j in TicketBooked.items():
        print(i, j)

def CancelTicket():
    movie_id = int(input("Enter movie id: "))
    if movie_id not in TicketBooked:
        print("Ticket not booked.")
        return
    else:
        TicketBooked.pop(movie_id)
        print("Ticket cancelled successfully.")

while True:
    print("\n----- Online Movie Ticket Booking System -----")
    choice = int(input("\n 1. Show Movies \n 2. Book Ticket \n 3. Show Booked Tickets \n 4. Cancel Ticket \n 5. Exit \nEnter your choice: "))

    if choice == 1:
        ShowMovies()
    
    elif choice == 2:
        ShowMovies()
        BookTicket()

    elif choice == 3:
        ShowBookedTickets()
    
    elif choice == 4:
        CancelTicket()
        pass
    
    elif choice == 5:
        print("Exiting...")
        print("Thank you for visiting Ticket Booking System!")
        break
    else:
        print("Invalid Input")

    
# def AvailableMovies():
#     if MovieDetails == []:
#         print("No movies available.")
#     else:
#         if TicketBooked != {}:
#             for i in TicketBooked.keys():
#                 for j in MovieDetails:
#                     if j[0] == i:
#                         MovieDetails.remove(j)
#                         print("Movies available after booking: ")

#         for i in MovieDetails:
#             print(i[0], i[1], i[2])

