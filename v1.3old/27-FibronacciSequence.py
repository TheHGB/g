limit = raw_input("Enter the upper limit of the sequence you want to print: ")

sequence = 1
previous = 1
print sequence
while sequence <= int(limit):
    print sequence
    aux = previous + sequence
    previous = sequence
    sequence = aux
