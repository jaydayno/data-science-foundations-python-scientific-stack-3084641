# %%
import matplotlib.pyplot as plt

img = plt.imread('flower.png')
img = img.copy()  # make img writable
plt.imshow(img)

#%%
type(img)
# %%
img.shape

# %%
# Draw a blue square around the flower
# Top-left: 190x350 (y by x)
# Bottom-right: 680x850
# Line width: 5

y_1, y_2 = 350, 850 # y-coords
x_1, x_2 = 190, 680 # x-coords
width = 5

color = [0, 0 , 0xFF]

#top of the square
img[y_1:y_1+width, x_1:x_2] = color

#left of the square
img[y_1:y_2, x_1:x_1+width] = color

#bottom of the square
img[y_2:y_2+width, x_1:x_2] = color

#right of the square
img[y_1:y_2, x_2:x_2+width] = color
plt.imshow(img)
# %%
