# class is a prototype blueprint for instance/object

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"\n{self.name} is sitting down")

    def roll(self):
        print(f"\n{self.name} is rolling over")

lili = Cat('Lili', 3)

print(lili.name)
print(lili.age)

lili.name
lili.age

lili.sit()
lili.roll()

# 使用类

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 #添加一个里程表属性，默认值0

    def get_long_name(self):
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()

    def read_odometer(self):
        print(f"\nThe car has been running for {self.odometer_reading}")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you cannot roll back odometer !")
    def increment_odometer(self, miles):
        self.odometer_reading += miles

my_car = Car("Audi", "A8", 2022)

print(my_car.get_long_name())

cname = my_car.get_long_name()
print(cname)

my_car.read_odometer()

my_car.update_odometer(10086)
my_car.update_odometer(1006)

my_car.read_odometer()

my_car.increment_odometer(100)
my_car.read_odometer()


my_car.increment_odometer(100)
my_car.read_odometer()


# Inheritence
class EV(Car):
    def __init__(self, make, model, year): #初始化父类属性
        super().__init__(make, model, year)# super()函数调用父类方法
        self.battery_size = 76

    def describe_battery(self):
        print(f"\n{self.make} {self.model} {self.year} has a battery of size {self.battery_size}")

my_ev = EV("Wuling", "Mini EV", 2022)

print(my_ev.get_long_name())
my_ev.read_odometer()

my_ev.describe_battery()

