# SPML HW2 Advanced Attacks

## Packages

- torch
- torchvision
- torchattacks
- pytorchcv
- numpy
- PIL
- matplotlib

## Get cifar-100-eval's labels

- Run `get_labels.ipynb` .

## Do the targeted attack and save adversarial examples

- Run `targeted_attack.ipynb` (details in the notebook)

## Do the universal attack and save UAP

- Run `universal_attack.ipynb` (details in the notebook)

## Check if the adv_images's epsilon are all below 4/255

- Run `checkEps.py` .

## Check if the UAP pixels are all in 0/255~24/255

- Run `checkUniversalEps.py` .
