# File Handling
# ไฟล์ การจัดการ
# คือ การทำงานเก็บไฟล์
# การเปิดไฟล์ write (w) extend (x)/ read (r)

try :
    f_iot = open ('IOT3.txt' , 'x' , encoding='utf-8') # ถ้าไม่มีมันจะสร้างไฟล์ใหม่

    f_iot.write ('hello na ja')
    f_iot.write ('hello naa jaa\n')
    f_iot.write ('hello naa jaaa\n')
    f_iot.write ('Hi Kub\n')

    f_iot.close ( )
except FileExistsError :
    print('กรุณาเปลี่ยนชื่อไฟล์ เพราะซ้ำ.......')