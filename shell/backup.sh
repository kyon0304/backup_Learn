# backup my learning content 
#! /bin/bash
cd /home/wangying/Learn
git add cpp/*.cpp c/*.c *.sh *.py */*.txt *.js
git commit -am "Commit - @ $(date)"
git push backup_Learn master:master
