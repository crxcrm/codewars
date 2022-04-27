# The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. 
# Any values that fall out of that range must be rounded to the closest valid value.
# Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.
  
import string

def rgb(r, g, b): 
  
    if r < 0:
        r = 0
    else:
        if r > 255:
            r = 255
    if g < 0:
        g = 0
    else:
        if g > 255:
            g = 255
    if b < 0:
        b = 0
    else:
        if b > 255:
            b = 255
            
    hex = "%02x%02x%02x" % (r, g, b)
    return  hex.upper()

# Other method: 
def limit(num):
   if num < 0:
       return 0
   if num > 255:
       return 255
   return num

def rgb(r, g, b):
    return "{:02X}{:02X}{:02X}".format(limit(r), limit(g), limit(b))
