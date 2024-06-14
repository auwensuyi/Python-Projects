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
    
    def convert_2_km():
        distance = True
        while distance:
            user = input("Miles (or STOP):")
            try:
                miles = float(user)
                if miles < 0:
                    print("Bad input:" + str(miles))
                if miles >= 0:
                    miles = miles*(1.60934)
                    print("Kilometers:" + str(miles))
            except ValueError:
                try:
                    miles = str(user)
                    if miles != 'STOP':
                        print("Bad input:" + str(miles))
                    if miles == 'STOP':
                        return
                except ValueError:
                    return
        
        

def meal_price(items):
    item = []
    price = 0
    for item in items:
        if item == 'apple':
            price += 0.59
        elif item == 'burger':
            price += 2.50
        elif item == 'drink':
            price += 0.99
        elif item == 'fries':
            price += 1.29
        else:
            print('Unknown item: ' + item)

    return price
            
    


def print_change(row):
    x = []
    for i in range(1, len(row)):
        x.append(row[i] - row[i-1])
    print(*x, sep=",")
    