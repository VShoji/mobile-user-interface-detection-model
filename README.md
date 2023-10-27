# User Interface Element Detection for Phones using YOLOv7 for the Apprender Project

<p>This repository contains the weights and a script that converts images from the RICO dataset to a format compatinble with YOLOv7.</p>

[Link to the dataset](https://interactionmining.org/rico)</br>
[Link to YOLOv7](https://github.com/WongKinYiu/yolov7)

## Why is the Apprender Project important?

[The Apprender Project](https://github.com/VShoji/apprender-research "Apprender Research") aims to assist people who have difficulties when learning how to use new technologies, such as the elderly and individuals who have little experience with electronic devices, when using mobile devices.</br>

To request assistance, the user would input a task they want to complete, such as logging in, posting a photo or adding a new phone number, after which the app would automatically identify what kind of page the user is in (like dashboards, login pages, posts and profile pages) and give instructions on how to complete the task.</br>

This repository contains the weights of a YOLOv7 model that identifies multiple types of UI elements in mobile devices.</br>
The types include:
- Advertisement
- Background Image
- Bottom Navigation
- Button Bar
- Card
- Checkbox
- Date Picker
- Drawer
- Icon
- Input
- List Item
- Map View
- Modal
- Multi-Tab
- Number Stepper
- On/Off Switch
- Pager Indicator
- Radio Button
- Text
- Text Button
- Video

## How to set up training

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
- Run the script to convert the dataset
```
python convert.py
```
- Follow YOLOv7's instructions to start training
