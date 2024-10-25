# program to show the axioms associated with a vector space.

import numpy as np

v1 = list(map(int, input("Enter the first vector, separated by space: ").split()))
v2 = list(map(int, input("Enter the first vector, separated by space: ").split()))
v3 = list(map(int, input("Enter the first vector, separated by space: ").split()))
k = eval(input("enter a scalar: "))
l = eval(input("enter a scalar: "))

print("Associativity of addition")
print(f"( {v1} + {v2} ) + {v3} = {np.add(np.add(v1,v2),v3)} ")
print(f" {v1} + ( {v2} + {v3} ) = {np.add(v1, np.add(v2, v3))} ")

print("commutativity of addition")
print(f" {v1} + {v2} = {np.add(v1, v2)}")
print(f" {v2} + {v1} = {np.add(v2, v1)}")

print("Identity element of addition")
print(f" {v1} + 0 = {np.add(v1, 0)}")

print("Inverse element of addition")
print(f" {v1} + {np.negative(v1)} = {np.add(v1, np.negative(v1))}")

print("distributivity of scalar multiplication over vector addition")
print(f" {k}({v1} + {v2}) = {np.multiply(k,np.add(v1, v2))} ")
print(f" {k} * {v1} + {k} * {v2} = {np.add(np.multiply(k,v1), np.multiply(k, v2))} ")

print(" Distributivity of scalar multiplication over field addition ")
print(f" ({k} + {l}) {v1} = {np.multiply(np.add(k, l), v1)} ")
print(f" {k} * {v1} + {l} * {v1} = {np.add(np.multiply(k, v1), np.multiply(l,v1))} ")

print("Compatibility of scalar multiplication with field multiplication ")
print(f" {k} ( {l} * {v1} ) = {np.multiply(k, np.multiply(l, v1))}")
print(f" {k} * {l} *( {v1} ) = {np.multiply(k*l, v1)}")

print("Identity element of scalar multiplication")
print(f" {v1} * 1 = {np.multiply(v1,1)}")
