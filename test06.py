# ใส่ end='' จะไม่ขึ้นบรรทัดใหม่
f_iot = open ('IOT5.txt' , 'r' , encoding='utf-8')

data = f_iot.readline( )
print(data, end='') 
data = f_iot.readline( )
print(data, end='')
data = f_iot.readline( )
print(data, end='')
data = f_iot.readline( )
print(data, end='')

f_iot.close( )