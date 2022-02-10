import os

import display
os.mkdir("trainer")
os.mkdir("dataset")
print("Would you like to train a new user \n if so input the number of users \n if not input 0")
users = 0
newusers = input()
f = open("ids.csv","w")
f.close
f= open("ids.csv")
lines = f.readlines()
names = []
ids = []
for line in lines:
    print(line)
    x = line.split(",")
    names.append(x[1])
    ids.append(int(x[0]))
print(names)
print(ids)
f = open("ids.csv", "a")
origlen = len(ids)
for user in range(0,int(newusers)):
    print("input user "+str(user)+"'s name")
    temp = input()
    f.write(str(len(ids)) + "," + temp + "\n")
    ids.append(len(ids))
    names.append(temp)
    print("user "+str(user)+" please sit in front of the screen")
    print("is this a main user y/n")
    if input()=='y':
        display.makedataset(origlen + user, 200)
    else:
        display.makedataset(origlen + user, 50)

    print("next user please")
display.training()
display.execlaststep(names)



