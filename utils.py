from config import collection

collection.insert_many([
    {
        "customer_id" : "C001",
        "age": 30,
        "tenure": 3,
        "services" : ["Internet","Phone"],
        "monthly_charges": 65.0
    },
    {
        "customer_id" : "C002",
        "age": 25,
        "tenure": 2,
        "services" : ["Internet"],
        "monthly_charges": 50.0
    
    },
    {
        "customer_id" : "C003",
        "age": 40,
        "tenure": 4,
        "services" : ["Internet","Phone","TV"],
        "monthly_charges": 70.0
    },
    {
        "customer_id" : "C004",
        "age": 35,
        "tenure": 3,
        "services" : ["Internet","Phone"],
        "monthly_charges": 60.0
    }
])
print("Data inserted successfully")
