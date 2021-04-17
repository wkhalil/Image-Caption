# Image-Caption
project for machine learning <br />


Reference for network framework and training code: <a href="https://github.com/sgrvinod/a-PyTorch-Tutorial-to-Image-Captioning">a-PyTorch-Tutorial-to-Image-Captioning</a>. <br />
Data comes from: <a href="https://www.kaggle.com/adityajn105/flickr8k?select=Images">Flickr 8k Dataset</a> <br />


- Adding config.py to record all parameters.
- Adding data preprocessing part for specific input.
- Revised code to suit API changes of different libraries.
- Caption test revised.

**before training & testing: make sure all libraries are installed with compatible versions (requirements.txt for reference).**

### Training Process
1. run create_input_files.py
2. run train.py

### Testing Process
1. run caption.py <br />
(also can run by cmd iwth arguments, example: <br />
python caption.py --img='./inputs/Images/2472574160_8ce233f396.jpg' --model='BEST_checkpoint_flickr8k_5_cap_per_img_5_min_word_freq.pth.tar' --word_map='./output/WORDMAP_flickr8k_5_cap_per_img_5_min_word_freq.json' --beam_size=5
)
