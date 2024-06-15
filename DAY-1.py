#!/usr/bin/env python
# coding: utf-8

# ##DAY1

# In[ ]:


time complexcity : amount of time taken by computer to execute the program/application

seacrching 

LINEAR: O(n)
BINARYB SEARCH : O(log(n))

---------------------------------
comes under divide & conquer
merge: (n*log(n))
quick:O(n*log(n))

H.W 
time complexicity


2. applications of python

3.data types in python
int
float
tuple
bool
set
dic
list
str




# In[8]:


def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
a=int(input("Enter the number:"))

result=check_even_odd(a)
print(result)


# In[9]:


#program to find leep year


# In[12]:


def check_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def main():
    year = int(input("Please enter the year to check


# In[15]:


def is_leap_year(year):
    """
    Checks if a year is a leap year.
    """
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            return True
    return False

start = 1850
end = 2024

leap = []

for year in range(start, end + 1):
    if is_leap_year(year):
        leap.append(year)

print("Leap years between 1850 and 2024:", leap)
print("Total number of leap years:", len(leap))


# In[17]:


def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
number = int(input("Enter a number: "))
if is_prime(number):
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")


# In[ ]:


functions
tuples
list
dict()
sets()
5tttt

