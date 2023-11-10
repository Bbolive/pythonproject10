# File Handling
# ไฟล์ การจัดการ
# คือ การทำงานเก็บไฟล์
# การเปิดไฟล์ write (w) extend (x)/ read (r)

f_iot = open ('IOT5.txt' , 'a' , encoding='utf-8') # ถ้าไม่มีมันจะสร้างไฟล์ใหม่

f_iot.write ('12113134')
f_iot.write ('355355353\n')
f_iot.write ('454434\n')

f_iot.close ( )
