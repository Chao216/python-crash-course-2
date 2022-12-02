import unittest
from name_function import get_formated_name

class NameTestCase(unittest.TestCase):
    def test_full_name(self):
        full_name = get_formated_name('VALADIMIR', "PUTIN")
        self.assertEqual(full_name, "Valadimir Putin")

if __name__ == "__main__":
    unittest.main()
