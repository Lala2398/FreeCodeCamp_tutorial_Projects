'''
The Luhn algorithm (also known as the modulus 10 or mod 10 algorithm) is a simple checksum formula used to validate a variety of identification numbers, most commonly credit card numbers. 
It was created by IBM scientist Hans Peter Luhn in 1954.
Purpose of the Luhn Algorithm

The algorithm is used to detect accidental errors in numeric sequences, such as mistyped digits, and to verify the validity of numbers like:

    Credit card numbers
    Bank account numbers
    IMEI numbers (used in mobile devices)
    Canadian Social Insurance Numbers

The Luhn algorithm is not a cryptographically secure method but is widely used for quick validation:

    In credit card payments, the Luhn check is used before transmitting numbers to a payment processor.
    In registration forms or online purchases, it detects invalid card numbers early, reducing processing load.
  

    Example: Validating a Credit Card Number

Let’s validate the credit card number: 4539 1488 0343 6467

    Reverse the number:
    7 6 4 6 3 4 3 0 8 8 4 1 9 5 3 4

    Double every second digit:
        Original: 7, 6, 4, 6, 3, 4, 3, 0, 8, 8, 4, 1, 9, 5, 3, 4
        Doubled: 7, 12, 4, 12, 3, 8, 3, 0, 16, 8, 8, 1, 18, 5, 6, 4

    Subtract 9 from numbers > 9 (or add the digits):
        Adjusted: 7, 3, 4, 3, 3, 8, 3, 0, 7, 8, 8, 1, 9, 5, 6, 4

    Sum all digits:
        Sum = 7 + 3 + 4 + 3 + 3 + 8 + 3 + 0 + 7 + 8 + 8 + 1 + 9 + 5 + 6 + 4 = 80

    Check modulo 10:
        80 % 10 = 0

Since the result is 0, the card number is valid.

'''



def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number
    total = sum_of_odd_digits + sum_of_even_digits
    #print(total)
    return total % 10 == 0

def main():
    card_number = '4111-1111-1111-1111'
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')

main()
