from sklearn.ensemble import RandomForestClassifier
import cv2
import numpy as np
import pickle

rf = pickle.load(open('outputs/random_forest_intel.pkl', 'rb'))
pca = pickle.load(open('outputs/pca_intel.pkl','rb'))
encoder = pickle.load(open('outputs/enconder_intel.pkl','rb'))

img_to_predict = cv2.imread('datasets/intel_images/seg_pred/72.jpg')
img_to_predict = cv2.cvtColor(img_to_predict, cv2.COLOR_BGR2RGB)
img_to_predict = cv2.resize(img_to_predict, (50,50))
img_to_predict = img_to_predict.flatten().reshape(1, -1)

pca_image = pca.transform(img_to_predict)

print(pca_image)

labels = rf.predict(pca_image)
# labels = encoder.inverse_transform(labels)
print(labels)