import time
from openvino.inference_engine import IEPlugin

while True:
    plugin = IEPlugin(device="CPU")

    if plugin != None:
        print("Found inference engine")
    else:
        print("ERROR - no inference engine found")

    time.sleep(10.0)
