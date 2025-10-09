import os
import subprocess

os.chdir('F:')
# filse = os.listdir()
# print(filse)

result = subprocess.check_output('dir /s/b *.psd',shell=True).decode().split()

for i in result:
    os.remove(i)
    print(f'remove items : {i}')
