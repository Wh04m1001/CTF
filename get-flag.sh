ltrace ./run 2> flag.out;cat flag.out | grep -o '^putchar.*'| awk '{print $3}' | grep -v '^0x' | tr -d ','  |xargs  printf '%x\n' | xxd -r -p| xargs echo -e 
