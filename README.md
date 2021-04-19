# Image-Caption
project for machine learning <br />


Reference for network framework and training code: <a href="https://github.com/sgrvinod/a-PyTorch-Tutorial-to-Image-Captioning">a-PyTorch-Tutorial-to-Image-Captioning</a>. <br />
Data comes from: <a href="https://www.kaggle.com/adityajn105/flickr8k?select=Images">Flickr 8k Dataset</a> <br />


- Adding config.py to record all parameters.
- Adding data preprocessing part for specific input.
- Revised code to suit API changes of different libraries.
- Caption test revised.

**before training & testing: make sure all libraries are installed with compatible versions (requirements.txt for reference).**

### Preprocess
```
$ run create_input_files.py
```
(only once for generating intermediate data files)

### Training Process
There are two choices for training, if training without previous checkpoints, set checkpoints in config.py as None. <br />
Another one is training based on current best model (default, <a href="https://drive.google.com/drive/folders/1E3W1wKbhV20FyBfRfTXfRcjAVjoIQavp?usp=sharing">latest model checkpoints<a/>).
```
$ run train.py
```

### evaluation metrics
first install <a href="https://github.com/salaniz/pycocoevalcap"> pycocoevalcap <a/> for CIDER, SPICE metrics.(Problems still exist for SPICE after installing following <a href="https://github.com/jiasenlu/coco-caption">instructions<a/>, and others also met <a href="https://github.com/jiasenlu/NeuralBabyTalk/issues/9">the same problem<a/>)
```
$ run eval.py
```

### Testing Process
All generated captions would be stored under test_results directory. <br />
Three choices:
1. If randomly generated one caption from all inputs
```
$ run caption.py
```
2. If randomly generated multiple captions from all inputs <br />
ex. randomly select 6 images to generate caption
```
$ run caption.py --num = 6
```
3. generate caption for specified image & specified model & specified path to save<br />
ex.
```
$ python caption.py  --word_map='./inputs/Intermediate_files/WORDMAP_flickr8k_5_cap_per_img_5_min_word_freq.json' --beam_size=5 --img='./inputs/Images/2877424957_9beb1dc49a.jpg' --save='./test_results/gen_3' --model='./model_history/best_0417_20.pth.tar'
```
