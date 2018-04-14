#encoding=utf-8
import numpy as np

def main():
    list=[[1,3,5],[2,4,6]]
    print(type(list))
    nplist=np.array(list)
    print(type(nplist))
    nplist=np.array(list,dtype=np.float)
    #bool,int,uint....
    print(nplist.shape) #几行几列
    print(nplist.ndim) #维数
    print(nplist.itemsize) #每个元素的大小（字节）
    print(nplist.size) #所有元素个数（行*列）
    import tensorflow as tf
    hello = tf.constant('hello, Tensorflow!')
    sess = tf.Session()
    print(sess.run(hello))

if __name__=="__main__":
    main()