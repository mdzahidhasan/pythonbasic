from sys import argv


print(type(argv))
print(argv[0])
print(argv[1])
print(argv[3])
print(len(argv))
for x in argv:
    print(x)

