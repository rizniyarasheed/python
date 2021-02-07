f=open("movies.csv","r")

dict={}

for lines in f:
    data=lines.rstrip("\n").split(",")
    #movie name,year,relese

    movie=data[1]
    year=data[2]
    relese_count=data[4]

    print(data[1])

    if(year not in dict):
        dict[year]=relese_count

    else:
        #dict[relese_count]=relese_count
        dict[year] =relese_count


for k,v in dict.items():
    print(k,v)



res=sorted(dict,key=dict.get,reverse=True)
print(res[0],dict[res[0]])