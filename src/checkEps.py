import os
from PIL import Image
import numpy as np

epsilon_threshold = 5
def calculate_epsilon(img_path1, img_path2):
   
    img1 = Image.open(img_path1)
    img2 = Image.open(img_path2)
    if img1.size != img2.size:
        return False, "Image sizes are different.", 0

    img1_array = np.array(img1).astype(float)
    img2_array = np.array(img2).astype(float)
    
    diff = np.abs(img1_array - img2_array)
    max_diff = np.max(diff) 

    is_below_epsilon = max_diff <= epsilon_threshold
    return is_below_epsilon, max_diff

def compare_folders_epsilon(folder1, folder2,ok):
    comparison_results = {}

    for file in files1:
        img1_path = os.path.join(folder1, file)
        img2_path = os.path.join(folder2, file)
        
        if os.path.isfile(img1_path) and os.path.isfile(img2_path):
            is_below_epsilon, max_diff = calculate_epsilon(img1_path, img2_path)
            if is_below_epsilon:
                ok+=1
            comparison_results[file] = (is_below_epsilon, max_diff)
        else:
            comparison_results[file] = (False, "Matching file not found or one is not a file.", 0)
    
    return comparison_results,ok

original_folder = '/home/adl/Desktop/zenn/SPML/HW2/eval_500'
adversarial_folder = '/home/adl/Desktop/zenn/SPML/HW2/adv_imgs'
files1 = os.listdir(original_folder)
files1.sort()  

ok = 0

results,ok = compare_folders_epsilon(original_folder, adversarial_folder,ok)

for img_name, (is_below_epsilon, max_diff) in results.items():
    print(f"{img_name}: Epsilon <= {epsilon_threshold}: {is_below_epsilon}, Maximum Difference: {max_diff}")

print(ok,"/500 checked")