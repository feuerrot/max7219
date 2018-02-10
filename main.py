import max7219

display = max7219.max7219()
display.clear()

i = 0xFFFFFFFF
while True:
	display.write_string("{:0>8X}".format(i))
	i -= 1
