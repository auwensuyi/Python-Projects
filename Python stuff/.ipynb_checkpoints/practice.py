#Will be creating several notebooks
print("Getting started")
#placeholder
x = 6
y = 7
z = x + y
v = x - y
t = x * y
print(z)
print(v)
print(t)

a = 100 
b = 25

c = a/b
d = a%b
print(c)
print(d)

def ticket(age, ticket_type):
    if age < 65 and ticket_type == "10-ride":
        return int(38)
    if age < 65 and ticket_type == "standard":
        return float(159.5)
    if age >= 65 and ticket_type == "10-ride":
        return float(34.2)
    if age >= 65 and ticket_type == "elderly":
        return float(143.55)