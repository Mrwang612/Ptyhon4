#!/user/bin/Python3
# -*- coding:utf-8 -*-
# Author:jiangNan
# Time:2018.6.2
i =1
while i <= 9:
    j = 1
    while j <= i:
        print("%d * %d = %d\t" % ( j   , i   ,j  * i    ),end = "" )
        j += 1
    print ()
    i += 1