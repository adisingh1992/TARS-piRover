from flask import Flask, render_template
import RPi.GPIO as gpio
import os, random
import time

app = Flask(__name__)

gpio.setmode(gpio.BOARD)
gpio.setup(12, gpio.OUT)
gpio.setup(11, gpio.OUT)
gpio.setup(13, gpio.OUT)
gpio.setup(15, gpio.OUT)
    
@app.route('/setup')
def setup():
    gpio.setmode(gpio.BOARD)
    gpio.setup(12, gpio.OUT)
    gpio.setup(11, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    gpio.setup(15, gpio.OUT)
    return render_template('index.html')

@app.route('/forward')
def forward():
    gpio.output(12, False)
    gpio.output(11, True)
    gpio.output(13, False)
    gpio.output(15, True)
    return render_template('index.html')

@app.route('/reverse')
def reverse():
    gpio.output(12, True)
    gpio.output(11, False)
    gpio.output(13, True)
    gpio.output(15, False)
    return render_template('index.html')

@app.route('/left')
def left():
    gpio.output(12, False)
    gpio.output(11, True)
    gpio.output(13, False)
    gpio.output(15, False)
    time.sleep(1.8)
    stop()
    return render_template('index.html')

@app.route('/right')
def right():
    gpio.output(12, False)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, True)
    time.sleep(1.8)
    stop()
    return render_template('index.html')

@app.route('/stop')
def stop():
    gpio.output(12, False)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, False)
    return render_template('index.html')

@app.route('/clear')
def clear():
    stop()
    gpio.cleanup()
    return render_template('index.html')

@app.route('/music')
def rndmp3():
    randomfile = random.choice(os.listdir("/home/pi/mp3/"))
    file = " /home/pi/mp3/"+randomfile
    os.system('mplayer'+file+' &')
    return render_template('index.html')

@app.route('/stopm')
def stopm():
    proc="mplayer"
    os.system('pkill '+proc)
    return render_template('index.html')

@app.route('/shutdown')
def shutdown():
    clear()
    stopm()
    os.system('shutdown -h now')
    return

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
