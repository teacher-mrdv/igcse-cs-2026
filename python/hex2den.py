Your update addresses the string length validation cleanly!

There are two subtle bugs in the current logic to be aware of:

### Key Issues to Fix

1. **The ASCII Range "Gap" (`:;<=>?@`)**
* `'0'` to `'9'` is ASCII **48 to 57**.
* `'A'` to `'F'` is ASCII **65 to 70**.
* The condition `ord(char) < 48 or ord(char) > 70` accidentally allows ASCII characters **58 through 64** (`:`, `;`, `<`, `=`, `>`, `?`, `@`) to pass validation. For example, typing `12:456` will be accepted as valid hex.
* **Fix:** Use explicit range checks:
```python
if not (48 <= ord(char) <= 57 or 65 <= ord(char) <= 70):

```




2. **Silent Failure on Bad Length**
* If `len(hex) < 1` or `len(hex) > 6`, the loop sets `invalid = True` and calls `continue`, but it doesn't print an error message. The prompt re-appears without telling the user what went wrong.
* **Fix:** Add a quick `print("Error: Input must be between 1 and 6 characters.")` before `continue`.


3. **Minor Slicing Detail**
* `hex[4:7]` works safely because Python stops at index 5 for a 6-character string, but standard slice notation for 6 characters is `hex[4:6]` or `hex[4:]`.



---

### Corrected Code (Keeping Your Educational ASCII Logic)

If you are writing this for a CS class requirement where manual ASCII conversion is required:

```python
def hex2den(hex_str):
    total = 0
    digit1 = hex_str[0]
    digit2 = hex_str[1]

    # First digit (multiply by 16)
    if ord(digit1) >= 65:
        total = (ord(digit1) - 55) * 16
    else:
        total = (ord(digit1) - 48) * 16

    # Second digit (multiply by 1)
    if ord(digit2) >= 65:
        total += ord(digit2) - 55
    else:
        total += ord(digit2) - 48

    return total


invalid = True
while invalid:
    hex_input = input("hex = ").strip().upper()
    invalid = False

    # 1. Length check
    if len(hex_input) < 1 or len(hex_input) > 6:
        print("Error: Input must be between 1 and 6 hexadecimal characters.")
        invalid = True
        continue

    # 2. Hexadecimal character check (48-57 for 0-9, 65-70 for A-F)
    for char in hex_input:
        if not (48 <= ord(char) <= 57 or 65 <= ord(char) <= 70):
            print("Error: Not a hexadecimal character.")
            invalid = True
            break

# Pad leading zeros to make exactly 6 characters
if len(hex_input) < 6:
    hex_input = "0" * (6 - len(hex_input)) + hex_input

# Slice into 2-character pairs
hex_red = hex_input[:2]
hex_green = hex_input[2:4]
hex_blue = hex_input[4:6]

# Convert each pair to denary
den_red = hex2den(hex_red)
den_green = hex2den(hex_green)
den_blue = hex2den(hex_blue)

print(hex_red, hex_green, hex_blue, " =", den_red, den_green, den_blue)



# check with https://www.color-hex.com/