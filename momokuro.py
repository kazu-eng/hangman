# momokuro dic made by kkihara

# this is comment using #

for i in range(5):
    print("We are!")

# dictionary of momokuro members
momokuro =\
         {"red":"Kanako", "yellow":"Siori","pink":"Ayaka","purple":"Reni","green":"Momoka"}
# \ for long long sentence
# added in dictionary
momokuro membersmomokuro["blue"] = "Akari"

print("input your favarite color")

count=0
while (count<5):
    count+=1
    color = input("Input color ")
    if (color in momokuro.keys()):
        break

print("She is "+ momokuro[color])



