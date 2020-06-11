from mongo_seeder import MongoSeeder
from postgre_seeder import PostgreSeeder

# Mongo related seeding
print(MongoSeeder('./mongo_customer_companies.csv').seed('customer_companies'))
print(MongoSeeder('./mongo_customers.csv').seed('customers'))

# PostgreSQL related seeding
print(PostgreSeeder('./postgre_deliveries.csv').seed('deliveries'))
print(PostgreSeeder('./postgre_order_items.csv').seed('order_items'))
print(PostgreSeeder('./postgre_orders.csv').seed('orders'))

# Print finish
print("Seeding completed....")