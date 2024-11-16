from __future__ import print_function
import fixpath
import ksilorama

# Demonstrate cursor relative movement: UP, DOWN, FORWARD, and BACK in ksilorama.CURSOR

up = ksilorama.Cursor.UP
down = ksilorama.Cursor.DOWN
forward = ksilorama.Cursor.FORWARD
back = ksilorama.Cursor.BACK

def main():
    """
    expected output:
    1a2
    aba
    3a4
    """
    ksilorama.just_fix_windows_console()
    print("aaa")
    print("aaa")
    print("aaa")
    print(forward() + up(2) + "b" + up() + back(2) + "1" + forward() + "2" + back(3) + down(2) + "3" + forward() + "4")


if __name__ == '__main__':
    main()
