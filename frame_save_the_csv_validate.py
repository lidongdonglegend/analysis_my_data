import tensorflow as tf
import csv
import concurrent.futures

def down_load_validate_data():
    tfrecords = open('frame_validate_url.txt').read().split(',')
    with open('frame_validateInfo.csv','a+') as c:
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



