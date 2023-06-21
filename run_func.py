from globus_compute_sdk import Executor
from pprint import pprint
import time


# First, define the function ...
def add_func(a, b):
    import time
    time.sleep(10)
    return a + b

tutorial_endpoint_id = '6b4b7c27-3fd5-4f12-a529-96f2f1dfffdf' # Public tutorial endpoint
#tutorial_endpoint_id = '657ee312-da8a-497e-9026-a6faf4b16cf8' # Public tutorial endpoint
# ... then create the executor, ...
with Executor(endpoint_id=tutorial_endpoint_id) as gce:
    # ... then submit for execution, ...
    future = gce.submit(add_func, 5, 10)

    # ... and finally, wait for the result
    print(future.result())
