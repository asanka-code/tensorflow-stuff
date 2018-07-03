#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Need the following setting to remove the warning message
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

# Importing tensorflow module
import tensorflow as tf

# Some variables to calculate
x = 2
y = 3

##########################################################
# First graph

# Variable addOp will contain the add tensor
addOp = tf.add(x,y)
print(addOp)

# Variable mulOp will contain the multiplication tensor
mulOp = tf.multiply(x,y)
print(mulOp)

# Variable powOp1 will contain the power operation tensor
powOp1 = tf.pow(addOp, mulOp)
print(powOp1)


##########################################################
# Second graph

# Variable powOp2 will contain the power operation tensor
powOp2 = tf.pow(mulOp, addOp)
print(powOp2)





# A session is requred to run a tensor graph
sess = tf.Session()

# Let's run the graph on this session (answer1= 5^6, answer2= 6^5)
ans1, ans2 = sess.run( [powOp1, powOp2] )
print("ans1 = %d" % ans1)
print("ans2 = %d" % ans2)

# Close the session
sess.close()

