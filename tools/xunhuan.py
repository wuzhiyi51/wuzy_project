# coding=utf-8

for i in range(1, 10):
    for j in range(1, i + 1):
        print j, 'x', i, '=', j * i, '\t',
        # print str(j)+'+'+str(i)
    print '\n'
