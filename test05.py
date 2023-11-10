
f_iot = open ('IOT5.txt' , 'r' , encoding='utf-8')

data = f_iot.read( )

f_iot.close( )

print(data)