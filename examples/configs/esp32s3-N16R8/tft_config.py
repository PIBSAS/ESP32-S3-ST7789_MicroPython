from machine import SPI, Pin
import st7789

TFA = 40
BFA = 40

SPI_ID = 1
SPI_BAUDRATE = 40000000 # MAX 60Mhz

PIN_SCL  = 12 # FSPICLK
PIN_SDA = 11 # FSPID
PIN_CS   = 10 # FSPICS0

PIN_DC   = 6
PIN_RES  = 7
# Backlight (opcional if not 3V3 Pin available)
PIN_BLK   = 4 # 3V3 available

def config(rotation=0, buffer_size=0, options=0):
    return st7789.ST7789(
        SPI(SPI_ID, baudrate=SPI_BAUDRATE, polarity=0, phase=0, sck=Pin(PIN_SCL), mosi=Pin(PIN_SDA), miso=None),
        170,
        320,
        reset=Pin(PIN_RES, Pin.OUT),
        cs=Pin(PIN_CS, Pin.OUT),
        dc=Pin(PIN_DC, Pin.OUT),
        backlight=Pin(PIN_BLK, Pin.OUT),
        rotation=rotation,
        options=options,
        buffer_size= buffer_size)
