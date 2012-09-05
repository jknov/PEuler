#!/usr/bin/python
from math import sqrt

# Utilites to solve some Project Euler's problems

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


# Converts a into a list in which
# the i-th element is the i-th digit in its
# base b representation
def toList(a,b):
   A = []
   while a > 0:
      A.append(a%b)
      a = a / b
   return A

# Decides wheter a is a palindrome when
# represented in base 10
def isPalindrome(a):
   A = toList(a,10)
   for i in range(0,int(len(A)/2)):
      if A[i] != A[-(i+1)]:
         return False
   return True

# Decides wheter (a,b,c) is pythagorean
# triplet or not
def isPythagorean(a,b,c):
   return (a*a)+(b*b) == (c*c)

# Returns the all primes of size at most n
def primeSieve(n):
   A = range(2,n+1)
   P = []
   while len(A) > 0:
      p = A[0]
      P.append(p)
      for i in A:
         if i % p == 0:
            A.remove(i)
   return P
         
      
   