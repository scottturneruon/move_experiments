from microbit import *
import neopixel

np = neopixel.NeoPixel(pin0, 5)
lig=[[255,0,0],[255,127,0],[255,255,0],[0,255,0],[0,0,255],[75,0,136],[139,0,255]]
count1=1
count0=0
count2=2
count3=3
count4=4
while True:
        np[0] = lig[count0]
        if count0>=6:
            count0=0;
        else:
            count0=count0+1
        np[1] = lig[count1]
        if count1>=6:
            count1=0;
        else:
            count1=count1+1
        np[2] = lig[count2]
        if count2>=6:
            count2=0;
        else:
            count2=count2+1
        np[3] = lig[count3]
        if count3>=6:
            count3=0;
        else:
            count3=count3+1
        np[4] = lig[count4]
        if count4>=6:
            count4=0;
        else:
            count4=count4+1
        np.show()
        sleep(500)