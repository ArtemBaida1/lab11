import csv

def read_csv(file_path):
    products = {}
    with open(file_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            products[row['Product']] = float(row['Price'])
    return products

def write_csv(data, output_file_path):
    with open(output_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Product', 'Price'])
        for product, price in data.items():
            writer.writerow([product, price])

input_file = 'products.csv'
output_file = 'output_products.csv'

products = read_csv(input_file)
write_csv(products, output_file)
print("Дані успішно збережено у", output_file)
