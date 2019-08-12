# from tensorflow import flags
# import os
# if __name__ == "__main__" :
#     FLAGS = flags.FLAGS
#     flags.DEFINE_string(
#         "save_path", "",
#         "File glob for the training dataset. If the files refer to Frame Level "
#         "features (i.e. tensorflow.SequenceExample), then set --reader_type "
#         "format. The (Sequence)Examples are expected to have 'rgb' byte array "
#         "sequence feature as well as a 'labels' int64 context feature.")
#
#     with open(os.path.join(FLAGS.save_path, "data/1.txt"),'a+') as f:
#         f.write('I am a lobster')


import logging
import os
import cloudstorage as gcs
import webapp2

from google.appengine.api import app_identity


def create_file(filename):
  """Create a file.

  The retry_params specified in the open call will override the default
  retry params for this particular file handle.

  Args:
    filename: filename.
  """

  write_retry_params = gcs.RetryParams(backoff_factor=1.1)
  gcs_file = gcs.open(filename,
                      'w',
                      content_type='text/plain',
                      options={'x-goog-meta-foo': 'foo',
                               'x-goog-meta-bar': 'bar'},
                      retry_params=write_retry_params)
  gcs_file.write('abcde\n')
  gcs_file.write('f'*1024*4 + '\n')
  gcs_file.close()


if __name__ =='__main__':
    create_file('1.txt')