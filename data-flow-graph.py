#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tensorflow as tf

# Some variables to calculate
x = 2
y = 3

# Variable addOp will contain the add tensor
addOp = tf.add(x,y)
print(addOp)

# Variable mulOp will contain the multiplication tensor
mulOp = tf.multiply(x,y)
print(mulOp)

# Variable powOp will contain the power operation tensor
powOp = tf.pow(addOp, mulOp)
print(powOp)

# A session is requred to run a tensor graph
sess = tf.Session()

# Let's run the graph on this session (answer= 5^6)
ans = sess.run(powOp)
print(ans)

# Close the session
sess.close()

