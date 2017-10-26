import socket
from time import sleep
from datetime import datetime

import pyautogui



s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


server_address=('10.57.110.165',10007)
s.bind(server_address)

i=1
then = datetime.now()


while True:
    data,address = s.recvfrom(4096)
    recvdata = data.decode()
    if recvdata == 'pressed':
        pyautogui.click(100, 50)
        now= datetime.now()
        delta = now - then
        value = delta.seconds
        message=str(value).encode('ascii')
        sent=s.sendto(message,address)
        
        i+=1
        then = datetime.now()
    else:
        pass


s.close()
