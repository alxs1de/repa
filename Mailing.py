class Mailing:

    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

    def print_info(self):
        print(f"Отправление {self.track} из {self.from_address.city} в {self.to_address.city}. Стоимость: {self.cost} рублей.")
