from smartphone import Smartphone

catalog = [
    Smartphone("Nokia", "3310", "+79223335588"),
    Smartphone("Xiaomi", "Redmi 10", "+79111234567"),
    Smartphone("Apple", "iPhone 15", "+79068463587"),
    Smartphone("Samsung", "Galaxy S25", "+79308463521"),
    Smartphone("Tecno", "Camon 40", "+79219995533")
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}, {smartphone.number}")