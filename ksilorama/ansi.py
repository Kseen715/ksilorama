# Copyright Jonathan Hartley 2013. BSD 3-Clause license, see LICENSE file.
'''
This module generates ANSI character codes to printing colors to terminals.
See: http://en.wikipedia.org/wiki/ANSI_escape_code
'''

CSI = '\033['
OSC = '\033]'
BEL = '\a'


def code_to_chars(code):
    return CSI + str(code) + 'm'

def set_title(title):
    return OSC + '2;' + title + BEL

def clear_screen(mode=2):
    return CSI + str(mode) + 'J'

def clear_line(mode=2):
    return CSI + str(mode) + 'K'

def hsl_to_rgb(h, s, l):
    # hsl values are in [0, 1], rgb values are in [0, 255]
    h = float(h)
    s = float(s)
    l = float(l)

    h = min(max(h, 0), 1)
    s = min(max(s, 0), 1)
    l = min(max(l, 0), 1)
    
    r, g, b = 0, 0, 0

    if s == 0:
        r = g = b = l # achromatic
    else:
        def hue2rgb(p, q, t):
            if t < 0: t += 1
            if t > 1: t -= 1
            if t < 1/6: return p + (q - p) * 6 * t
            if t < 1/2: return q
            if t < 2/3: return p + (q - p) * (2/3 - t) * 6
            return p

        q = l * (1 + s) if l < 0.5 else l + s - l * s
        p = 2 * l - q
        r = hue2rgb(p, q, h + 1/3)
        g = hue2rgb(p, q, h)
        b = hue2rgb(p, q, h - 1/3)

    return int(r * 255), int(g * 255), int(b * 255)

def cmyk_to_rgb(c, m, y, k):
    # cmyk values are in [0, 100], rgb values are in [0, 255]
    # cap values to 0-100
    c = min(max(c, 0), 100)
    m = min(max(m, 0), 100)
    y = min(max(y, 0), 100)
    k = min(max(k, 0), 100)

    c = float(c) / 100
    m = float(m) / 100
    y = float(y) / 100
    k = float(k) / 100
    r, g, b = 0, 0, 0

    r = 255 * (1 - c) * (1 - k)
    g = 255 * (1 - m) * (1 - k)
    b = 255 * (1 - y) * (1 - k)

    return int(r), int(g), int(b)

def hex_to_rgb(hex):
    hex = hex.lstrip('#')
    return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

class AnsiCodes(object):
    def __init__(self):
        # the subclasses declare class attributes which are numbers.
        # Upon instantiation we define instance attributes, which are the same
        # as the class attributes but wrapped with the ANSI escape sequence
        for name in dir(self):
            if not name.startswith('_'):
                value = getattr(self, name)
                if isinstance(value, int):
                    setattr(self, name, code_to_chars(value))


class AnsiCursor(object):
    def UP(self, n=1):
        return CSI + str(n) + 'A'
    def DOWN(self, n=1):
        return CSI + str(n) + 'B'
    def FORWARD(self, n=1):
        return CSI + str(n) + 'C'
    def BACK(self, n=1):
        return CSI + str(n) + 'D'
    def POS(self, x=1, y=1):
        return CSI + str(y) + ';' + str(x) + 'H'


class AnsiFore(AnsiCodes):
    BLACK           = 30
    RED             = 31
    GREEN           = 32
    YELLOW          = 33
    BLUE            = 34
    MAGENTA         = 35
    CYAN            = 36
    WHITE           = 37
    RESET           = 39

    # These are fairly well supported, but not part of the standard.
    LIGHTBLACK_EX   = 90
    LIGHTRED_EX     = 91
    LIGHTGREEN_EX   = 92
    LIGHTYELLOW_EX  = 93
    LIGHTBLUE_EX    = 94
    LIGHTMAGENTA_EX = 95
    LIGHTCYAN_EX    = 96
    LIGHTWHITE_EX   = 97

    def C256(self, value):
        return f'\033[38;5;{value}m'

    def RGB(self, r, g, b):
        return f'\033[38;2;{r};{g};{b}m'

    def HSL(self, h, s, l):
        # Convert HSL (float) to RGB and then return the ANSI code
        r, g, b = hsl_to_rgb(h, s, l)
        return f'\033[38;2;{r};{g};{b}m'

    def CMYK(self, c, m, y, k):
        # Convert CMYK (0-100) to RGB and then return the ANSI code
        r, g, b = cmyk_to_rgb(c, m, y, k)
        return f'\033[38;2;{r};{g};{b}m'

    def HEX(self, hex_value):
        # Convert HEX to RGB and then return the ANSI code
        r, g, b = hex_to_rgb(hex_value)
        return f'\033[38;2;{r};{g};{b}m'


class AnsiBack(AnsiCodes):
    BLACK           = 40
    RED             = 41
    GREEN           = 42
    YELLOW          = 43
    BLUE            = 44
    MAGENTA         = 45
    CYAN            = 46
    WHITE           = 47
    RESET           = 49

    # These are fairly well supported, but not part of the standard.
    LIGHTBLACK_EX   = 100
    LIGHTRED_EX     = 101
    LIGHTGREEN_EX   = 102
    LIGHTYELLOW_EX  = 103
    LIGHTBLUE_EX    = 104
    LIGHTMAGENTA_EX = 105
    LIGHTCYAN_EX    = 106
    LIGHTWHITE_EX   = 107

    def C256(self, value):
        return f'\033[48;5;{value}m'

    def RGB(self, r, g, b):
        return f'\033[48;2;{r};{g};{b}m'

    def HSL(self, h, s, l):
        # Convert HSL (float) to RGB and then return the ANSI code
        r, g, b = hsl_to_rgb(h, s, l)
        return f'\033[48;2;{r};{g};{b}m'

    def CMYK(self, c, m, y, k):
        # Convert CMYK to RGB and then return the ANSI code
        r, g, b = cmyk_to_rgb(c, m, y, k)
        return f'\033[48;2;{r};{g};{b}m'

    def HEX(self, hex_value):
        # Convert HEX to RGB and then return the ANSI code
        r, g, b = hex_to_rgb(hex_value)
        return f'\033[48;2;{r};{g};{b}m'


class AnsiStyle(AnsiCodes):
    RESET_ALL       = 0
    BRIGHT          = 1 # aka BOLD
    DIM             = 2
    ITALIC          = 3
    UNDERLINE       = 4
    BLINK           = 5
    INVERTED        = 7
    HIDDEN          = 8
    STRIKETHROUGH   = 9

    NOT_BOLD            = 21
    NORMAL              = 22 # aka NOT_DIM
    NOT_DIM             = 22
    NOT_ITALIC          = 23
    NOT_UNDERLINE       = 24
    NOT_BLINK           = 25
    NOT_INVERTED        = 27
    NOT_HIDDEN          = 28
    NOT_STRIKETHROUGH   = 29

Fore   = AnsiFore()
Back   = AnsiBack()
Style  = AnsiStyle()
Cursor = AnsiCursor()
