alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
n = input()
print("","  ".join(alphabet))
for i in range(len(alphabet)):
    if alphabet[i] in n:
        print("",n.find(alphabet[i]),end=" ")
    else:
        print("-1 ",end="")
