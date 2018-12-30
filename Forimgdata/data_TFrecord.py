#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-14 09:19:14
# @Author  : WangGuo
# @Email   : guo_wang_113@163.com
# @Github  : https://github.com/King-Key

# #制作二进制数据
import sys
#sys.path.insert(0, '../models/slim/')  models-master research
#sys.path.insert(0, './models/research/slim/') #把后面的路径插入到系统路径中 idx=0
#from datasets import dataset_utils
#import dataset_utils


import math
import tensorflow as tf 
import os


#  根据list路径  把数据转化为TFRecord

def int64_feature(values):
  """Returns a TF-Feature of int64s.
  Args:
    values: A scalar or list of values.
  Returns:
    A TF-Feature.
  """
  if not isinstance(values, (tuple, list)):
    values = [values]
  return tf.train.Feature(int64_list=tf.train.Int64List(value=values))


def bytes_feature(values):
  """Returns a TF-Feature of bytes.
  Args:
    values: A string.
  Returns:
    A TF-Feature.
  """
  return tf.train.Feature(bytes_list=tf.train.BytesList(value=[values]))


def float_feature(values):
  """Returns a TF-Feature of floats.
  Args:
    values: A scalar of list of values.
  Returns:
    A TF-Feature.
  """
  if not isinstance(values, (tuple, list)):
    values = [values]
  return tf.train.Feature(float_list=tf.train.FloatList(value=values))


def image_to_tfexample(image_data, image_format, height, width, class_id):
  return tf.train.Example(features=tf.train.Features(feature={
      'image/encoded': bytes_feature(image_data),
      'image/format': bytes_feature(image_format),
      'image/class/label': int64_feature(class_id),
      'image/height': int64_feature(height),
      'image/width': int64_feature(width),
  }))


# def convert_dataset(list_path, data_dir, output_dir, _NUM_SHARDS=5):  
def convert_dataset(split_name,list_path, data_dir, output_dir, _NUM_SHARDS=2): 
    assert split_name in ['train','validation']    
    fd = open(list_path)
    lines = [line.split() for line in fd]
    fd.close()
    num_per_shard = int(math.ceil(len(lines) / float(_NUM_SHARDS)))
    with tf.Graph().as_default():
        decode_jpeg_data = tf.placeholder(dtype=tf.string)
        decode_jpeg = tf.image.decode_jpeg(decode_jpeg_data, channels=3)
        with tf.Session('') as sess:
            for shard_id in range(_NUM_SHARDS):
                output_path = os.path.join(output_dir,
#                     'data_{:05}-of-{:05}.tfrecord'.format(shard_id, _NUM_SHARDS))
                    'flowers_%s_%05d-of-%05d.tfrecord' % (split_name, shard_id, _NUM_SHARDS))
                tfrecord_writer = tf.python_io.TFRecordWriter(output_path)
                start_ndx = shard_id * num_per_shard
                end_ndx = min((shard_id + 1) * num_per_shard, len(lines))
                for i in range(start_ndx, end_ndx):
                    sys.stdout.write('\r>> Converting image {}/{} shard {}'.format(
                        i + 1, len(lines), shard_id))
                    sys.stdout.flush()
                    image_data = tf.gfile.FastGFile(os.path.join(data_dir, lines[i][0]), 'rb').read()
                    image = sess.run(decode_jpeg, feed_dict={decode_jpeg_data: image_data})
                    height, width = image.shape[0], image.shape[1]
                    # example = dataset_utils.image_to_tfexample(
                    #     image_data, b'jpg', height, width, int(lines[i][1]))
                    # tfrecord_writer.write(example.SerializeToString())
                    example=image_to_tfexample(image_data,b'jpg',height,width,int(lines[i][1]))
                    tfrecord_writer.write(example.SerializeToString())
                tfrecord_writer.close()
    sys.stdout.write('\n')
    sys.stdout.flush()

#os.system('mkdir -p train')
convert_dataset('train','../data/list_train_licenseimage.txt', '../data/', '../data/')
#os.system('mkdir -p test')
convert_dataset('validation','../data/list_test_licenseimage.txt', '../data/', '../data/')