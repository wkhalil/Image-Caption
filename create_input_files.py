from utils import txt_2_json, create_input_files
from config import *
import os.path

if __name__ == '__main__':
    # convert custom txt caption to karpathy json format, only once
    if not os.path.isfile(caption_json_path):
        txt_2_json(caption_txt_path, caption_json_path, train_rate, val_rate)

    # Create input files (along with word map)
    create_input_files(dataset=dataset_name,
                       karpathy_json_path= caption_json_path ,
                       image_folder= image_folder,
                       captions_per_image=captions_per_image,
                       min_word_freq= min_word_freq,
                       output_folder=output_folder,
                       max_len=max_cap_len)
