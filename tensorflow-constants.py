#!/usr/bin/python

# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 16:28:50 2018

@author: asanka
"""

# Need the following setting to remove the warning message
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

# Importing tensorflow module
import tensorflow as tf

# Defining constant variables
#a = tf.constant([2,2])
a = tf.constant(2)
b = tf.constant([ [0,1], [2,3] ])

# elementwise multiplication
x = tf.multiply(a,b)


#zero filled tensors
z = tf.zeros([2,2], tf.int32)
#ones filled tensors
o = tf.ones([2,3], tf.int32)

sess = tf.Session()

ans = sess.run(x)
print(ans)
ans = sess.run(z)
print(ans)
ans = sess.run(o)
print(ans)

sess.close()
