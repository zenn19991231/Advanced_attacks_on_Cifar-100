
from PIL import Image
import numpy as np

image_path = "/home/adl/Desktop/zenn/SPML/HW2/universarial.png"  
image = Image.open(image_path)
pixels = np.array(image)

lower_bound = np.array([0, 0, 0])  
upper_bound = np.array([24, 24, 24])  

in_range = np.all((pixels >= lower_bound) & (pixels <= upper_bound), axis=-1)

all_in_range = np.all(in_range)

print("All pixels within range:", all_in_range)
