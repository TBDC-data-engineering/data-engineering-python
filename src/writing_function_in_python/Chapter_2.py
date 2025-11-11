# Using context managers
import contextlib
import os
from datetime import time

import timer

with open('example.txt', 'w') as file:
    file.write('Hello, World!')




with open('example.txt') as file:
  text = file.read()

n = 0
for word in text.split():
  if word.lower() in ['cat', 'cats']:
    n += 1

print('Lewis Carroll uses the word "cat" {} times'.format(n))


# Time how long process_with_numpy(image) takes to run
#with timer:
#  print('Numpy version')


# Time how long process_with_pytorch(image) takes to run
#with timer:
#  print('Pytorch version')

## Define a context manager

@contextlib.contextmanager
def my_context_manager(interval=5):
    print("Entering the context")
    yield 900 + interval
    print("Exiting the context")


# Use the context manager
with my_context_manager(100) as foo:
  print(f"foo is {foo}")


@contextlib.contextmanager
def in_dir(path:str):
  old_dir = os.getcwd()
  print(old_dir)
  os.chdir(path)
  print(path)
  print(os.listdir(path))
  yield
  os.chdir(old_dir)

with in_dir('/Users/silvionormeygomez/Documents'):
  print("test")


# Add a decorator that will make timer() a context manager
@contextlib.contextmanager
def timer():
  """Time the execution of a context block.

  Yields:
    None
  """
  start = time.time()
  # Send control back to the context block
  yield
  end = time.time()
  print('Elapsed: {:.2f}s'.format(end - start))

with timer():
  print('This should take approximately 0.25 seconds')
  time.sleep(0.25)









