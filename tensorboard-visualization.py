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
a = tf.constant(2)
b = tf.constant(3)
x = tf.add(a,b)

writer = tf.summary.FileWriter('./graphs', tf.get_default_graph())

sess = tf.Session()

ans = sess.run(x)
print(ans)

writer.close()
sess.close()
