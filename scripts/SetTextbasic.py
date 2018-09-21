import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

import sys

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Raspberry Pi pin configuration:
RST = None     # on the PiOLED this pin isnt used
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

# 128x32 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Load default font.
font = ImageFont.load_default()

draw.text((x, top),str(sys.argv[1]),font=font,fill=255)

if len(sys.argv)>2:
	draw.text((x, top+8),str(sys.argv[2]),font=font,fill=255)
	
if len(sys.argv)>3:
	draw.text((x, top+16),str(sys.argv[3]),font=font,fill=255)

if len(sys.argv)>4:
	draw.text((x, top+24),str(sys.argv[4]),font=font,fill=255)

# Display image.
disp.image(image)
disp.display()