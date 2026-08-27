import shutil
import sys
import termios
import tty

old_settings = termios.tcgetattr(sys.stdin)

try:
    tty.setcbreak(sys.stdin)

    sys.stdout.write("\x1b[?1049h")
    sys.stdout.flush()

    while True:
        key = sys.stdin.read(1)

        if key == "q":
            break
        elif key == "\x1b":
            follows = sys.stdin.read(2)
            if follows == "[A":
                sys.stdout.write("<UP>")
            elif follows == "[B":
                sys.stdout.write("<DOWN>")
            elif follows == "[C":
                sys.stdout.write("<RIGHT>")
            elif follows == "[D":
                sys.stdout.write("<LEFT>")
            else:
                sys.stdout.write(f"\x1b{follows}")
        else:
            sys.stdout.write(key)

        sys.stdout.flush()

finally:
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
    sys.stdout.write("\x1b[?1049l")
    sys.stdout.flush()
