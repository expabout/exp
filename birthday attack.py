from gmssl import sm3, func
import random

def str_to_byte(str):  # 字符串转换成byte
    ml = len(str)
    msg_byte = []
    msg_bytearray = str.encode('utf-8')
    for i in range(ml):
        msg_byte.append(msg_bytearray[i])
    return msg_byte

def byte_to_str(byte):  # byte转字符串
    ml = len(byte)
    str1 = b""
    for i in range(ml):
        str1 += b'%c' % byte[i]
    return str1.decode('utf-8')

for j in range(0,1000):
    for i in range(0,2**16):
        x = str_to_byte(str(random.randint(0,2**256)))
        y = str_to_byte(str(random.randint(0,2**256)))

        x_EN = sm3.sm3_hash(func.bytes_to_list(x))
        y_EN = sm3.sm3_hash(func.bytes_to_list(y))

        if(x_EN[0:8] ==y_EN[0:8]):
            print("True")
            print(x),print(y)
    print("计数器:",j)
