from funcx import FuncXClient, FuncXExecutor
from pprint import pprint

fxc = FuncXClient()
fx = FuncXExecutor(fxc)
endpoint_id = '3d0f563e-f797-40ba-a960-e4614eb258a3'  # gl-login1.arc-ts.umich.edu
#endpoint_id = '21777219-17f0-4de0-ab2d-8ac6df700d18'  # gl-login1.local

endpoint_status = fxc.get_endpoint_status(endpoint_id)
print("Status: %s" % endpoint_status['status'])
pprint(endpoint_status)
#print("Workers: %s" % endpoint_status['logs'][0]['total_workers'])
#print("Tasks: %s" % endpoint_status['logs'][0]['outstanding_tasks'])

def add_func(a, b):
      return a + b

future = fx.submit(add_func, 10, 20, endpoint_id=endpoint_id)

print("Status : ", future.done())

print("Result : ", future.result())

