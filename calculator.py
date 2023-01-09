# Initialize variables
display = '0'
last_number = None
last_operation = None
clear_next = False

def clear():
  global display, last_number, last_operation, clear_next
  display = '0'
  last_number = None
  last_operation = None
  clear_next = False

def negate():
  global display
  if display[0] == '-':
    display = display[1:]
  else:
    display = '-' + display

def decimal():
  global display
  if '.' not in display:
    display += '.'

def digit(n):
  global display, clear_next
  if clear_next:
    display = '0'
    clear_next = False
  if display == '0':
    display = str(n)
  elif len(display) < 8:
    display += str(n)

def operation(op):
  global display, last_number, last_operation, clear_next
  if len(display) == 8:
    return
  if last_number is not None and last_operation is not None:
    result = perform_operation(last_number, last_operation, float(display))
    if result is None:
      display = 'ERR'
      last_number = None
      last_operation = None
      clear_next = True
      return
    display = str(result)
    last_number = result
  else:
    last_number = float(display)
  last_operation = op
  clear_next = True

def perform_operation(x, op, y):
  if op == '+':
    return x + y
  elif op == '-':
    return x - y
  elif op == '/':
    if y == 0:
      return None
    return x / y
  elif op == '*':
    return x * y

# Test the calculator
clear()
digit(1)
digit(2)
digit(3)
operation('+')
digit(4)
digit(5)
operation('-')
digit(6)
operation('*')
digit(7)
operation('/')
digit(8)
operation('=')

print(display) # should display '141.75'
