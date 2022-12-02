class Employee:
    def __init__(self, first, last, anual_pay):
        self.first = first
        self.last = last
        self.anual_pay = anual_pay

    def pay_rise(self, amount = 5000):
        self.anual_pay += amount


