import os
from time import sleep

name_file = input("\nEnter name file: ") + ".py"
with open(f"{name_file}", "w") as file:
    script_py = file
    script_py.write("import generate_script.py")

for i in range(3, 0, -1):
    print(i, end=" ")
    sleep(1)

os.system(f"python {name_file}")
