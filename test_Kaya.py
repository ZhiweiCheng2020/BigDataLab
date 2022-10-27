import unittest
from Kaya import kaya_identity

class TestKaya(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual(kaya_identity(1,2,1,1).cal_kaya_identity(), 2.00)
        self.assertEqual(kaya_identity(82.4,44,5,0.05).cal_kaya_identity(), 906.40)
        # self.assertEqual(kaya_identity("-82.4",44,5,0.05).cal_kaya_identity(), 906.40)
        # self.assertEqual(kaya_identity(-82.4,44,5,0.05).cal_kaya_identity(), 906.40)

if __name__ == '__main__':
    unittest.main()