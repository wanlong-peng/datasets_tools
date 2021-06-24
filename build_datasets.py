#from peng import config
from imutils import paths
import random
import shutil
import os

os.chdir('/Users/pengwanlong/Desktop/Pyimagesearch2021/datasets_handle')
class Config:
    ORIG_INPUT_DATASET = os.path.join("datasets", "orig")
    BASE_PATH = os.path.join("datasets", "idc")

    # derive the training, validation, and testing directories
    TRAIN_PATH = os.path.sep.join([BASE_PATH, "training"])
    VAL_PATH = os.path.sep.join([BASE_PATH, "validation"])
    TEST_PATH = os.path.sep.join([BASE_PATH, "testing"])

    TRAIN_SPLIT = 0.8
    VAL_SPLIT = 0.1

    # define input image spatial dimensions
    IMAGE_SIZE = (48, 48)

    # initialize our number of epochs, early stopping patience, initial
    # learning rate, and batch size
    NUM_EPOCHS = 40
    EARLY_STOPPING_PATIENCE = 5
    INIT_LR = 1e-2
    BS = 128
config =Config

imagePaths = list(paths.list_images(config.ORIG_INPUT_DATASET))
random.seed(18)
random.shuffle(imagePaths)

i = int(len(imagePaths)*config.TRAIN_SPLIT)
trainPaths = imagePaths[:i]
testPaths = imagePaths[i:]

i = int(len(trainPaths)*config.VAL_SPLIT)
valPaths = trainPaths[:i]
tarinPaths = trainPaths[i:]

datasets = [
('training',trainPaths,config.TRAIN_PATH),
('testing',testPaths,config.TEST_PATH),
('validation',valPaths,config.VAL_PATH)
]

for (dTpye, imagePaths,baseOutput) in datasets:
    print("[INFO] building '{}' split".format(dTpye))

    if not os.path.exists(baseOutput):
        print("[INFO] building '{}' split".format(baseOutput))
        os.makedirs(baseOutput)

    for inputPath in imagePaths:
        filename = inputPath.split(os.path.sep)[-1]
        label = filename[-5:-4]

        #建立标签路径
        labelPath = os.path.sep.join([baseOutput,label])

        if not os.path.exists(labelPath):
            print("[INFO] building '{}' split".format(labelPath))
            os.makedirs(labelPath)
        
        #将图片从原始路径拷贝到已建立的标签路径里
        tarPath = os.path.sep.join([labelPath,filename])
        shutil.copy2(inputPath,tarPath)