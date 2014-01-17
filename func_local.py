#!/usr/bin/env python
# -*- coding: utf-8 -*-

def func(x):
    print 'x is ', x
    x = 2
    print 'change local x to', x

x = 50
func(x)
print 'x is still', x