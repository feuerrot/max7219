# MAX7219

[Datasheet](https://datasheets.maximintegrated.com/en/ds/MAX7219-MAX7221.pdf)


## Usage
```python
import max7219

display = max7219.max7219()

display.clear()

display.write_char(0, "H")
display.write_char(1, "E")
display.write_char(2, "L")
display.write_char(3, "L")
display.write_char(4, "O")

display.write_string("12345678")
```

