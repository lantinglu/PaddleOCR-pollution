from paddleocr import PaddleOCR
import warnings
warnings.filterwarnings("ignore")

import os
import logging

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
os.environ["PATH"] = r"C:\Users\tinal\.conda\envs\paddle_env\Library\bin;" + os.environ["PATH"]

logging.getLogger().setLevel(logging.ERROR)
logging.getLogger("ppocr").setLevel(logging.ERROR)
ocr = PaddleOCR(use_angle_cls=True, use_gpu=False, lang='ch')  # 中文模式 Chinese mode
pdf_path = r"D:\UW\大三\复旦\污染物\环保源文件\1、排污许可证\1、鸿丰化工-排污许可证.pdf"
result = ocr.ocr(pdf_path, page_num=2)

with open("result.txt", "w", encoding="utf-8") as f:
    for page in result:
        for line in page:
            f.write(line[1][0] + "\n")
