from pathlib import Path
import os


current_dir = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(current_dir, "json")
filePath = f"{path}"
cuong = ""
# C:\Users\dell\Documents\cuong\learning\test\Automation_Test\testCase\json\"cuong.json" "demo.json" "demo1.json"
entries = Path(r'C:\Users\dell\Documents\cuong\learning\test\Automation_Test\testCase\json')
for entry in entries.iterdir():
    cuong = cuong + '"' + str(entry.name) + '" '

print(cuong)
# print(filePath)

