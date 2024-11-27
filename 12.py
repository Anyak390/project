for k in range (2,100):
    s=k*'8'
    while '555' in s or '888' in s:
        s=s.replace('555','8',1)
        s=s.replace('888','55',1)
        print(s, s.count('8'))
