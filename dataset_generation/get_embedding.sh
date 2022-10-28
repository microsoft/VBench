# reference: https://github.com/torralba-lab/im2recipe-Pytorch
echo "Cloning source code..."
git clone --branch benchmark https://github.com/suiguoxin/im2recipe-Pytorch.git

echo "Downloading pretrained model..."
mkdir im2recipe-Pytorch/snapshots
# `model_e220_v-4.700.pth.tar` should be better than model_e500_v-8.950.pth.tar
wget http://data.csail.mit.edu/im2recipe/model_e220_v-4.700.pth.tar -P im2recipe-Pytorch/snapshots

gzip -d data/vocab.bin.gz
mkdir data/train
tar -xvf data/train.tar -C data/train/
mkdir data/val
tar -xvf data/val.tar -C data/val/
mkdir data/test
tar -xvf data/test.tar -C data/test/
mkdir data/recipe1M_images_train
tar -xvf data/recipe1M_images_train.tar -C data/recipe1M_images_train/
mkdir data/recipe1M_images_val
tar -xvf data/recipe1M_images_val.tar -C data/recipe1M_images_val/
mkdir data/recipe1M_images_test
tar -xvf data/recipe1M_images_test.tar -C data/recipe1M_images_test/

echo "Installing dependencies..."
cd im2recipe-Pytorch
python -m pip install -r requirements.txt
python -m pip install torchwordemb==0.0.9

echo "Getting embedding..."
# change `torchvision.transforms.Scale` to `torchvision.transforms.Resize` in `test.py` if necessary
# https://discuss.pytorch.org/t/attributeerror-module-torchvision-transforms-has-no-attribute-scale/146687
# test
mkdir -p results/test
python test.py \
--ingrW2V ../data/vocab.bin \
--model_path=snapshots/model_e220_v-4.700.pth.tar \
--img_path ../data/recipe1M_images_test/test \
--data_path ../data/test/ \
--path_results results/test/ \
--batch_size 10 \
--partition "test"

# val
mkdir -p results/val
python test.py \
--ingrW2V ../data/vocab.bin \
--model_path=snapshots/model_e220_v-4.700.pth.tar \
--img_path ../data/recipe1M_images_val/val \
--data_path ../data/val/ \
--path_results results/val/ \
--batch_size 80 \
--partition "val"

# train
mkdir -p results/train
python test.py \
--ingrW2V ../data/vocab.bin \
--model_path=snapshots/model_e220_v-4.700.pth.tar \
--img_path ../data/recipe1M_images_train/train \
--data_path ../data/train/ \
--path_results results/train/ \
--batch_size 80 \
--partition "train"

echo "Evaluating..."
cd scripts
python rank.py --path_results=../results/test
# Mean median 4.85, Recall {1: 0.24749999999999997, 5: 0.5231, 10: 0.6468999999999999}
python rank.py --path_results=../results/val
# Mean median 4.8, Recall {1: 0.25110000000000005, 5: 0.5273999999999999, 10: 0.6493}
python rank.py --path_results=../results/train
# Mean median 2.0, Recall {1: 0.44160000000000005, 5: 0.7532, 10: 0.8453000000000002}
