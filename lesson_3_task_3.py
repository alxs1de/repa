from Address import Address
from Mailing import Mailing

to_addr = Address("123456", "Москва", "Ленина", "1", "101")
from_addr = Address("654321", "Сочи", "Морская", "5", "42")
mailing = Mailing(to_addr, from_addr, 500, "TRACK123")

mailing.print_info()  # Если добавил метод в Mailing
