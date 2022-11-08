from funcx import FuncXClient, FuncXExecutor
from pprint import pprint

fxc = FuncXClient()
#endpoint_id = '3d0f563e-f797-40ba-a960-e4614eb258a3'  # gl-login1.arc-ts.umich.edu
#endpoint_id = '21777219-17f0-4de0-ab2d-8ac6df700d18'  # gl-login1.local

def add_func(a = 0, b = 0):
      return a + b

func_uuid = fxc.register_function(add_func)
print(func_uuid)
