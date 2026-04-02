from address import Address
from mailing import Mailing

# Создание экземпляра класса Address
address1 = Address(125847, "город Москва", "улица Арбат", 102, 57)
address2 = Address(865214, "город Томск", "улица Ленина", 40, 14)

# Создание экземпляра класса Mailing
mailing = Mailing(address1, address2, 800, "123456789")

print(f"Отправление {mailing.track} из {mailing.from_address} в {mailing.to_address}. Стоимость {mailing.cost} рублей.")