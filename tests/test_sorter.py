import unittest
from src.sorter import sort

class TestPackageSorting(unittest.TestCase):
    def test_standard_package(self):
        self.assertEqual(sort(50, 50, 50, 10), "STANDARD")

    def test_bulky_package(self):
        self.assertEqual(sort(160, 50, 50, 10), "SPECIAL")

    def test_heavy_package(self):
        self.assertEqual(sort(50, 50, 50, 25), "SPECIAL")

    def test_rejected_package(self):
        self.assertEqual(sort(200, 200, 200, 25), "REJECTED")

    def test_edge_case_volume(self):
        self.assertEqual(sort(100, 100, 100, 10), "SPECIAL")  # Exactly 1,000,000 cm³

    def test_edge_case_dimension(self):
        self.assertEqual(sort(150, 50, 50, 10), "SPECIAL")  # Exactly 150 cm in one dimension

    def test_edge_case_mass(self):
        self.assertEqual(sort(50, 50, 50, 20), "SPECIAL")  # Exactly 20 kg

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            sort(-50, 50, 50, 10)

if __name__ == "__main__":
    unittest.main()
