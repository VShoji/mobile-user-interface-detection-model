import os
from PIL import Image
import json
import pandas as pd
import numpy as np
from tqdm import tqdm
from collections import Counter
import matplotlib.pyplot as plt

def get_childr_labels(comp : dict):
    lbs = []
    bxs = []

    try:
        if '$' not in comp['componentLabel'] and 'Web View' not in comp['componentLabel']:
          lbs = [comp['componentLabel']]
          bxs = [comp['bounds']]

        children = []
        if 'children' in comp.keys():
          children = comp['children']

        for c in children:
          labels, boxes = get_childr_labels(c)
          lbs.extend(labels)
          bxs.extend(boxes)
    except:
      pass

    return lbs, bxs

def open_json(path):
  labels = []
  boxes = []

  with open(path) as file:
    try:
      data = json.load(file)
      df = pd.json_normalize(data)
      for ch in df['children'][0]:
        lbs, bxs = get_childr_labels(ch)
        labels.extend(lbs)
        boxes.extend(bxs)
    except:
      pass
  
  return labels, boxes

def save_split(split, dest_folder, label_dict):
  images_folder = './combined'
  data_folder = './semantic_annotations'

  for idx in tqdm(split):
    img = Image.open(os.path.join(images_folder, idx.__str__() + '.jpg'))
    img.save(os.path.join(dest_folder, 'images', idx.__str__() + '.jpg'))
    labels, boxes = open_json(os.path.join(data_folder, idx.__str__() + '.json'))
    with open(os.path.join(dest_folder, 'labels', idx.__str__() + '.txt'), 'w') as f:
      for lb_idx in range(labels.__len__()):
        try:
          box = boxes[lb_idx]
          w = box[2] - box[0]
          h = box[3] - box[1]
          xmid = ((w / 2) + box[0]) / 1440
          ymid = ((h / 2) + box[1]) / 2560
          nw = w / 1440
          nh = h / 2560
          string = label_dict[labels[lb_idx]].__str__() + ' ' + xmid.__str__() + ' ' + ymid.__str__() + ' ' + nw.__str__() + ' ' + nh.__str__() + '\n'
          f.write(string)
        except:
          pass

def main():
    data_folder = './semantic_annotations'
    num_files = 72218
    valid_files = []
    allLabels = []

    for idx in tqdm(range(num_files + 1)):
        filename = idx.__str__() + '.json'
        try:
            lbs, _ = open_json(os.path.join(data_folder, filename))
            allLabels.extend(lbs)
            valid_files.append(idx)
        except FileNotFoundError:
            pass

    label_dict = { }
    allKeys = np.unique(allLabels)
    for idx in range(allKeys.__len__()):
        label_dict[allKeys[idx]] = idx

    valid_files = np.array(valid_files)
    np.random.shuffle(valid_files)
    train_split, validation_split, test_split  = np.split(valid_files, [int(.6*len(valid_files)), int(.8*len(valid_files))])

    train_folder = './dataset/train'
    test_folder = './dataset/test'
    validation_folder = './dataset/valid'

    save_split(train_split, train_folder, label_dict)
    save_split(validation_split, validation_folder, label_dict)
    save_split(test_split, test_folder, label_dict)

if __name__ == '__main__':
    main()