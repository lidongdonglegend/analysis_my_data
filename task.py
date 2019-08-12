import frame_save_the_csv_train
import frame_save_the_csv_test
import frame_save_the_csv_validate
import video_save_the_csv_train
import video_save_the_csv_test
import video_save_the_csv_validate

if __name__ == '__main__':
    frame_save_the_csv_train.down_load_the_info()
    frame_save_the_csv_test.save()
    frame_save_the_csv_validate.down_load_validate_data()
    video_save_the_csv_train.save()
    video_save_the_csv_test.save()
    video_save_the_csv_validate.save()