#! /bin/bash
cd 
echo -n 'time:' >> info.txt 
date >> info.txt 
echo -n 'user:' >> info.txt 
whoami >> info.txt 
echo -n 'os:' >> info.txt 
uname >> info.txt 
echo -n 'num folders in homedir:' >> info.txt 
ls -la | grep ^d | wc -l >> info.txt 
echo -n 'num files in homedir:' >> info.txt
ls -laR | grep "^-" | wc -l >> info.txt

