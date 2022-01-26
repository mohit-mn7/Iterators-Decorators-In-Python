num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in num_list:
    print(num*num)

for num in range(1, 11):
    print(num*num) 

x = range(1, 11)

print("Printing x: ",x)

print("Type Of x: ", type(x))

print("List of the attributes and methods of object x:", dir(x))

x = range(1, 11)

iter_obj = x.__iter__()

print("Iterator Object: ", iter_obj)

print("Value of Iterator: ", iter_obj.__next__())
print("Value of Iterator: ", iter_obj.__next__())
print("Value of Iterator: ", iter_obj.__next__())

while True:
    try:
        print("Value of Iterator: ", iter_obj.__next__())
    except StopIteration:
        print("Exception Caught! Breaking the Loop")
        break