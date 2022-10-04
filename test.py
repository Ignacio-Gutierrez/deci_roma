from main import convert_decimal_to_roman

import unittest

class TestDecimalToRoman(unittest.TestCase):

    def test_1(self):
        roman_number = convert_decimal_to_roman(1)
        self.assertEqual(roman_number, 'I')

    def test_2(self):
        roman_number = convert_decimal_to_roman(2)
        self.assertEqual(roman_number, 'II')

    def test_3(self):
        roman_number = convert_decimal_to_roman(3)
        self.assertEqual(roman_number, "III")

    def test_5(self):
        roman_number = convert_decimal_to_roman(5)
        self.assertEqual(roman_number, "V")

    def test_6(self):
        roman_number = convert_decimal_to_roman(6)
        self.assertEqual(roman_number, "VI")
    
    def test_9(self):
        roman_number = convert_decimal_to_roman(9)
        self.assertEqual(roman_number, "IX")

    def test_10(self):
        roman_number = convert_decimal_to_roman(10)
        self.assertEqual(roman_number, "X")

    def test_11(self):
        roman_number = convert_decimal_to_roman(11)
        self.assertEqual(roman_number, "XI")

    def test_12(self):
        roman_number = convert_decimal_to_roman(12)
        self.assertEqual(roman_number, "XII")

    def test_18(self):
        roman_number = convert_decimal_to_roman(18)
        self.assertEqual(roman_number, "XVIII")

    def test_19(self):
        roman_number = convert_decimal_to_roman(19)
        self.assertEqual(roman_number, "XIX")

    def test_20(self):
        roman_number = convert_decimal_to_roman(20)
        self.assertEqual(roman_number, "XX")

    def test_21(self):
        roman_number = convert_decimal_to_roman(21)
        self.assertEqual(roman_number, "XXI")

    def test_23(self):
        roman_number = convert_decimal_to_roman(23)
        self.assertEqual(roman_number, "XXIII")

    def test_30(self):
        roman_number = convert_decimal_to_roman(30)
        self.assertEqual(roman_number, "XXX")

    def test_35(self):
        roman_number = convert_decimal_to_roman(35)
        self.assertEqual(roman_number, "XXXV")

    def test_38(self):
        roman_number = convert_decimal_to_roman(38)
        self.assertEqual(roman_number, "XXXVIII")

    def test_40(self):
        roman_number = convert_decimal_to_roman(40)
        self.assertEqual(roman_number, "XL")
    
    def test_46(self):
        roman_number = convert_decimal_to_roman(46)
        self.assertEqual(roman_number, "XLVI")

    def test_53(self):
        roman_number = convert_decimal_to_roman(53)
        self.assertEqual(roman_number, "LIII")

    def test_67(self):
        roman_number = convert_decimal_to_roman(67)
        self.assertEqual(roman_number, "LXVII")
    
    def test_70(self):
        roman_number = convert_decimal_to_roman(70)
        self.assertEqual(roman_number, "LXX")

    def test_81(self):
        roman_number = convert_decimal_to_roman(81)
        self.assertEqual(roman_number, "LXXXI")
    
    def test_99(self):
        roman_number = convert_decimal_to_roman(99)
        self.assertEqual(roman_number, "XCIX")
    
    def test_100(self):
        roman_number = convert_decimal_to_roman(100)
        self.assertEqual(roman_number, "C")

    def test_101(self):
        roman_number = convert_decimal_to_roman(101)
        self.assertEqual(roman_number, "CI")

    def test_456(self):
        roman_number = convert_decimal_to_roman(456)
        self.assertEqual(roman_number, "CDLVI")

    def test_500(self):
        roman_number = convert_decimal_to_roman(500)
        self.assertEqual(roman_number, "D")

    def test_504(self):
        roman_number = convert_decimal_to_roman(504)
        self.assertEqual(roman_number, "DIV")

    def test_693(self):
        roman_number = convert_decimal_to_roman(693)
        self.assertEqual(roman_number, "DCXCIII")

    def test_748(self):
        roman_number = convert_decimal_to_roman(748)
        self.assertEqual(roman_number, "DCCXLVIII")

    def test_825(self):
        roman_number = convert_decimal_to_roman(825)
        self.assertEqual(roman_number, "DCCCXXV")

    def test_999(self):
        roman_number = convert_decimal_to_roman(999)
        self.assertEqual(roman_number, "CMXCIX")

    def test_1999(self):
        roman_number = convert_decimal_to_roman(1999)
        self.assertEqual(roman_number, "MCMXCIX")

    def test_2999(self):
        roman_number = convert_decimal_to_roman(2999)
        self.assertEqual(roman_number, "MMCMXCIX")

    def test_3999(self):
        roman_number = convert_decimal_to_roman(3999)
        self.assertEqual(roman_number, "MMMCMXCIX")

if __name__ == '__main__':
    unittest.main()
