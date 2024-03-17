# simple interest
p = 8
r = 4
t = 5

b = r/100
a = b * t
c = 1 + a
simple_interest = p * c
print("simple_interest")

#compound interest
p = 8
n = 4
t = 5
r = 4

w = r/n
x = 1 + w
y = x ** (n * t)
compound_interest = p * y
print("compound_interest")

#annuity plan
p = 8
n = 4
t = 5
r = 4
pmt = 6

l = r/n
m = 1 + l
n = m ** (n * t)
o = n - 1
p = o/l
annuity_plan = pmt * p
print("annuity_plan")