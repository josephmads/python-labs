# Use the built-in `platform` module to print out the following info:

import platform

p1 = platform.platform()
p2 = platform.python_compiler()
p3 = platform.python_version()
p4 = platform.system()
p5 = platform.release()
p6 = platform.processor()
 
print(f"{'Platform:':>10} {p1}",)  # platform.platform()
print(f"{'Compiler:':>10} {p2}",)  # platform.python_compiler()
print(f"{'Python:':>10} {p3}",)  # platform.python_version()
print(f"{'System:':>10} {p4}",)  # platform.system()
print(f"{'Release:':>10} {p5}",)  # platform.release()
print(f"{'System:':>10} {p6}",)  # platform.processor()