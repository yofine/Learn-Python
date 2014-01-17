#!/usr/bin/env python
# -*- coding: utf-8 -*-

number = 23
guess = int(raw_input('Enter an integer : '))

if guess == number:
    print 'Congratulations, you guessed it.'
    print '(but you do not win any prizes!)'
elif guess < number:
    print 'No, it is a little higher than that'
else:
    print 'No, it is a little lower than that'

print 'Done'
