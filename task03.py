from deconvolution import Deconvolution
from PIL import Image

# Load an image
original = Image.open("image_003.jpg")
# Create a deconvolution object with the image basis=[[1, 0.1, 0.2], [0, 0.1, 0.8]]
dec = Deconvolution(image=original, basis=[[1, 0, 0], [0.01, 0.13, 0.01], [0, 0, 1]])

# Produce reconstructed image, first layer, second layer, and rest
out_image1, out_image2, out_image3, out_image4 = dec.out_images(mode=[0, 1, 2, -1])
out_image2.show()
out_image3.show()