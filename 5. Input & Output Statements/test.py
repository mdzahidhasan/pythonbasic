from sys import argv 
print(type(argv))
print(argv[3])
print('The number of command line argument values are:', len(argv))
print('The list of command line agruments are:', argv)
print('Print ting all command line arguments one by one:')
for x in argv:
   print(x)


# in command line need to write ( py test.py 10 20 30 40 50)
# Then it will print the indexed value.
# zero index will show test.py 
# ['test.py','10','20','30','40','50'] is a list type,   first index value will be always name of the file.
