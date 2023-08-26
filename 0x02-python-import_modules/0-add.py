#!/usr/bin/python3

a = 1
b = 2

imported_module = __import__('add_0', globals(), locals(), ['add'], 0)
add_result = imported_module.add(a, b)

print(f"{a} + {b} = {add_result}")
