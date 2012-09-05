#!/usr/bin/python
from math import sqrt

# Computes the greatest common divisor
# of a and b.
def GCD(a, b):
   if a < b:
      t = b
      b = a
      a = t
   while b != 0:
      t = b
      b = a % b
      a = t
   return a

# Computes the least common multiple
# of a and b.
def LCM(a, b):
   i = 1
   if a < b:
      t = b
      b = a
      a = t
   while ((a*i) % b) != 0:
      i = i + 1
   return a*i

# Decides wether a is prime or not.
def isPrime(a):
   for x in range(2,int(sqrt(a))+1):
      if a % x == 0:
         return False
   return True

# A class that allows to represent a rational
# number by its numerator and denominatior
# instead as a single float or double, this
# avoids common precision errors that arise by
# representing it as a float or as a double.
class Rational:
   # It recieves the numerator and denominator
   # default numerator is 1 (is an integer).
   def __init__(self, pnum, pden = 1):
      self.num = pnum
      self.den = pden
      self.string = ''
      self.minExp()
   
   # Returns the result of adding x to itself
   def sum(self, x):
      c = LCM(self.den,x.den)
      sNum = (self.num * (c/self.den)) + (x.num * (c/x.den))
      r = Rational(sNum,c)
      r.minExp()
      return r
      
   # Add x to itself
   def sumSelf(self, x):
      c = LCM(self.den,x.den)
      self.num = (self.num * (c/self.den)) + (x.num * (c/x.den))
      self.den = c
      self.minExp()
   
   # Converts numerator and numerator
   # to its minimal expresion.
   def minExp(self):
      c = GCD(self.num,self.den)
      self.num = self.num / c
      self.den = self.den / c
      self.string = self.toString()
   
   # Returns its value as a floating point
   # number.
   def toDouble(self):
      return self.num/self.den
   
   # Returns its floor.
   def toInt(self):
      return int(self.toDouble())
   
   # Prints itself as "num/den"
   def printR(self):
      print self.string
   
   def toString(self):
      return '%(n)d/%(d)d' % {"n": self.num, "d": self.den}
      
   def toLaTex(self):
      return '\frac{%(n)d}{%(d)d}' % {"n": self.num, "d": self.den}
