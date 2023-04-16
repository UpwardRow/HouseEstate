import time


class Houses:

    def __init__(self, income, no_of_houses, waste):
        self.income = income
        self.no_of_houses = no_of_houses
        self.rubbish = waste

    def __repr__(self):
        return f"income: {self.income}, no_of_houses: {self.no_of_houses}, waste: {self.rubbish}"

    def house_iteration(self):
        while True:

            flag = False

            while self.rubbish != 35 and flag is not True:

                self.income += 1
                self.rubbish += 0.5

                print(f"The estate's income is: {self.income},"
                      f" the number of houses is {self.no_of_houses},"
                      f" and the waste buildup is {self.rubbish}")
                time.sleep(1)
                if self.income % 10 == 0:
                    self.no_of_houses += 1
                    flag = True

            if self.rubbish == 35:
                print("Rubbish overflow!")
                time.sleep(2)


if __name__ == "__main__":
    house_object = Houses(3, 5, 30)
    house_object.house_iteration()
