f=open("write.txt","w")
names=["abc","def","hij"]

for name in names:
    f.write(name+"\n")


#append

f=open("write.txt","a")
names=["abc","def","hij"]

for name in names:
    f.write(name+"\n")
