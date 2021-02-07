def add(*args):
    return sum(args)

total=add(10,20,30,40)
print(total)

#**kwars

def print_data(**kwars):
    print(kwars)

print_data(name="Rizniya",workplace="kakkanad",home="Thrissur")
