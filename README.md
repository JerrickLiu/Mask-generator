# Mask-generator
Various functions to generate masks for images and replace the background of images with a color or some other image of your choosing 

## Usage and examples

All you need is Python's computer vision library OpenCV2 to run these functions. Specifiy the image folder where you want the mask applied to in the arguments and that's it. 

Once done, the code first generates a mask for the image by thresholding. Certain values above a threshold turn to white pixels and other values below a threshold turn to black pixesl. Play around with the thresholding for your specific images. 

Here are a few examples with a mask applied to an image of an apple then replacing all 0 valued pixels (black) to be a different color:


<img src="/example_masks/apple.png" alt="drawing" width="350" height="300" />

<img src="/example_masks/appleMaskedMaskedFinal.png" alt="drawing" width="350" height="300" />

<img src="/example_masks/appleMaskedMaskedFinalColoredBG.png" alt="drawing" width="350" height="300" />

