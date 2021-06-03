from time import sleep,time,strftime
import board
import busio
import adafruit_tmp117
import matplotlib.pyplot as plt

i2c = busio.I2C(board.SCL, board.SDA)
tmp117 = adafruit_tmp117.TMP117(i2c)

plt.ion()
x = []
y = []

def write_temp(temp):
    print("Temperature: %.2f degrees C" % tmp117.temperature)    
    with open("/home/pi/temp.csv", "a") as log:
        log.write("{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(temp)))

def graph(temp):
    y.append(temp)
    x.append(time())
    plt.clf()
    plt.scatter(x,y)
    plt.plot(x,y)
    plt.draw()
    
while True:
    temp = tmp117.temperature
    write_temp(temp)
    graph(temp)
    plt.pause(1)
    
