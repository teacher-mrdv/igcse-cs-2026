def hex2den(hex):
    total = 0
    digit1 = hex[0]
    digit2 = hex[1]
    if ord(digit1) >= 65:
        total = (ord(digit1) - 55) * 16
    else:
        total = (ord(digit1) - 48) * 16
    if ord(digit2) >= 65:
        total = total + (ord(digit2) - 55)
    else:
        total = total + (ord(digit2) - 48)
    return total

invalid = True
while invalid:
    hex = input("hex = ")
    hex = hex.strip().upper()
    invalid = False
    for char in hex:
        if ord(char) < 48 or ord(char) > 70:
            print("error-not a hexadecimal number")
            invalid = True
            break
if len(hex) < 6:
    hex = "0" * (6 - len(hex)) + hex

hex_red = hex[:2]
hex_green = hex[2:4]
hex_blue = hex[4:]

den_red = hex2den(hex_red)
den_green = hex2den(hex_green)
den_blue = hex2den(hex_blue)

print(hex_red, hex_green, hex_blue, " =", den_red, den_green, den_blue)

# check with https://www.color-hex.com/