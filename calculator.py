# Initialize variables
display = '0'
last_number = None
last_operation = None
clear_next = False

#The clear() function reset the calculator state
def clear():
  global display, last_number, last_operation, clear_next
  display = '0'
  last_number = None
  last_operation = None
  clear_next = False

#The negate() function changes the sign of the displayed number
def negate():
  global display
  if display[0] == '-':
    display = display[1:]
  else:
    display = '-' + display

#The decimal() function adds a decimal point to the displayed number if one is not already present
def decimal():
  global display
  if '.' not in display:
    display += '.'

#The digit() function adds a digit to the displayed number
def digit(n):
  global display, clear_next
  if clear_next:
    display = '0'
    clear_next = False
  if display == '0':
    display = str(n)
  elif len(display) < 8:
    display += str(n)

#The operation() function performs the specified operation using the last number entered and the result of the preceding operation (if any).
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

#The perform_operation() function performs the actual arithmetic for the calculator.
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
