import unittest #引进测试模块
from name_function import get_formated_name #引入要测试的函数

class NameTestCase(unittest.TestCase): #继承一下TestCase
    def test_full_name(self):
        full_name = get_formated_name('VALADIMIR', "PUTIN")
        self.assertEqual(full_name, "Valadimir Putin")

if __name__ == "__main__":# __name__ 是特殊变量名，表示python脚本，__main__ 表示在主程序， 如果引入则是module名。
    unittest.main() # 运行测试。
