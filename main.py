from hashlist import *
import hashlib
from sjsc import *
def md5(content=None):
    if content is None:
        return ''
    md5gen = hashlib.md5()
    md5gen.update(content.encode())
    md5code = md5gen.hexdigest()
    md5gen = None
    return md5code





sjlist = csj(100000)
mainjg = hashlist(sjlist)
print(mainjg)
while True:
    a1n = input("请输入名称:")
    a2n = md5(a1n)
    a3n = int(a2n, 16)
    a4n = a3n % len(sjlist)
    a5n = str(a4n)
    if a5n in mainjg:
        for b in mainjg[a5n]:
            if a1n in b:
                print(b[a1n])
                break
        else:    
            print("没有此人！请检查大小写是否错误！")
            
    else:
        print('没有此行！请检查大小写是否错误！')

