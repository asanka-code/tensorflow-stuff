#!/usr/bin/python
import tensorflow as tf

# define a placeholder of 1x3 row vector (values are not assigned)
a = tf.placeholder(tf.int32, shape=[3])

# define a constant of 1x3 vector with values assigned
b = tf.constant([1, 1, 1], tf.int32)

# add the two tensors together
c = tf.add(a,b)

sess = tf.Session()

# run the session while assigning a dictionary of values to the placeholder/s
ans = sess.run(c, feed_dict={a: [1,2,3]})

print(ans)

sess.close()
