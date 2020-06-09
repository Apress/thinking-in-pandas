import sys


try:
    raise Exception("Something went wrong.")
except Exception as e:
    exc_info = sys.exc_info()
    frame = exc_info[2].tb_frame  # create a third reference

import pdb; pdb.set_trace()
assert sys.getrefcount(frame) == 3
del exc_info
assert sys.getrefcount(frame) == 3
