# Exception Handling 
# ข้อผิดพลาด การจัดการ
# Exception ข้อผิดพลาดที่เกิดขึ้นตอนโปรแกรมทำงาน
# try Exception finally 

try :
    num1 = int( input('ป้อนตัวเลขที่1 : ') )
    num2 = int( input('ป้อนตัวเลขที่2 : ') ) 

    sum = num1 + num2
    result = num1 / num2

    print(f'ผลรวมของ {num1} + {num2} คือ {sum}')
    print(f'ผลรวมของ {num1} / {num2} คือ {result}')
except ValueError :
    print('ป้อนตัวเลขเท่านั้นห้ามตัวอักษร....สงสัยติดต่อ IT')
except ZeroDivisionError :
    print('ป้อนตัวเลขตัวที่2 ห้ามเป็น 0....สงสัยติดต่อ Admin')
except Exception :
    print('มีข้อผิดพลาดเกิดขึ้น ติดต่อIT')
finally :
    print('Hi...')
    print('Hello...')
    