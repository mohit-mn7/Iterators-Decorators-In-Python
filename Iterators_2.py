def generator_function(n):
    i = 1
    while True:
        if i < n:
            yield i
            i += 1
        else:
            print('Finished Execution')
            break

x = generator_function(11)

for num in x:
    print(num)
