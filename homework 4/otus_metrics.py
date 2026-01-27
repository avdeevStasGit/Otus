#!/usr/bin/env python3
import json
import random
import sys

METRICS = ["metric1", "metric2", "metric3"]

def discovery():
   
    data = [{ "{#METRIC}": m } for m in METRICS]
    print(json.dumps(data, indent=4))

def value(metric):
    if metric not in METRICS:
        print("0")
        return
    print(random.randint(0, 100))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: script --discovery | --value <metric>")
        sys.exit(1)

    if sys.argv[1] == "--discovery":
        discovery()
    elif sys.argv[1] == "--value" and len(sys.argv) == 3:
        value(sys.argv[2])
    else:
        print("Invalid parameters")
