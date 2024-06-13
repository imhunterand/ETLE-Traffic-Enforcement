import os
import cv2

def preprocess_images(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        img_path = os.path.join(input_dir, filename)
        img = cv2.imread(img_path)
        resized_img = cv2.resize(img, (224, 224))
        output_path = os.path.join(output_dir, filename)
        cv2.imwrite(output_path, resized_img)

if __name__ == "__main__":
    preprocess_images('raw_data/violations', 'data/violations')
