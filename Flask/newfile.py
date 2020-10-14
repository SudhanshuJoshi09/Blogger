from socket import *
ssock = socket(AF_INET, SOCK_DGRAM)
ssock.bind(('', 9999))
x= int(input('Enter last digit of your USN: '))
while True:
    msg,caddr= ssock.recvfrom(10+x)
    msg = msg.decode('ascii')
    print ("Rcvd from ", caddr, " data: ", msg)
    rmsg = msg.upper().encode('ascii')
    ssock.sendto(rmsg, caddr)
