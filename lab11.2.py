import json

def write_json(data, file_path):
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def find_oldest_city(data):
    oldest_city = min(data, key=data.get)
    return oldest_city

cities = {
    "Kyiv": 482,
    "Chernihiv": 907,
    "Lviv": 1256,
    "Odessa": 1794,
    "Kharkiv": 1654
}

output_file = 'cities.json'

write_json(cities, output_file)
print(f"Дані збережено у {output_file}")

oldest_city = find_oldest_city(cities)
print(f"Місто з найбільшим віком: {oldest_city}")
