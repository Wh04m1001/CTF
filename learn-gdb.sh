#!/bin/bash
#Author: Wh04m1
#Description: Solution for picoCTF2018 lear gdb challenge ( without gdb :) )

ltrace ./run 2> flag.out;cat flag.out | grep -o '^putchar.*'| awk '{print $3}' | grep -v '^0x' | tr -d ','  |xargs  printf '%x\n' | xxd -r -p| xargs echo -e 
