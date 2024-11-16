# Copyright Jonathan Hartley 2013. BSD 3-Clause license, see LICENSE file.
import sys
from unittest import TestCase, main

from ..ansi import Back, Fore, Style
from ..ansitowin32 import AnsiToWin32

stdout_orig = sys.stdout
stderr_orig = sys.stderr


class AnsiTest(TestCase):

    def setUp(self):
        # sanity check: stdout should be a file or StringIO object.
        # It will only be AnsiToWin32 if init() has previously wrapped it
        self.assertNotEqual(type(sys.stdout), AnsiToWin32)
        self.assertNotEqual(type(sys.stderr), AnsiToWin32)

    def tearDown(self):
        sys.stdout = stdout_orig
        sys.stderr = stderr_orig


    def testForeAttributes(self):
        self.assertEqual(Fore.BLACK, '\033[30m')
        self.assertEqual(Fore.RED, '\033[31m')
        self.assertEqual(Fore.GREEN, '\033[32m')
        self.assertEqual(Fore.YELLOW, '\033[33m')
        self.assertEqual(Fore.BLUE, '\033[34m')
        self.assertEqual(Fore.MAGENTA, '\033[35m')
        self.assertEqual(Fore.CYAN, '\033[36m')
        self.assertEqual(Fore.WHITE, '\033[37m')
        self.assertEqual(Fore.RESET, '\033[39m')

        # Check the light, extended versions.
        self.assertEqual(Fore.LIGHTBLACK_EX, '\033[90m')
        self.assertEqual(Fore.LIGHTRED_EX, '\033[91m')
        self.assertEqual(Fore.LIGHTGREEN_EX, '\033[92m')
        self.assertEqual(Fore.LIGHTYELLOW_EX, '\033[93m')
        self.assertEqual(Fore.LIGHTBLUE_EX, '\033[94m')
        self.assertEqual(Fore.LIGHTMAGENTA_EX, '\033[95m')
        self.assertEqual(Fore.LIGHTCYAN_EX, '\033[96m')
        self.assertEqual(Fore.LIGHTWHITE_EX, '\033[97m')

        self.assertEqual(Fore.C256(0), '\033[38;5;0m')
        self.assertEqual(Fore.C256(255), '\033[38;5;255m')

        self.assertEqual(Fore.RGB(0, 0, 0), '\033[38;2;0;0;0m')
        self.assertEqual(Fore.RGB(255, 255, 255), '\033[38;2;255;255;255m')

        self.assertEqual(Fore.HSL(0, 0, 0), '\033[38;2;0;0;0m')
        self.assertEqual(Fore.HSL(0, 0, 1), '\033[38;2;255;255;255m')

        self.assertEqual(Fore.CMYK(0, 0, 0, 100), '\033[38;2;0;0;0m')
        self.assertEqual(Fore.CMYK(0, 0, 0, 0), '\033[38;2;255;255;255m')

        self.assertEqual(Fore.HEX('#000000'), '\033[38;2;0;0;0m')
        self.assertEqual(Fore.HEX('#FFFFFF'), '\033[38;2;255;255;255m')


    def testBackAttributes(self):
        self.assertEqual(Back.BLACK, '\033[40m')
        self.assertEqual(Back.RED, '\033[41m')
        self.assertEqual(Back.GREEN, '\033[42m')
        self.assertEqual(Back.YELLOW, '\033[43m')
        self.assertEqual(Back.BLUE, '\033[44m')
        self.assertEqual(Back.MAGENTA, '\033[45m')
        self.assertEqual(Back.CYAN, '\033[46m')
        self.assertEqual(Back.WHITE, '\033[47m')
        self.assertEqual(Back.RESET, '\033[49m')

        # Check the light, extended versions.
        self.assertEqual(Back.LIGHTBLACK_EX, '\033[100m')
        self.assertEqual(Back.LIGHTRED_EX, '\033[101m')
        self.assertEqual(Back.LIGHTGREEN_EX, '\033[102m')
        self.assertEqual(Back.LIGHTYELLOW_EX, '\033[103m')
        self.assertEqual(Back.LIGHTBLUE_EX, '\033[104m')
        self.assertEqual(Back.LIGHTMAGENTA_EX, '\033[105m')
        self.assertEqual(Back.LIGHTCYAN_EX, '\033[106m')
        self.assertEqual(Back.LIGHTWHITE_EX, '\033[107m')

        self.assertEqual(Back.C256(0), '\033[48;5;0m')
        self.assertEqual(Back.C256(255), '\033[48;5;255m')

        self.assertEqual(Back.RGB(0, 0, 0), '\033[48;2;0;0;0m')
        self.assertEqual(Back.RGB(255, 255, 255), '\033[48;2;255;255;255m')

        self.assertEqual(Back.HSL(0, 0, 0), '\033[48;2;0;0;0m')
        self.assertEqual(Back.HSL(0, 0, 1), '\033[48;2;255;255;255m')

        self.assertEqual(Back.CMYK(0, 0, 0, 100), '\033[48;2;0;0;0m')
        self.assertEqual(Back.CMYK(0, 0, 0, 0), '\033[48;2;255;255;255m')

        self.assertEqual(Back.HEX('#000000'), '\033[48;2;0;0;0m')
        self.assertEqual(Back.HEX('#FFFFFF'), '\033[48;2;255;255;255m')


    def testStyleAttributes(self):
        self.assertEqual(Style.RESET_ALL            , '\033[0m')
        self.assertEqual(Style.BRIGHT               , '\033[1m') # aka BOLD
        self.assertEqual(Style.DIM                  , '\033[2m')
        self.assertEqual(Style.ITALIC               , '\033[3m')
        self.assertEqual(Style.UNDERLINE            , '\033[4m')
        self.assertEqual(Style.BLINK                , '\033[5m')
        self.assertEqual(Style.INVERTED             , '\033[7m')
        self.assertEqual(Style.HIDDEN               , '\033[8m')
        self.assertEqual(Style.STRIKETHROUGH        , '\033[9m')
        self.assertEqual(Style.NOT_BOLD             , '\033[21m')
        self.assertEqual(Style.NORMAL               , '\033[22m') # aka NOT_DIM
        self.assertEqual(Style.NOT_DIM              , '\033[22m')
        self.assertEqual(Style.NOT_ITALIC           , '\033[23m')
        self.assertEqual(Style.NOT_UNDERLINE        , '\033[24m')
        self.assertEqual(Style.NOT_BLINK            , '\033[25m')
        self.assertEqual(Style.NOT_INVERTED         , '\033[27m')
        self.assertEqual(Style.NOT_HIDDEN           , '\033[28m')
        self.assertEqual(Style.NOT_STRIKETHROUGH    , '\033[29m')
        

if __name__ == '__main__':
    main()
