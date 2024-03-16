import os
import pickle
from skimage.io import imread
from skimage.transform import resize
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
input_dir = 'D:\Color_Detection\clf-data'
categories = ['empty','not_empty']
data = []
labels = []

for category_idx, category in enumerate(categories):
    for file in os.listdir(os.path.join(input_dir,category)):
        img_path = os.path.join(input_dir,category,file)
        img = imread(img_path)
        img = resize(img,(15,15))
        data.append(img.flatten())
        labels.append(category_idx)

data = np.asarray(data)
labels = np.asarray(labels)

x_train,x_test,y_train,y_test = train_test_split(data,labels,test_size=0.2,stratify=labels,shuffle=True)

classifier = SVC()
parameters = [{'gamma':[0.01,0.001,0.0001],'C':[1,10,100,1000]}]
grid_search = GridSearchCV(classifier,parameters)
grid_search.fit(x_train,y_train)

best_estimator = grid_search.best_estimator_
y_predict = best_estimator.predict(x_test)
score = accuracy_score(y_predict, y_test)
print('{}% of samples are correctly classified'.format(str(score*100)))
pickle.dump(best_estimator,open('./model.p','wb'))