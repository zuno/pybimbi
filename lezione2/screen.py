import base64
import numbers
import os

ESC = '\u001B['
# isTerminalApp = 1 if os.environ['TERM_PROGRAM'] == 'Apple_Terminal' else 0
isTerminalApp = 0

def _(s): 
    do(s)
    return s

# def _(s): return s.decode('unicode_escape');

def cursorTo(x, y = None):
  if (not isinstance(x, numbers.Number)):
    raise ValueError('The `x` argument is required')

  if not isinstance(y, numbers.Number):
    return _(ESC + str(x + 1) + 'G')

  return _(ESC + str(y + 1) + ';' + str(x + 1) + 'H')

def cursorMove(x, y = None):
  if not isinstance(x, numbers.Number):
    raise ValueError('The `x` argument is required')

  ret = ''

  if x < 0:
    ret += ESC + '-' + str(x) + 'D'
  elif x > 0:
    ret += ESC + str(x) + 'C'

  if y < 0:
    ret += ESC + '-' + str(y) + 'A'
  elif y > 0:
    ret += ESC + str(y) + 'B'

  return _(ret);

def cursorUp(count = 1):
  if not isinstance(count, numbers.Number): count = 1
  return _(ESC + str(count) + 'A');

def cursorDown(count = 1):
  if not isinstance(count, numbers.Number): count = 1
  return _(ESC + str(count) + 'B');

def cursorForward(count = 1):
  if not isinstance(count, numbers.Number): count = 1
  return _(ESC + str(count) + 'C');

def cursorBackward(count = 1):
  if not isinstance(count, numbers.Number): count = 1
  return _(ESC + str(count) + 'D');

def cursorLeft(): return _(ESC + 'G')
def cursorSavePosition(): return _(ESC + ('7' if isTerminalApp else 's'))
def cursorRestorePosition(): return _(ESC + ('8' if isTerminalApp else 'u'))
def cursorGetPosition(): return _(ESC + '6n')
def cursorNextLine(): return _(ESC + 'E')
def cursorPrevLine(): return _(ESC + 'F')
def cursorHide(): return _(ESC + '?25l')
def cursorShow(): return _(ESC + '?25h')

def eraseLines(count = 1):
  clear = ''

  for i in range(count):
    clear += eraseLine() + (cursorUp() if i < count - 1 else '')

  return _(clear + cursorLeft());

def eraseEndLine(): return _(ESC + 'K');
def eraseStartLine(): return _(ESC + '1K');
def eraseLine(): return _(ESC + '2K');
def eraseDown(): return _(ESC + 'J');
def eraseUp(): return _(ESC + '1J');
def eraseScreen(): return _(ESC + '2J');
def scrollUp(): return _(ESC + 'S');
def scrollDown(): return _(ESC + 'T');

def clearScreen(): return _('\u001Bc');
def beep(): return _('\u0007');

def image(buf, opts = {}):
  ret = '\u001B]1337;File=inline=1'

  if 'width' in opts:
    ret += ';width=' + str(opts['width'])

  if 'height' in opts:
    ret += ';height=' + str(opts['height'])

  if 'preserveAspectRatio' in opts:
    if (not opts['preserveAspectRatio']):
      ret += ';preserveAspectRatio=0'

  return _(ret + ':' + base64.b64encode(buf) + '\u0007');

def setCwd(cwd = os.getcwd()):
  return _('\u001B]50;CurrentDir=' + cwd + '\u0007');

def do(s):
  print(s,end="")

