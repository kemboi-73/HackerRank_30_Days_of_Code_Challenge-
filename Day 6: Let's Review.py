# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/30-review-loop/problem

for T in range(int(input())): 
    s = input()
    print(s[::2]+" "+s[1::2])
