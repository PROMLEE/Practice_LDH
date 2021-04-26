def pickup_even(a):
    result = []
    for i in a:
        if i%2 == 0:
            result.append(i)
    return result

a = [3,4,5,6,7]
b = pickup_even(a)
print(b)
