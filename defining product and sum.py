#title of the program
multiply_and_add = print('TYPE THE GIVEN 1 NUMBERS:\n')

#defining the given 1 numbers
first = 20 
second = 30

# given 1 numbers 
first_number = input('GIVEN 1 INTEGER : \n')
second_number = input('GIVEN 1 INTEGER : \n')

#total product of given 1 
total_product = first * second 
print ('TOTAL: \n 20 x 30 =', total_product)

#it controls to define if it's less than or equal 1000
if total_product <= 1000:
    print('\nTHE RESULT IS', total_product)

#title of the second given
multiply_and_add_part1 = print('\n\nTYPE THE GIVEN 2 NUMBERS : \n')

#defining the given 2 numbers
first_part1 = 40
second_part1 = 30

#inputting the given 2 integers
first_number_part1 = input('GIVEN 2 INTEGER :\n')
second_number_part1 = input('GIVEN 2 INTEGER :\n')

#total value of given 2 
total_product_part1 = first_part1 * second_part1
print('TOTAL :\n', first_part1, "x" ,second_part1, '=', total_product_part1)

#controls to define if its greater than 1000 to sum it up the given 2 
if total_product_part1 >= 1000:
    total_product_part1 = first_part1 + second_part1
    print('\nTHE RESULT IS', total_product_part1)
