from sklearn.datasets import load_wine
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# wine �����ͼ� �о����
wine = load_wine()

# feature, target ����
wine_data = wine.data
wine_target = wine.target

# train������, test ������ split
x_train, x_test, y_train, y_test = train_test_split(wine_data, wine_target, 
                                                    random_state = 0, train_size = 0.2)
# �� ����
svm_model = svm.SVC(C=1, gamma=0.1, kernel='linear')
svm_model.fit(x_train,y_train)

# ����
pred = svm_model.predict(x_test)

# svm��Ȯ�� Ȯ��
svm_accuracy = accuracy_score(y_test, pred)
print("svm�� ��Ȯ��: " ,svm_accuracy) 