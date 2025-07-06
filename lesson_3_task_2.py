from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "Galaxy S21", "+79123456789"),
    Smartphone("Apple", "iPhone 13", "+79098765432"),
    Smartphone("Google", "Pixel 6", "+79987654321"),
    Smartphone("OnePlus", "9 Pro", "+79876543210"),
    Smartphone("Xiaomi", "Mi 11", "+79765432109")
]


for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.number}")
