#author = inveteckglobal

import subprocess
from subprocess import PIPE
import os

in_file = open("/home/robert/check.txt", "r").read()
out_file = open("/home/robert/out.txt", "r").read()

result = ""
for char in range(len(in_file)):
in_ord = ord(in_file[char])
out_ord = ord(out_file[char])

index = 0
while out_ord != in_ord:
out_ord = (out_ord - 1) % 255
print(out_ord)
print(in_ord)
index += 1
result += chr(index)
print(result)
