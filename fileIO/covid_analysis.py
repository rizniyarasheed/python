f=open("covid_19_india.csv","r")

dict={}

for line in f:
    data=line.rstrip("\n").split(",")
    #state,confirmed case
    state=data[3].rstrip("***")#kerala
    if(state=="Telengana"):
        state="Telangana"

    confirmed_cases=int(data[8])

    if(state not in dict):
        dict[state]=confirmed_cases
    else:
        dict[state]=confirmed_cases

for k,v in dict.items():
    print(k,"===>",v)

#print highest

res=sorted(dict,key=dict.get,reverse=True)
print(res[0],dict[res[0]])

#alphabetic order

res=sorted(dict)
print(res)

