# Advanced attacks on Cifar-100

## Targeted Attack
### PGD targeted attack success rate: 94.4%
### Targeted attack success rates under different model
<img src = "https://github.com/zenn19991231/Advanced_attacks_on_Cifar-100/blob/main/results/targeted_examples/adversarial%20attack%20success%20rates%20by%20model.png" width="700" height="350">

### Images before and after the attack
<img src = "https://github.com/zenn19991231/Advanced_attacks_on_Cifar-100/blob/main/results/targeted_examples/targeted.png" width="700" height="350">

## Universal Attack
### Lowered resnet20’s accuracy to 3.5%
<img src = "https://github.com/zenn19991231/Advanced_attacks_on_Cifar-100/blob/main/results/universal_examples/universal.png" width="700" height="250">

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
