#------------------------train----------------
import tensorflow as tf
import csv
import concurrent.futures

def down_load_the_info():
    tfrecords = open('/home/analysis/frame_level/save_the_urls/train_url.txt').read().split(',')
    a = 0
    for i in range(1,20):
        for tfrecord in tfrecords[(i-1)*200:i*200]:
            with open('trainInfo_download/trainInfo%s.csv'%i,'a+') as c:
                vid_lvl_record = 'gs://youtube8m-ml-us-east1/2/frame/train/train%s.tfrecord'%(tfrecord)
                for example in tf.python_io.tf_record_iterator(vid_lvl_record):
                    tf_example = tf.train.Example.FromString(example)
                    sub_vid_id = tf_example.features.feature['id'].bytes_list.value[0].decode(encoding='UTF-8')
                    sub_label = tf_example.features.feature['labels'].int64_list.value
                    csv_writer = csv.writer(c)
                    csv_writer.writerow([sub_vid_id,sub_label])
        a+=1
        print(a)
        print('download %s/20 files'%a)
    for tfrecord in tfrecords[19 * 200:]:
        with open('trainInfo_download/trainInfo20.csv','a+') as c:
            vid_lvl_record = 'gs://youtube8m-ml-us-east1/2/frame/train/train%s.tfrecord' % (tfrecord)
            for example in tf.python_io.tf_record_iterator(vid_lvl_record):
                tf_example = tf.train.Example.FromString(example)
                sub_vid_id = tf_example.features.feature['id'].bytes_list.value[0].decode(encoding='UTF-8')
                sub_label = tf_example.features.feature['labels'].int64_list.value
                csv_writer = csv.writer(c)
                csv_writer.writerow([sub_vid_id, sub_label])
    a+=1
    print(a)
    print('download %s/20 files' % a)

if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.submit(down_load_the_info)

#----------------train部分第二种--------------------
import tensorflow as tf
import csv
import concurrent.futures

def down_load_train_data():
    tfrecords = open('/home/analysis/frame_level/save_the_urls/train_url.txt').read().split(',')
    with open('trainInfo.csv','a+') as c:
        a = 1
        for tfrecord in tfrecords:
            print(a)
            a+=1
            vid_lvl_record = 'gs://youtube8m-ml-us-east1/2/frame/train/train%s.tfrecord'%(tfrecord)
            for example in tf.python_io.tf_record_iterator(vid_lvl_record):
                tf_example = tf.train.Example.FromString(example)
                sub_vid_id = tf_example.features.feature['id'].bytes_list.value[0].decode(encoding='UTF-8')
                sub_label = tf_example.features.feature['labels'].int64_list.value
                csv_writer = csv.writer(c)
                csv_writer.writerow([sub_vid_id,sub_label])

if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.submit(down_load_train_data)



#----------------validate部分-----------------


import tensorflow as tf
import csv

def down_load_validate_data():
    tfrecords = open('/home/analysis/video_level/save_the_urls/validate_url.txt').read().split(',')
    with open('validateInfo.csv','a+') as c:
        a = 1
        for tfrecord in tfrecords:
            print(a)
            a+=1
            vid_lvl_record = 'gs://youtube8m-ml-us-east1/2/video/validate/validate%s.tfrecord'%(tfrecord)
            for example in tf.python_io.tf_record_iterator(vid_lvl_record):
                tf_example = tf.train.Example.FromString(example)
                sub_vid_id = tf_example.features.feature['id'].bytes_list.value[0].decode(encoding='UTF-8')
                sub_label = tf_example.features.feature['labels'].int64_list.value
                csv_writer = csv.writer(c)
                csv_writer.writerow([sub_vid_id,sub_label])

if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.submit(down_load_validate_data)



#----------------test部分------------------

import tensorflow as tf
import csv
tfrecords = open('/home/analysis/video_level/save_the_urls/test_url.txt').read().split(',')
with open('testInfo.csv','a+') as c:
    for tfrecord in tfrecords:
        vid_lvl_record = 'gs://youtube8m-ml-us-east1/2/video/test/test%s.tfrecord'%(tfrecord)
        for example in tf.python_io.tf_record_iterator(vid_lvl_record):
            tf_example = tf.train.Example.FromString(example)
            sub_vid_id = tf_example.features.feature['id'].bytes_list.value[0].decode(encoding='UTF-8')
            sub_label = tf_example.features.feature['labels'].int64_list.value
            csv_writer = csv.writer(c)
            csv_writer.writerow([sub_vid_id,sub_label])

