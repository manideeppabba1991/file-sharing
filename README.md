# OCR for health screening

The code has tested on python3.7 on Raspberry pi. To run the script, download the file from the dropbox and install the requirements. The url is https://www.dropbox.com/s/g8pjzv2de9gty8g/TextBoxes_icdar13.caffemodel?dl=0 

## Installation

```bash
pip install -r requirements.txt
```

## Explaination

The script det.py provides the detected bounding box. You could follow the same logic to pick the best one or few bounding boxes and run ssocr algorithm on it.  

## Format

The result from the ocr package is a list. For det.py, each element is a list of four values. The structure is [topleft[x], topleft[y], width, height]. 

## Reference

In Linux, there is a ssocr library. During the testing, I found it is much better than your current ssocr algorithm written by python. Here is the instruction: https://ourcodeworld.com/articles/read/741/how-to-recognize-seven-segment-displays-content-with-ssocr-seven-segment-optical-character-recognition-in-ubuntu-1604. To run the library inside the python:

```python
os.system(“ssocr -d -1 test.png”)
```

## Contact

yilun.chen@samsclub.com
