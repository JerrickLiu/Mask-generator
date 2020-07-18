# Mask-generator
Various functions to generate masks for images and replace the background of images with a color or some other image of your choosing 

## Usage

All you need is Python's computer vision library OpenCV2 to run these functions. Specifiy the image folder where you want the mask applied to in the arguments and that's it. 

## Examples

Mask function applied to an image of an apple:
<img src="/example_masks/appleMasked.png" alt="drawing" width="350" height="300" />

Using the mask to replace all 0 value pixels (black) with a random color:
<img src="/example_masks/appleMaskedColoredBG.png" alt="drawing" width="350" height="300" />

