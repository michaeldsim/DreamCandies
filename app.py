import csv

# Load input file containing wanted customers
input_file = open('./data/input/CUSTOMER_SAMPLE.csv')
csv_reader = csv.reader(input_file, delimiter=',')

customers = []

# Skip the header line
next(csv_reader)

# Parse out all customer codes
for row in csv_reader:
    customers.append(row[0])

# Load data containing customers
customer_file = open('./data/CUSTOMER.csv')
csv_reader = csv.reader(customer_file, delimiter=',')

customer_names = []

# Skip the header line
next(csv_reader)

# Add all matching customers to list
for row in csv_reader:
    if row[0] in customers:
        customer_names.append(row)

# Load data containing invoices
invoice_file = open('./data/INVOICE.csv')
csv_reader = csv.reader(invoice_file, delimiter=',')

invoices = []
invoice_nums = []

# Skip the header line
next(csv_reader)

# Add all invoices matching customer codes to list
for row in csv_reader:
    if row[0] in customers:
        invoices.append(row)
        invoice_nums.append(row[1])

# Load data containing items for invoices
items_file = open('./data/INVOICE_ITEM.csv')
csv_reader = csv.reader(items_file, delimiter=',')

items = []

# Skip the header line
next(csv_reader)

# Add all items matching invoice codes to list
for row in csv_reader:
    if row[0] in invoice_nums:
        items.append(row)

# Write names to separate file
with open('./data/output/CUSTOMER.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['CUSTOMER_CODE','FIRSTNAME','LASTNAME'])
    writer.writerows(customer_names)

# Write invoices to separate file
with open('./data/output/INVOICES.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['CUSTOMER_CODE','INVOICE_CODE','AMOUNT','DATE'])
    writer.writerows(invoices)

# Write items to separate file
with open('./data/output/INVOICE_ITEM.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['INVOICE_CODE','ITEM_CODE','AMOUNT','QUANTITY'])
    writer.writerows(items)