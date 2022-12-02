import unittest
from Employee import Employee

class TestEmployeeCase(unittest.TestCase):
    def setUp(self):
        self.my_employee = Employee("Chao", "Jiang", 50000)

    def give_default_rise(self):
        self.my_employee.pay_rise()
        self.assertEqual(self.my_employee.anual_pay, 55000)

    def give_exact_amount(self):
        self.my_employee.pay_rise(10000)
        self.assertEqual(self.my_employee.anual_pay, 60000)

if __name__ == "__main__":
    unittest.main()
