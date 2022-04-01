from ctypes import windll
from sys import stdout


def set_cmd_text_color(color, handle=windll.kernel32.GetStdHandle(-11)):
    Bool = windll.kernel32.SetConsoleTextAttribute(handle, color)
    return Bool


def color(mess, color, enter=True):
    if enter == True:
        set_cmd_text_color(color)  #设置颜色
        stdout.write(mess + '\n')  #输出
        set_cmd_text_color(0x0c | 0x0a | 0x09)  #重置颜色
    else:
        set_cmd_text_color(color)  #设置颜色
        stdout.write(mess)  #输出
        set_cmd_text_color(0x0c | 0x0a | 0x09)  #重置颜色


def ErrP(mode, item):
    if mode == 'e':
        color('\aErr: ' + item, 0x04)
    elif mode == 'w':
        color('\aWarn: ' + item, 0x06)
    elif mode == 'p':
        color(item, 0x0b)
    elif mode == 'i':
        color('说明: ' + item, 0x0a)
    elif mode == 'g':
        color(item, 0x0a)
    elif mode == 'n':
        color(item, 0x0f)


'''
# Windows CMD命令行 字体颜色定义 text colors
FOREGROUND_BLACK = 0x00 # black.
FOREGROUND_DARKBLUE = 0x01 # dark blue.
FOREGROUND_DARKGREEN = 0x02 # dark green.
FOREGROUND_DARKSKYBLUE = 0x03 # dark skyblue.
FOREGROUND_DARKRED = 0x04 # dark red.
FOREGROUND_DARKPINK = 0x05 # dark pink.
FOREGROUND_DARKYELLOW = 0x06 # dark yellow.
FOREGROUND_DARKWHITE = 0x07 # dark white.
FOREGROUND_DARKGRAY = 0x08 # dark gray.
FOREGROUND_BLUE = 0x09 # blue.
FOREGROUND_GREEN = 0x0a # green.
FOREGROUND_SKYBLUE = 0x0b # skyblue.
FOREGROUND_RED = 0x0c # red.
FOREGROUND_PINK = 0x0d # pink.
FOREGROUND_YELLOW = 0x0e # yellow.
FOREGROUND_WHITE = 0x0f # white.


# Windows CMD命令行 背景颜色定义 background colors
BACKGROUND_BLUE = 0x10 # dark blue.
BACKGROUND_GREEN = 0x20 # dark green.
BACKGROUND_DARKSKYBLUE = 0x30 # dark skyblue.
BACKGROUND_DARKRED = 0x40 # dark red.
BACKGROUND_DARKPINK = 0x50 # dark pink.
BACKGROUND_DARKYELLOW = 0x60 # dark yellow.
BACKGROUND_DARKWHITE = 0x70 # dark white.
BACKGROUND_DARKGRAY = 0x80 # dark gray.
BACKGROUND_BLUE = 0x90 # blue.
BACKGROUND_GREEN = 0xa0 # green.
BACKGROUND_SKYBLUE = 0xb0 # skyblue.
BACKGROUND_RED = 0xc0 # red.
BACKGROUND_PINK = 0xd0 # pink.
BACKGROUND_YELLOW = 0xe0 # yellow.
BACKGROUND_WHITE = 0xf0 # white.
'''