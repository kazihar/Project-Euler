product = 1
result = 1
string = ''


with open("13adj.txt") as file:
    for line in file:
        string = string + line

length = len(string)

for i in range(length-12):
    product = 1
    for j in range(0,13):
        product = product * int(string[i+j])

    if(product > result):
        result = product

print(result)
