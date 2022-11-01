import subprocess

import sys
res = 0
process = subprocess.run(["rg", "-c", r"^## \w"] + sys.argv[1:], text=True, stdout=subprocess.PIPE)
for line in process.stdout.splitlines():
    print(line)
    number = int(line.split(":")[-1])
    res += number

print("---")
print(res, "slides")
print(res / 50, "hours")
