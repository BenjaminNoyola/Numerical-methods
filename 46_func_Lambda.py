# -*- coding: utf-8 -*-
#! /usr/bin/env python

#tema: función lamda

li = [1,1,1,1,1]
lo = [1,1,1,1,1]
s="holoa mundo"

print map(lambda x,m: x*m, li,lo)

print filter(lambda n: n=="o",s)

print reduce(lambda n,m: n+m,lo) 
