# Practice Question Customer data
order = {
    "P001":["Laptop", "60000"],
    "P002":["Mobile", "50000"],
    "P003":["Tablet", "30000"],
    "P004":["Earphone", "1000"],
}

customer = [{
    "id":"A01",
    "Name":"Akshat",
    "email":"aksh@12",
    "Order_history":order},
    {"id":"A02",
     "Name":"Rahul",
     "email":"rahul@12",
     "Order_history":order
     }]
order["P001"][0] = "Computer"

print(customer[0]["Order_history"]["P001"])
print(customer[1]["Order_history"]["P002"])
