import os
import cv2
import numpy as np

if __name__ == '__main__':

    # Data transfer
    os.system('python -u ./Data_Transfer/tools/main.py --config-file ./Data_Transfer/configs/ourdata.yaml')

    # Traditional pre-processing
    os.system('python ./Traditional_Preprocessing/main.py \
                    --input_path ./input_image \
                    --output_path ./preprocess_result ')
    # crop images
    preprocessed_imgs = os.listdir('./preprocess_result')
    for i in preprocessed_imgs:
        img = cv2.imread(os.path.join('preprocess_result', i))
        img = cv2.resize(img, (512, 512))
        cv2.imwrite(i, img)

        # PSFRGAN
        os.system('python PSFRGAN/test_enhance_single_unalign.py \
                        --test_img_path' + os.path.join('preprocess_result', i) +
                        '--results_dir dl_result \
                        --gpus 1')
