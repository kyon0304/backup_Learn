#! /usr/bin/env/ python
#import sys
#sys.setrecursionlimit(1000000000)

def getChange(amount, changes, idx, flag, ans):
    if idx == 0:
        return 1
    if amount < 0:
        return 0
    if flag[amount][idx] == True:
        return ans[amount][idx]
    repeat = 0
    while repeat*changes[idx] <= amount:
        ans[amount][idx] += getChange(amount - repeat*changes[idx], changes, idx-1, flag, ans)
        repeat += 1
    flag[amount][idx] = True
    return ans[amount][idx]

def main():
    amount = 10000
    changes = [1,5,10,50,100,500,1000,2000,5000]
    count = len(changes)
    ans = [[0 for col in range(count)] for row in range(amount+1)]
    flag = [[False for col in range(count)] for col in range(amount+1)]
    count -= 1
    #answer = getChange(amount, changes, count, vis, ans)
    answer = getChange(10000, changes, count, flag, ans)
    print answer

if __name__ == '__main__':
    main()
