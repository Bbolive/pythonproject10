# ลบไฟล์ต้องใช้ 
import os 

if os.path.exists('IOTxxx.txt') :
    os.remove('IOTxxx.txt')
else :
    print('File not found.......')