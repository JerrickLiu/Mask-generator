import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
import fnmatch
import random
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--image_dir', type=str, default=None)
parser.add_argument('--bg_img_dir', type=str, default=None)
args = parser.parse_args()

def mask(path):
    for root, dirs, filename in os.walk(path):
        for file in filename:
            new_path = os.path.join(root, file)
            img = cv2.imread(new_path)
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            ret, thresh = cv2.threshold(gray_img, 180, 255, cv2.THRESH_BINARY_INV) # Play around with the thresholding here 
            f, e = os.path.splitext(new_path)
            cv2.imwrite(f + 'Masked.png', thresh)


def generate_colored_background(path):

    mask(args.image_dir)

    for root, dirs, filename in os.walk(path):
        for file in filename:
            if fnmatch.fnmatch(file, '*Masked.png'):
                new_path = os.path.join(root, file)
                color = list(np.random.choice(range(256), size=3))
                img = cv2.imread(new_path)
                img[np.where(((img == [0, 0, 0]).all(axis=2)))] = color
                f, e = os.path.splitext(new_path)
                cv2.imwrite(f + 'ColoredBG.png', img)


def generate_image_as_background(path, other_img_path):

    # The background image must be the same size as your mask!!

    mask(args.image_dir)
    images = []

    for root, dirs, filename in os.walk(other_img_path):
        for file in filename:
            new_image_path = os.path.join(root, file)
            images.append(new_image_path)
    for root, dirs, filename in os.walk(path):
        for file in sorted(filename):
            bg_img = cv2.imread(random.choice(images))
            if fnmatch.fnmatch(file, '*Masked.png'):
                mask_path = os.path.join(root, file)
                masked_img = cv2.imread(mask_path)
                bg = cv2.bitwise_or(bg_img, masked_img, mask=None)
                out = bg.copy()
                out[bg == 255] = masked_img[bg == 255]
                f, e = os.path.splitext(mask_path)
                cv2.imwrite(f + 'ImageBG.png', out)


def main():
    generate_colored_background(args.image_dir)
    #generate_image_as_background(args.image_dir, args.bg_img_dir)


if __name__ == '__main__':
    main()
