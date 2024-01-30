import utime

def led_setup():
    pinPA0 = pyb.Pin(pyb.Pin.board.PA0, pyb.Pin.OUT_PP) # Initialize pin PA0
    tim2 = pyb.Timer(2, freq=20000)
    ch1 = tim2.channel(1, pyb.Timer.PWM, pin=pinPA0)
    return ch1
    
def led_brightness(channel, pwm):
    channel.pulse_width_percent(pwm)


if __name__ == "__main__":
    
    ch1 = led_setup()
    while True:
        val = 100
        for i in range(100):
            led_brightness(ch1, val)
            val -= 1
            utime.sleep(0.05)
            
            
        