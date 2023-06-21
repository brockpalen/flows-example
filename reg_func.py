from globus_compute_sdk import Client
from pprint import pprint

gcc = Client()

def add_func(a = 0, b = 0):
          return a + b

func_uuid = gcc.register_function(add_func)
print(func_uuid)
