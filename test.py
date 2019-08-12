from tensorflow import flags
import os
if __name__ == "__main__" :
    FLAGS = flags.FLAGS
    flags.DEFINE_string(
        "save_path", "",
        "File glob for the training dataset. If the files refer to Frame Level "
        "features (i.e. tensorflow.SequenceExample), then set --reader_type "
        "format. The (Sequence)Examples are expected to have 'rgb' byte array "
        "sequence feature as well as a 'labels' int64 context feature.")

    with open(os.path.join(FLAGS.save_path, "data/1.txt"),'a+') as f:
        f.write('I am a lobster')
