import socket
from gpiozero import Button
from datetime import datetime
from time import sleep

b1= Button(4)
b2= Button(17)

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_address=('10.57.10.65',10008)
i=1
#then = datetime.now()
try:
    while (1):
        
        if b1.is_pressed:
            message = 'pressed'.encode('ascii')
            sent=s.sendto(message,server_address)
            print ("pressed")
            """now= datetime.now()
            delta = now - then
            value = delta.seconds
            print(value)"""
            data,address = s.recvfrom(4096)
            datarecv=data.decode()
            with open("Datalog.txt","a") as f1:
                timdif=str(datarecv)+"\n"
                f1.writelines(timdif)
            i+=1
            #then = datetime.now()
            f1.close()
            sleep(0.5)
            
        elif b2.is_pressed:
            with open("Datalog.txt","r+") as f2:
                for line in f2:
                    t=int(line)
                    sleep(t)
                    message = 'pressed'.encode('ascii')
                    sent=s.sendto(message,server_address)
                    print ("pressed")
                f2.close()
            with open("Datalog.txt","w") as f2:
                print('file is emptied now')
                f2.close()
        else: 
            pass
finally:
    s.close()
