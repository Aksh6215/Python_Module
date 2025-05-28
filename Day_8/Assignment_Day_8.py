'''
1) Event Scheduler
Create a Python program using Object-Oriented Programming (OOP) to manage events. Each event should have a name, date, and time. Use the datetime module to handle date and time operations.
Implement the following functionalities:
1. Add an event.
2. Remove an event.
3. Display all events in chronological order.
4. Save events to a file using the pickle module.
5. Load events from a file using the pickle module.
'''
'''
from datetime import datetime as dt
import pickle

class EventScheduler:
    def __init__(self):
        self.events = []

    def add_event(self):
        name = input("Event name: ")
        date = input("Event date (DD-MM-YYYY): ")
        time = input("Event time (HH:MM): ")
        
        try:
            event = (name, dt.strptime(date, "%d-%m-%Y"), dt.strptime(time, "%H:%M").time())
            self.events.append(event)
            self.events.sort(key=lambda e: (e[1], e[2]))  # Sort by date and time
            print("Event '{}' added successfully.\n".format(name))
        except ValueError:
            print("Please use YYYY-MM-DD for date and HH:MM for time.\n")

    def remove_event(self):
        name = input("Enter event name to remove: ")
        for event in self.events:
            if event[0] == name:
                self.events.remove(event)
                print("Event '{}' removed successfully.\n".format(name))
                return
        print("Event '{}' not found.\n".format(name))

    def display_events(self):
        if not self.events:
            print("No events scheduled.\n")
        else:
            print("\nScheduled Events:")
            for name, date, time in self.events:
                print(f"{name} - {date.strftime('%d-%m-%Y')} at {time.strftime('%H:%M')}")
            print()

    def save_events(self, filename="events.pkl"):
        with open(filename, "wb") as file:
            pickle.dump(self.events, file)
        print("Events saved successfully.\n")

    def load_events(self, filename="events.pkl"):
        try:
            with open(filename, "rb") as file:
                self.events = pickle.load(file)
            self.events.sort(key=lambda e: (e[1], e[2]))  # Ensure sorting after loading
            for event in self.events:
                print(event)
            print("Events loaded successfully.\n")
        except FileNotFoundError:
            print("File does not exists.\n")
    
obj = EventScheduler()
print("----- Event Scheduler -----")
while True:
    try:
        choice = int(input("\n 1. Add an Event\n 2. Remove an Event\n 3. Display Events\n 4. Save Events to file\n 5. Load Events of file\n 6. Exit\nEnter your choice: "))

        if choice == 1:
            obj.add_event()
        elif choice == 2:
            obj.remove_event()
        elif choice == 3:
            obj.display_events()
        elif choice == 4:
            obj.save_events()
        elif choice == 5:
            obj.load_events()
        elif choice == 6:
            print("Exiting...")
            break
        else:
            print("Invalid choice.\n")
    except ValueError:
        print("Invalid Input!")
'''

'''
2) Advanced Password Manager
Create a password manager using OOP. Each password entry should have attributes
like website, username, password, and last updated date (use datetime). Implement the following
functionalities:
1. Add a password entry (handle exceptions for invalid inputs).
2. Use regex to validate password strength.
3. Use a generator to yield passwords that were last updated more than 90 days ago.
4. Save password entries to a file using pickle (handle file-related exceptions).
5. Load password entries from a file using pickle (handle file-related exceptions).
6. Create a custom module password_utils.py to handle password validation and encryption.
7. Handle exceptions for invalid file operations. 
'''

from datetime import datetime as dt
import pickle
import os
from password_utils import validate_password, encrypt_password, decrypt_password

class PasswordManager:
    def __init__(self):
        self.passwords = []

    def add_entry(self):
        website = input("Enter website name: ")
        username = input("Enter username: ")
        password = input("Enter password: ")

        if not validate_password(password):
            print("Password must be at least 8 characters long, include uppercase, lowercase, a number, and a special character.\n")
            return

        encrypted_password = encrypt_password(password)
        last_updated = dt.now().strftime("%d-%m-%Y")

        self.passwords.append((website, username, encrypted_password, last_updated))
        print("Password entry added successfully!\n")

    def display_entries(self):
        if not self.passwords:
            print("No password entries found.\n")
        else:
            print("\nSaved Passwords:")
            for website, username, encrypted_password, last_updated in self.passwords:
                print("Website: {}, Username: {}, Password: {}, Last Updated: {}".format(website, username, decrypt_password(encrypted_password), last_updated))
            print()

    def outdated_passwords(self):
        today = dt.now()
        for website, username, encrypted_password, last_updated in self.passwords:
            last_updated_date = dt.strptime(last_updated, "%d-%m-%Y")
            if (today - last_updated_date).days > 90:
                yield website, username, decrypt_password(encrypted_password), last_updated

    def show_outdated_passwords(self):
        outdated = list(self.outdated_passwords())
        if not outdated:
            print("No outdated passwords found.\n")
        else:
            print("\nOutdated Passwords (over 90 days old):")
            for website, username, password, last_updated in outdated:
                print(f"Website: {website}, Username: {username}, Password: {password}, Last Updated: {last_updated}")
            print()

    def save_passwords(self, filename="passwords.pkl"):
        try:
            with open(filename, "wb") as file:
                pickle.dump(self.passwords, file)
            print("Passwords saved successfully!\n")
        except Exception as e:
            print(f"Error saving passwords: {e}\n")

    def load_passwords(self, filename="passwords.pkl"):
        if not os.path.exists(filename):
            print("File does not exists.\n")
            return
        
        try:
            with open(filename, "rb") as file:
                self.passwords = pickle.load(file)
            print("Passwords loaded successfully!\n")
        except Exception as e:
            print(f"Error loading passwords: {e}\n")

obj = PasswordManager()

while True:
    try:
        choice = input("\n 1. Add Password entry\n 2. Display All Passwords\n 3. Show Outdated Passwords\n 4. Save Passwords\n 5. Load Passwords\n 6. Exit \nEnter the choice: ")

        if choice == "1":
            obj.add_entry()
        elif choice == "2":
            obj.display_entries()
        elif choice == "3":
            obj.show_outdated_passwords()
        elif choice == "4":
            obj.save_passwords()
        elif choice == "5":
            obj.load_passwords()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice!\n")

    except ValueError:
        print("Invalid input value!")


'''
3) Problem Statement : Advanced Travel Itinerary Planner
Create a Python program that plans travel itineraries. Each itinerary should have attributes
like itinerary ID, destination, start date (use datetime), and end date. Implement the following
functionalities:
1. Add an itinerary (handle exceptions for invalid dates).
2. Use regex to validate the format of the destination.
3. Use a generator to yield itineraries starting in the next 7 days.
4. Save itinerary data to a file using pickle (handle file-related exceptions).
5. Load itinerary data from a file using pickle (handle file-related exceptions).
6. Create a custom module travel_utils.py to handle itinerary planning logic.
7. Implement logic to handle overlapping itineraries.
'''
'''
from datetime import datetime as dt, timedelta
import pickle
import os
from travel_utils import validate_destination, check_overlap

class TravelPlanner:
    def __init__(self):
        self.itineraries = []

    def add_itinerary(self):
        itinerary_id = input("Enter itinerary ID: ")
        destination = input("Enter destination: ")
        start_date = input("Enter start date (DD-MM-YYYY): ")
        end_date = input("Enter end date (DD-MM-YYYY): ")

        if not validate_destination(destination):
            print("Invalid destination format.\n")
            return

        try:
            start = dt.strptime(start_date, "%d-%m-%Y")
            end = dt.strptime(end_date, "%d-%m-%Y")

            if end < start:
                print("End date must be after start date.\n")
                return

            if check_overlap(self.itineraries, start, end):
                print("Choose different dates, it is already occupied.\n")
                return

            self.itineraries.append((itinerary_id, destination, start, end))
            print("Itinerary added successfully!\n")
        
        except ValueError:
            print("Invalid date format. Use DD-MM-YYYY.\n")

    def display_itineraries(self):
        if not self.itineraries:
            print("No itineraries available.\n")
        else:
            self.itineraries.sort(key=lambda i: i[2])  # Sort by start date
            print("\nUpcoming Itineraries:")
            for itinerary_id, destination, start, end in self.itineraries:
                print("ID: {}, Destination: {}, Start: {}, End: {}".format(itinerary_id, destination, start.strftime('%d-%m-%Y'), end.strftime('%d-%m-%Y')))
            print()

    def upcoming_itineraries(self):
        today = dt.now()
        for itinerary in self.itineraries:
            if 0 <= (itinerary[2] - today).days <= 7:
                yield itinerary

    def show_upcoming_itineraries(self):
        upcoming = list(self.upcoming_itineraries())
        if not upcoming:
            print("No upcoming itineraries in the next 7 days.\n")
        else:
            print("\nItineraries starting in the next 7 days:")
            for itinerary_id, destination, start, end in upcoming:
                print("ID: {}, Destination: {}, Start: {}, End: {}".format(itinerary_id, destination, start.strftime('%d-%m-%Y'), end.strftime('%d-%m-%Y')))
            # print()

    def save_itineraries(self, filename="itineraries.pkl"):
        try:
            with open(filename, "wb") as file:
                pickle.dump(self.itineraries, file)
            print("Itineraries saved successfully!\n")
        except Exception as e:
            print(f"Error saving itineraries: {e}\n")

    def load_itineraries(self, filename="itineraries.pkl"):
        if not os.path.exists(filename):
            print("No saved itineraries found.\n")
            return
        
        try:
            with open(filename, "rb") as file:
                self.itineraries = pickle.load(file)
            print("Itineraries loaded successfully!\n")
        except Exception as e:
            print(f"Error loading itineraries: {e}\n")

planner = TravelPlanner()

while True:
    try:
        choice = int(input("\n 1. Add Itinerary\n 2. Display Itineraries\n 3. Show Upcoming Itineraries\n 4. Save Itineraries\n 5. Load Itineraries\n 6. Exit\nEnter your choice: "))

        if choice == 1:
            planner.add_itinerary()
        elif choice == 2:
            planner.display_itineraries()
        elif choice == 3:
            planner.show_upcoming_itineraries()
        elif choice == 4:
            planner.save_itineraries()
        elif choice == 5:
            planner.load_itineraries()
        elif choice == 6:
            print("Exiting...")
            break
        else:
            print("Invalid choice.\n")

    except ValueError:
        print("Invalid input.\n")
'''

'''
4) Problem Statement: Goods Trading &amp; Tax Calculator
Create a Python program to manage goods trading between buyers and sellers. The program should
track purchases, sales, and calculate taxes like GST/VAT on sold goods. It should also analyze trading
patterns and handle inventory.

✅ Key Features &amp; Requirements:
1. OOP-based Design:
o Classes: Product, Trade, Inventory, Trader.
o Each Product should have a name, SKU (Stock Keeping Unit), price, and tax rate.
o Each Trade will have product details, buy/sell type, quantity, price, and date.
2. Inventory Management:
o Add products to the inventory.
o Track available stock levels after trades.
3. Trade Operations:
o Add buy and sell trades.
o Use regex to validate product names and SKUs (e.g., SKU-12345).
4. Tax Calculation:
o Apply GST/VAT on sold goods based on their tax rate.
o Calculate total sales, total tax, and net profit.
o Use datetime to handle trade dates for sales reports.
5. Profit Analysis:
o Calculate profits/losses on goods sold.
o Use a generator to yield trades with profit margins &gt;20%.
6. Custom Module trade_utils.py:
o Functions for tax calculation, profit analysis, and SKU validation.
7. File Handling with Pickle:
o Save inventory and trade history to a file.
o Load saved data on startup, handling file-related exceptions.
8. Exception Handling:
o Handle invalid product inputs, trade entries, or file errors.
o Raise custom exceptions for invalid SKUs or insufficient stock.

�� Example Flow:
1. User starts the program and loads inventory.
2. User adds products:
o Product: Laptop, SKU-12345, Price: $1000, Tax Rate: 18%
o Product: Phone, SKU-67890, Price: $600, Tax Rate: 12%
3. User records trades:
o BUY Laptop x10 on 2024-03-01
o SELL Laptop x5 @ $1200 on 2024-03-15
4. Program validates SKUs using regex.
5. Tax and profit are calculated:
o Sale Amount: $6000
o GST (18%): $1080
o Profit: $1000
6. Inventory updates: 5 Laptops remain.
7. All data is saved using pickle.
'''
'''
import pickle
import os
import re
from datetime import datetime as dt
from trade_utils import validate_sku, calculate_tax, calculate_profit, is_high_margin_trade

class Product:
    def __init__(self, name, sku, price, tax_rate):
        if not validate_sku(sku):
            raise ValueError("Invalid SKU format. Use 'SKU-12345'.")
        self.name = name
        self.sku = sku
        self.price = price
        self.tax_rate = tax_rate

class Trade:
    def __init__(self, product, trade_type, quantity, trade_price, trade_date):
        self.product = product
        self.trade_type = trade_type  # BUY or SELL
        self.quantity = quantity
        self.trade_price = trade_price
        self.trade_date = dt.strptime(trade_date, "%Y-%m-%d")

class Inventory:
    def __init__(self):
        self.products = {}
        self.trades = []

    def add_product(self):
        try:
            name = input("Enter product name: ")
            sku = input("Enter product SKU (SKU-12345): ")
            price = float(input("Enter product price: "))
            tax_rate = float(input("Enter tax rate (%): "))

            if sku in self.products:
                print("Product already exists.\n")
                return

            product = Product(name, sku, price, tax_rate)
            self.products[sku] = product
            print("Product added successfully!\n")
        except ValueError as e:
            print(f"Error: {e}\n")

    def record_trade(self):
        sku = input("Enter product SKU (SKU-12345): ")
        if sku not in self.products:
            print("Product not found.\n")
            return
        
        trade_type = input("Enter trade type (BUY/SELL): ").upper()
        quantity = int(input("Enter quantity: "))
        trade_price = float(input("Enter trade price per unit: "))
        trade_date = input("Enter trade date (YYYY-MM-DD): ")

        product = self.products[sku]

        if trade_type == "SELL":
            if sku not in self.get_stock_levels() or self.get_stock_levels()[sku] < quantity:
                print("Insufficient stock to complete the sale.\n")
                return

        trade = Trade(product, trade_type, quantity, trade_price, trade_date)
        self.trades.append(trade)

        print(f"Trade recorded successfully: {trade_type} {quantity} {product.name} at ${trade_price} each.\n")

    def get_stock_levels(self):
        stock = {}
        for trade in self.trades:
            if trade.product.sku not in stock:
                stock[trade.product.sku] = 0
            if trade.trade_type == "BUY":
                stock[trade.product.sku] += trade.quantity
            elif trade.trade_type == "SELL":
                stock[trade.product.sku] -= trade.quantity
        return stock

    def calculate_sales_summary(self):
        total_sales = 0
        total_tax = 0
        total_profit = 0

        for trade in self.trades:
            if trade.trade_type == "SELL":
                tax_amount = calculate_tax(trade.trade_price, trade.product.tax_rate) * trade.quantity
                profit = calculate_profit(trade.product.price, trade.trade_price, trade.quantity)

                total_sales += trade.trade_price * trade.quantity
                total_tax += tax_amount
                total_profit += profit

        print("\nSales Summary:")
        print("Total Sales: ${}".format(total_sales))
        print("Total Tax Collected: ${}".format(total_tax))
        print("Total Profit: ${}\n".format(total_profit))

    def show_high_margin_trades(self):
        print("\nHigh Margin Trades (>20% Profit):")
        for trade in self.trades:
            if trade.trade_type == "SELL":
                profit = calculate_profit(trade.product.price, trade.trade_price, trade.quantity)
                for high_profit, margin in is_high_margin_trade(profit, trade.product.price, trade.quantity):
                    print("Product: {}, Profit: ${}, Margin: {}.2f%".format(trade.product.name, high_profit, margin))
        print()

    def save_data(self):
        try:
            with open("inventory.pkl", "wb") as file:
                pickle.dump(self.products, file)
            with open("trades.pkl", "wb") as file:
                pickle.dump(self.trades, file)
            print("Data saved successfully!\n")
        except Exception as e:
            print(f"Error saving data: {e}\n")

    def load_data(self):
        if os.path.exists("inventory.pkl"):
            with open("inventory.pkl", "rb") as file:
                self.products = pickle.load(file)
        if os.path.exists("trades.pkl"):
            with open("trades.pkl", "rb") as file:
                self.trades = pickle.load(file)
        print("Data loaded successfully!\n")

obj = Inventory()
obj.load_data()

while True:
    try:
        choice = int(input("\n 1. Add Product\n 2. Record Trade\n 3. Show Stock Levels\n 4. Show Sales Summary\n 5. Show High Margin Trades\n 6. Save Data\n 7. Exit\nEnter your choice: "))

        if choice == 1:
            obj.add_product()
        elif choice == 2:
            obj.record_trade()
        elif choice == 3:
            stock = obj.get_stock_levels()
            print("\nStock Levels:")
            for sku, qty in stock.items():
                print("{} (SKU: {}) - {} in stock".format(obj.products[sku].name, sku, qty))
            print()
        elif choice == 4:
            obj.calculate_sales_summary()
        elif choice == 5:
            obj.show_high_margin_trades()
        elif choice == 6:
            obj.save_data()
        elif choice == 7:
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.\n")
    except ValueError:
        print("Invalid Input!")

'''