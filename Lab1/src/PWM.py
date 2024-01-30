if __name__ == "__main__":
    pinPA0 = pyb.Pin(pyb.Pin.board.PA0, pyb.Pin.OUT_PP) # Initialize pin PA0
    tim2 = pyb.Timer(2, freq=20000)
    ch1 = tim2.channel(1, pyb.Timer.PWM, pin=pinPA0)
    ch1.pulse_width_percent(50)
#     pinPA0.value(0)
    # brendan comment for git take two
    #gggggg
    # can JSR edit