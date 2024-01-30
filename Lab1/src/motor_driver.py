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
        self.enPin = pyb.Pin(en_pin, pyb.Pin.OUT_PP) # Initialize pin en_pin (PA10)
        self.enPin.value(1)        
        self.in2_pin = pyb.Pin(in2pin, pyb.Pin.OUT_PP) # Initialize pin PB5
        self.in1_pin = pyb.Pin(in1pin, pyb.Pin.OUT_PP) # Initialize pin PB4
        self.tim = pyb.Timer(timer, freq=20000)
        self.ch_pos = self.tim.channel(channel_pos, pyb.Timer.PWM, pin=self.in2_pin)
        self.ch_neg = self.tim.channel(channel_neg, pyb.Timer.PWM, pin=self.in1_pin)
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
            self.ch_neg.pulse_width_percent(0)
            self.ch_pos.pulse_width_percent(pwm)

        else:
            self.ch_neg.pulse_width_percent(abs(pwm))
            self.ch_pos.pulse_width_percent(0)




        print (f"Setting duty cycle to {pwm}")
        
        
if __name__ == "__main__":
    import utime
    moe = MotorDriver (pyb.Pin.board.PA10, pyb.Pin.board.PB4, pyb.Pin.board.PB5, 3, 2,1)
    while True:
        moe.set_duty_cycle (50)
        utime.sleep(2)
        moe.set_duty_cycle (-50)
        utime.sleep(2)
        
        
