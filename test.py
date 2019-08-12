from tensorflow import flags
import sys
if __name__ == "__main__" :
    FLAGS = flags.FLAGS
    flags.DEFINE_string(
        "save_path", "",
        "File glob for the training dataset. If the files refer to Frame Level "
        "features (i.e. tensorflow.SequenceExample), then set --reader_type "
        "format. The (Sequence)Examples are expected to have 'rgb' byte array "
        "sequence feature as well as a 'labels' int64 context feature.")
    path = sys.argv[0]
    with open(path+'1.txt','w') as f:
        f.write('I am a lobster')