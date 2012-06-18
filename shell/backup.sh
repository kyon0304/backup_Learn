# backup my learning content 
#! /bin/bash
cd /home/wangying/Learn
git add *.cpp *.c *.sh *.py *.txt
git commit -am "Commit - @ $(date)"
git push origin master:master
