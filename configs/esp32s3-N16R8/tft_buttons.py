from machine import Pin

class Buttons():
    def __init__(self):
        self.name = "esp32s3-n16r8"
        self.left   = Pin(15, Pin.IN, Pin.PULL_UP)
        self.right  = Pin(16, Pin.IN, Pin.PULL_UP)
        self.hyper  = Pin(17, Pin.IN, Pin.PULL_UP)
        self.thrust = Pin(18, Pin.IN, Pin.PULL_UP)
        self.fire   = Pin(21, Pin.IN, Pin.PULL_UP)
