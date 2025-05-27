#!/usr/bin/env python
# coding: utf-8

# In[9]:


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

result = []

for num in range(100, 0, -1):
    if is_prime(num):
        result.append("   ")  # Placeholder kosong untuk bilangan prima
    elif num % 15 == 0:
        result.append("FooBar")
    elif num % 3 == 0:
        result.append("Foo")
    elif num % 5 == 0:
        result.append("Bar")
    else:
        result.append(str(num))

# Cetak hasil 10 angka per baris
for i in range(0, len(result), 10):
    print("\t".join(result[i:i+10]))

