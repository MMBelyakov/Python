#ints

number = 123412341
print( number )

string = "123412341"
number = int( string )
print( number + 5 )



number_as_string = "15"
int( number_as_string )

#bools

bool1 = True
bool2 = False

print( bool1 , bool2 )

#floats
a = 5.3
b = 3.17823
print( a + b )

#dynamic_type

var = ' I am a string'
print(var)
print( type(var) )

print()

var = 42
print(var)
print( type(var) )

print()

a = 5
b = 23
print(a + b)

#arithmetic operations
x = 2

y = 8

result =  x + y
print(result)
print( x + y )
print( x + 3 )
print( x - y )
print()
print( x * y )
print( x / y )
print( x // y )
print( x % y )

print()

print( x ** y )
print( x ** 0.5 )
print( pow(x,y) )

print()

z = -2
print( abs(z) )
print( z ** 2 )

print()

print( 3.2 * 0.8 -2 * 5 - 3 ** 3 )

print()

number=3.26
print( round(number),round( number,1 ) )

#math_operations

import math
x=3.265
print( 'x=',x )
print( 'trunc(x) = ',math.trunc(x) )
print( 'floor(x) = ',math.floor(x) )
print( 'ceil(x) = ' ,math.ceil(x) )

print( math.pi )
print( math.e )

print( math.sin(math.pi / 4) )

print( 1/ math.sqrt(2) )

#strings

string1 =  "String"
string2 = 'String'
print( string1,string2 )

string = "First line of text. \n"\
          "Second line of text."
print( string )

multiline_string = """Some data types
-int
-float
-bool
-complex
-str
"""
print( multiline_string )

#print_examples

print( 2 , 3 , 4 , sep=' ,' )
print( 'he','llo',sep='' )
print( '1',end=' ' )
print( '2',end = '\n \n' )
print( 'he',end='' )
print( 'llo' )

#input_examples
string = input('Enter a string:')
print( 'You have entered "{}"' .format( string ) )
print( 'Press Enter to continue' )
input()

m = int (input('First number: '))
n = int (input('Second number: '))
print  ( '{} + {} = {}'.format( m,n,m+n ) )





