class MotorDriver:
    """! 
    This class implements a motor driver for an ME405 kit. The user can specify a PWM value and
    change the speed of the motor. Changing the sign of PWM changes the direction of the motor.
    """

    def __init__ (self, en_pin, in1pin, in2pin, timer, channel_pos, channel_neg):
        """! 
        Creates a motor driver by initializing GPIO
        pins and turning off the motor for safety. 
        @param en_pin : Pin on motor controller corresponding to pin PA_10 on the Nucleo.
                        Setting high enables the motor.
        @param in1pin : Pin on motor controller corresponding to pin PB_4 on the Nucleo.
                        Used to send PWM signal to motor controller in negative direction.
        @param in2pin : Pin on motor controller corresponding to pin PB_5 on the Nucleo.
                        Used to send PWM signal to motor controller in positive direction.
        @param timer  : Sets timer for PWM. Set to 20,000 Hz to avoid an annoying hum.
        @param channel_pos : Channel number corresponding to the pin controlling the PWM output, channel 2.
        @param channel_neg : Channel number corresponding to the pin controlling the PWM output, channel 1.
        """
        print ("Creating a motor driver")
        self.enPin = en_pin # Initialize pin en_pin (PA10)
        self.enPin.value(1)        
        self.in2_pin = in2pin
        self.in1_pin = in1pin
        self.tim = timer
        self.ch_pos = channel_pos
        self.ch_neg = channel_neg
#         return 

    def set_duty_cycle (self, pwm):
        """!
        This method sets the duty cycle to be sent
        to the motor to the given level. Positive values
        cause torque in one direction, negative values
        in the opposite direction.
        @param : pwm A signed integer holding the duty
                 cycle of the voltage sent to the motor 
        """
        

        if pwm > 0:
            self.ch_neg.pulse_width_percent(0) # sets negative pin to low
            self.ch_pos.pulse_width_percent(pwm) # sends signal to positive direction pin

        else:
            self.ch_neg.pulse_width_percent(abs(pwm)) # sends signal to negative direction pin
            self.ch_pos.pulse_width_percent(0) # sets positive pin to low




        print (f"Setting duty cycle to {pwm}")
        
        
if __name__ == "__main__":
   
    import utime
    
    enPin = pyb.Pin(pyb.Pin.board.PA10, pyb.Pin.OUT_PP) # Initialize pin en_pin (PA10)
    in2_pin = pyb.Pin(pyb.Pin.board.PB4, pyb.Pin.OUT_PP) # Initialize pin in2_pin (PB5)
    in1_pin = pyb.Pin(pyb.Pin.board.PB5, pyb.Pin.OUT_PP) # Initialize pin in1_pin (PB4)
    timmy = pyb.Timer(3, freq=20000) # Initialize timer
    ch_pos = timmy.channel(2, pyb.Timer.PWM, pin=in2_pin) # Initialize positive direction timer channel
    ch_neg = timmy.channel(1, pyb.Timer.PWM, pin=in1_pin) # Initialize negative direction timer channel
    
    moe = MotorDriver(enPin, in2_pin, in1_pin, timmy, ch_pos, ch_neg)
    
    while True:
        moe.set_duty_cycle (50)
        utime.sleep(2)
        moe.set_duty_cycle (0)
        utime.sleep(2)
        moe.set_duty_cycle (100)
        utime.sleep(2)
        moe.set_duty_cycle (0)
        utime.sleep(2)
        moe.set_duty_cycle (-50)
        utime.sleep(2)
        moe.set_duty_cycle (0)
        utime.sleep(2)
        moe.set_duty_cycle (-100)
        utime.sleep(2)
        moe.set_duty_cycle (0)
        utime.sleep(2)
        
