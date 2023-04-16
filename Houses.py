import time


class Houses:

    def __init__(self, income, no_of_houses):
        self.income = income
        self.no_of_houses = no_of_houses

    def __repr__(self):
        return f"income: {self.income}, no_of_houses: {self.no_of_houses}"

    def house_iteration(self):
        while True:
            self.income += 1

            time.sleep(1)

            if self.income % 10 == 0:
                self.no_of_houses += 1

            print(f"The estate's income is: {self.income} and the number of houses is {self.no_of_houses}")


if __name__ == "__main__":
    house_object = Houses(3, 5)
    house_object.house_iteration()
