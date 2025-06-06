import warnings
warnings.filterwarnings("ignore")

import os
import logging

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
os.environ["PATH"] = r"C:\Users\tinal\.conda\envs\paddle_env\Library\bin;" + os.environ["PATH"]

logging.getLogger().setLevel(logging.ERROR)
logging.getLogger("ppocr").setLevel(logging.ERROR)

from paddleocr import PaddleOCR, draw_ocr


# Paddleocr supports Chinese, English, French, German, Korean and Japanese
# You can set the parameter `lang` as `ch`, `en`, `french`, `german`, `korean`, `japan`
# to switch the language model in order
ocr = PaddleOCR(use_angle_cls=True, lang='ch') # need to run only once to download and load model into memory
img_path = 'C:/Users/tinal/Desktop/PaddleOCR/ppocr_img/ch/ch.jpg'
result = ocr.ocr(img_path, cls=True)
for idx in range(len(result)):
    res = result[idx]
    for line in res:
        print(line)

# draw result
from PIL import Image
result = result[0]
image = Image.open(img_path).convert('RGB')
boxes = [line[0] for line in result]
txts = [line[1][0] for line in result]
scores = [line[1][1] for line in result]
im_show = draw_ocr(image, boxes, txts, scores, font_path='/path/to/PaddleOCR/doc/fonts/simfang.ttf')
im_show = Image.fromarray(im_show)
im_show.save('result.jpg')