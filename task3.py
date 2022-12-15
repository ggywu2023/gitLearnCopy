from deconvolution import Deconvolution
from PIL import Image

original = Image.open('image_003.jpg')
# Create a deconvolution object with the image
dec = Deconvolution(image=original, basis=[[0.91, 0.38, 0.71], [0.39, 0.47, 0.85], [1, 0, 0]])

# Produce density matrices for both colors. Be aware, as Beer's law do not always hold.
first_density, second_density, third_density = dec.out_scalars()
print(first_density.shape, second_density.shape, third_density.shape)