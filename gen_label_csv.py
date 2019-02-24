import os
import math
import numpy as np
import pandas as pd
import os.path as osp
from tqdm import tqdm

label_warp = {'AcneandRosaceaPhotos': 0,
              'ActinicKeratosisBasalCellCarcinomaandotherMalignantLesions': 1,
              'AtopicDermatitisPhotos': 2,
              'BullousDiseasePhotos': 3,
              'CellulitisImpetigoandotherBacterialInfections': 4,
              'EczemaPhotos': 5,
              'ExanthemsandDrugEruptions': 6,
              'HairLossPhotosAlopeciaandotherHairDiseases': 7,
              'HerpesHPVandotherSTDsPhotos': 8,
              'LightDiseasesandDisordersofPigmentation': 9,
              'LupusandotherConnectiveTissuediseases': 10,
              'MelanomaSkinCancerNeviandMoles': 11,
              'NailFungusandotherNailDisease':12,
              'PoisonIvyPhotosandotherContactDermatitis':13,
              'PsoriasispicturesLichenPlanusandrelateddiseases':14,
              'ScabiesLymeDiseaseandotherInfestationsandBites':15,
              'SeborrheicKeratosesandotherBenignTumors':16,
              'SystemicDisease':17,
              'TineaRingwormCandidiasisandotherFungalInfections':18,
              'UrticariaHives':19,
              'VascularTumors':20,
              'VasculitisPhotos':21,
              'WartsMolluscumandotherViralInfections':22,
              }

# train data
data_path = 'data/train'
img_path, label = [], []

for first_path in os.listdir(data_path):
    dermatosis_label = first_path
    first_path = osp.join(data_path, first_path)
    for img in os.listdir(first_path):
        if 'DS_Store' not in img:
            img_path.append(osp.join(first_path, img))
            label.append(dermatosis_label)

label_file = pd.DataFrame({'img_path': img_path, 'label': label})
label_file['label'] = label_file['label'].map(label_warp)

label_file.to_csv('data/label.csv', index=False)

# test data
test_data_path = 'data/test'
#test_img_path = []
#for first_path in os.listdir(test_data_path):
#    first_path = osp.join(test_data_path, first_path)
#    for img in os.listdir(first_path):
#        if 'DS_Store' not in img:
#            test_img_path.append(osp.join(first_path, img))
all_test_img = os.listdir(test_data_path)
test_img_path = []

for img in all_test_img:
    if osp.splitext(img)[1] == '.jpg':
        test_img_path.append(osp.join(test_data_path, img))


test_file = pd.DataFrame({'img_path': test_img_path})
test_file.to_csv('data/test.csv', index=False)
