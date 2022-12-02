import unittest
from city_functions import format_place

class CityTestCase(unittest.TestCase):#继承一下测试父类
    def testcity(self):
        reality = format_place("SHANGHAI", "china")
        self.assertEqual(reality, "Shanghai, China")

if __name__ == "__main__":
    unittest.main()
