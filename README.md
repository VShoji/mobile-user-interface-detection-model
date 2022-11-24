# User Interface Element Detection for Phones using YOLO v7

<p>This repository contains the weights, some examples of detected elements on different apps and a jupyter notebook that contains an script that converts images from the RICO dataset to a format compatinble with YOLO v7.</p>

<p>Link to the dataset: https://interactionmining.org/rico</p>
<p>Link to YOLO v7:     https://github.com/WongKinYiu/yolov7</p>

## Conversion setup

- Download the "UI Screenshots and View Hierarchies" and "UI Screenshots and Hierarchies with Semantic Annotations" files at: https://interactionmining.org/rico
- Unzip files
- Clone YOLOv7 (https://github.com/WongKinYiu/yolov7)
- Set up the folder like this:
```
.
├───combined
├───dataset
│   ├───test
│   │   ├───images
│   │   └───labels
│   ├───train
│   │   ├───images
│   │   └───labels
│   └───valid
│       ├───images
│       └───labels
├───semantic_annotations
└───yolov7
```
- Install requirements.txt with:
```
pip install -r requirements.txt
```
- Run the script
```
python convert.py
```
- YOLOv7's instructions to start training