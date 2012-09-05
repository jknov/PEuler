#!/usr/bin/python

import math
Import EulerUtil

# Problem 1: Add all the natural numbers below x that are multiples of 3 or 5.
# Very naive solution, though.
def problem1(x):
   sum = 0
   i = 5
   while i < x:
      sum += i
      i += 5
   i = 3
   while i < x:
      if i % 5 != 0:
         sum += i
      i += 3
   return sum

# Problem 2: By considering the terms in the Fibonacci sequence whose values do not 
# exceed x, find the sum of the even-valued terms.
def problem2(x):
   prev  = 1
   pprev = 0
   sum = 0
   while prev <= x:
      if prev % 2 == 0:
         sum += prev
      prev += pprev
      pprev = prev - pprev
   return sum

# Problem 3: What is the largest prime factor of the number x?
def problem3(x):
   r = int(math.sqrt(x))
   for i in range(r,1,-1):
      if x % i == 0:
         if EulerUtil.isPrime(i):
            return i

# Problem 4: A palindromic number reads the same both ways. The largest palindrome 
# made from the product of two 2-digit numbers is 9009 = 91*99.
#
# Find the largest palindrome made from the product of two d-digit numbers.
def problem4(d):
   st = 10**d -1
   lo = 10**(d-1)
   maxm = lo*lo
   i = st
   j = st
   while i > lo:
      while i*j > maxm:
         if EulerUtil.isPalindrome(i*j):
            maxm = i*j
            lo = j
         j -= 1
      i -= 1
      j = i
   return maxm
      

# Problem 5: What is the smallest positive number that is evenly 
# divisible by all of the numbers from i to n?
def problem5(i,n):
   prod = 1
   if i == 1: i += 1
   for x in range(i,n):
      if EulerUtil.isPrime(x):
         p = x
         while p*x < n:
            p *= x
         prod *= p
   return prod

# Problem 6: Find the difference between the sum of the squares of 
# the first n natural numbers and the square of the sum.
def problem6(n):
   sums  = (n*(n+1))/2
   sumsq = sums*(((2*n)+1)/3)
   return (sums*sums) - sumsq

# Problem 7: What is the n-st prime number?
def problem7(n):
   pcount = 6
   last = 13
   i = 7
   while pcount < n:
      if EulerUtil.isPrime((2*i)+1):
         last = (2*i)+1
         pcount += 1
      i += 1
   return last

# Problem 8: Find the greatest product of five consecutive digits 
# in the large number written in file x, the one for this problem is the one named number.
def problem8(x):
   f = open(x,"r")
   L = f.readline()
   N = ''
   while L:
      if L[-1] == '\n':
         N = N + L[:-1]
      else:
         N = N + L
      L = f.readline()
   X = []
   for i in N:
      X.append(int(i))
   cont = 0
   maxm = 0
   p = 1
   for i in range(0,len(X)):
      if X[i] != 0:
         if cont == 5:
            p = (p*X[i])/X[i-5]
         else:
            p = p*X[i]
            cont += 1
         if cont == 5 and p > maxm:
            maxm = p
      else:
         cont = 0
         p = 1
   return maxm

# Problem 9: (a,b,c) is a Pythagorean triplet if a^2+b^2=c^2 
# find a Pythagorean triplet such that a + b + c = x. Return the product abc.
def problem9(x):
   least = x/3
   for c in range(least,x):
      for a in range(1,(c/2)+1):
         b = x - (a+c)
         if EulerUtil.isPythagorean(a,b,c):
            return a*b*c
   return 0

# Problem 10: Find the sum of all the primes below x.
# Very naive, though :(
def problem10(x):
   sum = 2
   for i in range(1,x/2):
      if EulerUtil.isPrime(2*i+1):
         sum += 2*i+1
   return sum









