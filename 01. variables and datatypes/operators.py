"""
    PYTHON OPERATORS ARE AS FOLLOWS: 
    - Arithmetic operators
        - Addition (x + y)
        - Subtraction (x - y)
        - Multiplication (x * y)
        - Division (x / y)
        - Floor division (x // y)
        - Modulus (x % y)
        - Exponentiation (x ** y)
    - Assignment operators
        - equal siqn (=) , +=	,-=	,*=	,/=	,%=	,//= ,**= , &=	, |= ,^= , >>= , <<=
    - Comparison operators
        - Equal (x == y)
        - Not equal (x != y	)
        - Greater than (x > y)
        - Less than (x < y	)
        - Greater than or equal to (x >= y	)
        - Less than or equal to (x <= y)
    - Logical operators
        - and (Returns True if both statements are true)
        - or (Returns True if one of the statements is true)
        - not (Reverse the result, returns False if the result is true)
    - Identity operators
        - is 	(Returns True if both variables are the same object	x is y)	 
        - is not	(Returns True if both variables are not the same object	x is not y)
        - NOTE: Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
    - Membership operators
        - in (Returns True if a sequence with the specified value is present in the object) 	
        - not in (Returns True if a sequence with the specified value is not present in the object)
    - Bitwise operators
        - AND (Sets each bit to 1 if both bits are 1) - & 
        - OR (Sets each bit to 1 if one of two bits is 1) - | 
        - XOR (Sets each bit to 1 if only one of two bits is 1) - ^ 
        - NOT (Inverts all the bits) - ~ 
        - Zero fill left shift (Shift left by pushing zeros in from the right and let the leftmost bits fall off) - <<
        - Signed right shift (Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off) - >> 
"""
 
   


#bitwise example
# decimal_number = 22

# _22_in_16_bin = format(22, '016b')  
# _14_in_16_bin = format(14, '016b')  

# print(_22_in_16_bin)
# print(_14_in_16_bin)

# results = 22 & 14; 
# print(results) 
# print(format(results, '016b')) 

print(3 >> 2)
# print(format(3, '016b')) 
# print(format(12, '016b')) 

# x =  ("apple", "banana", "cherry")	
# y =  ("apple", "banana", "cherry")	
# print(x is y)
