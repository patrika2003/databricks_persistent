import os

if os.path.exists('file.txt'):
  print('file exists')

size=os.path.getsize('file.txt')

import time
mod_time=os.path.getmtime('file.txt')
readable_time=time.ctime(mod_time)
print(mod_time)
print(readable_time)


# file exists
# 1752746785.4850125
# Thu Jul 17 15:36:25 2025