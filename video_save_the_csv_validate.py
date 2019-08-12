import tensorflow as tf
import csv

def save():
    tfrecords = open('video_validate_url.txt').read().split(',')
    with open('video_validateInfo.csv','a+') as c:
        for tfrecord in tfrecords:
            vid_lvl_record = 'gs://youtube8m-ml-us-east1/2/video/validate/validate%s.tfrecord'%(tfrecord)
            for example in tf.python_io.tf_record_iterator(vid_lvl_record):
                tf_example = tf.train.Example.FromString(example)
                sub_vid_id = tf_example.features.feature['id'].bytes_list.value[0].decode(encoding='UTF-8')
                sub_label = tf_example.features.feature['labels'].int64_list.value
                csv_writer = csv.writer(c)
                csv_writer.writerow([sub_vid_id,sub_label])

if __name__ == '__main__':
    save()