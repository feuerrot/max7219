import time
import max7219

display = max7219.max7219()

display.write_string("--HELP--")
time.sleep(5)

i = 0
while True:
	display.write_string("{:0>8X}".format(i))
	i += 1
