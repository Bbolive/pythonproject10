# File Handling
# ไฟล์ การจัดการ
# คือ การทำงานเก็บไฟล์
# เขียนข้อมูลลงไฟล์ คือ output
# อ่านข้อมูลในไฟล์ คือ Input
# การเปิดไฟล์ write (w) extend (x)/ read (r)

f_iot = open ('IOT1.txt' , 'w' , encoding='utf-8') # ถ้าไม่มีมันจะสร้างไฟล์ใหม่

f_iot.write ('hello na ja')
f_iot.write ('hello naa jaa\n')
f_iot.write ('hello naa jaaa\n')
f_iot.write ('Hi Kub\n')

f_iot.close ( )