file=open("海南省所有镇的经纬度.txt","r")
lines=file.readlines()
list=[]
listline=[]
longitude=[]
latitude=[]
for line in lines:
    listline=line.split(',')
    listline[1]=eval(listline[1])
    listline[2]=eval(listline[2])
    list.append(listline)
file.close()
#print(list)
for i in range(len(list)):
    longitude.append(list[i][1])
    latitude.append(list[i][2])
print("经度最大值：",max(longitude))
print("经度最小值：",min(longitude))
print("经度差：",max(longitude)-min(longitude))
print("纬度最大值：",max(latitude))
print("纬度最小值：",min(latitude))
print("纬度差：",max(latitude)-min(latitude))
"""
经度最大值： 110.8736325
经度最小值： 108.640365
经度差： 2.2332674999999966
纬度最大值： 20.0273831
纬度最小值： 18.27324925
纬度差： 1.7541338500000023
"""