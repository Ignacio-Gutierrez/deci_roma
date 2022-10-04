def convert_decimal_to_roman(decimal_number):
    roman4 = ''
    roman1 = ''
    roman2 = ''
    roman3 = ''
    decimal_number_units = (decimal_number%10)
    decimal_number_tens = (decimal_number%100-decimal_number%10)//10
    decimal_number_hundreds = (decimal_number%1000-decimal_number%100)//100
    decimal_number_thousand = (decimal_number%10000-decimal_number%1000)//1000

    if decimal_number:

        for digit in range(decimal_number_thousand):
            if decimal_number_thousand < 4:
                roman4 += 'M'

        for digit in range(decimal_number_hundreds):
            if decimal_number_hundreds < 4:
                roman1 += 'C'
            elif decimal_number_hundreds == 4:
                roman1 = 'CD'
            elif  4 < decimal_number_hundreds < 9:
                roman1 = 'C'*(decimal_number_hundreds - 5)
                roman1 = 'D' + roman1
            elif decimal_number_hundreds == 9:
                roman1 = 'CM'

        for digit in range(decimal_number_tens):
            if decimal_number_tens < 4:
                roman2 += 'X'
            elif decimal_number_tens == 4:
                roman2 = 'XL'
            elif  4 < decimal_number_tens < 9:
                roman2 = 'X'*(decimal_number_tens - 5)
                roman2 = 'L' + roman2
            elif decimal_number_tens == 9:
                roman2 = 'XC'

        for digit in range(decimal_number_units):
            if decimal_number_units < 4:
                roman3 += 'I'
            elif decimal_number_units == 4:
                roman3 = 'IV'
            elif  4 < decimal_number_units < 9:
                roman3 = 'I'*(decimal_number_units - 5)
                roman3 = 'V' + roman3
            elif decimal_number_units == 9:
                roman3 = 'IX'

    roman = roman4 + roman1 + roman2 + roman3

    return roman
