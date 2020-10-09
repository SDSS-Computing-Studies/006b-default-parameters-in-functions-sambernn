#!python3

""" 
example that shows how we can create our own module.
We have another file in this directory called cats.py
This means we can import the module cats using:

import cats

Any functions in that cats.py file can be used now, but
since they're in the cats.py file, we have to include
"cats." in front of the function name.

cats.py defines the following functions:
plusOne( integer )
timesTwo( float )
zeroMyHero( float )

so we can make use of

cats.plusOne()
cats.timesTwo()
cats.zeroMyHero()

Note that when you create your own module, you generally only put
function definitions, or variables but no other commands

functions in a module are also called METHODS
and variabes in a module are called PROPERTIES
"""
import cats

print( cats.plusOne(3) )
print( cats.timesTwo(4.3) )
print( cats.zeroMyHero("green"))
print( cats.black )
print( cats.tabby)