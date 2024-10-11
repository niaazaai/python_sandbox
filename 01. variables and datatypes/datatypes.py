"""
    Text Type:	str
    Numeric Types:	int, float, complex
    Sequence Types:	list, tuple, range
    Mapping Type:	dict
    Set Types:	set, frozenset
    Boolean Type:	bool
    Binary Types:	bytes, bytearray, memoryview
    None Type:	NoneType
"""
  
# note: explore more string datatypes 
string_ = "Hello World"	 # has it is own functions '' - "" - len(string_)
string__ = '''
    lorem ipsum dolor
    lorem ipsum dolor
    lorem ipsum dolor
'''

int_ = 20	
float_ = 20.5		
complex_ = 1j	
list_ = ["apple", "banana", "cherry"]		
tuple_ = ("apple", "banana", "cherry")		
dict_ = {"name" : "John", "age" : 36}		
set_ = {"apple", "banana", "cherry"}	
froozen_ = frozenset({"apple", "banana", "cherry"})		
bool_ = True		
bytes_ = b"Hello"		
memo_ = memoryview(bytes(5))		
none_ = None


# We can use constructor functions to cast types
x = str("Hello World")		
x = int(20)		
x = float(20.5)		
x = complex(1j)		
x = list(("apple", "banana", "cherry"))		
x = tuple(("apple", "banana", "cherry"))		
x = dict(name="John", age=36)		
x = set(("apple", "banana", "cherry"))		
x = frozenset(("apple", "banana", "cherry"))		
x = bool(5)		
x = bytes(5)		
x = memoryview(bytes(5))


x  = '10'

print(int(x))

