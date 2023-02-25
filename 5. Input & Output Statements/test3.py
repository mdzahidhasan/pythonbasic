from sys import argv
b=argv[1:]
sum=0
for x in b:
    sum=sum+int(x)  # as we know all inputs are str format so we should convert commandline inputs to int type 
    print('The sum is', sum)