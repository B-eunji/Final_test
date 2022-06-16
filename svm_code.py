from sklearn.datasets import load_wine
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.model_selection import RandomizedSearchCV

# wine �����ͼ� �о����
wine = load_wine()

# feature, target ����
wine_data = wine.data
wine_target = wine.target

# train������, test ������ ����
x_train, x_test, y_train, y_test = train_test_split(wine_data, wine_target, 
                                                    random_state = 0, train_size = 0.2)

#Ž�� ���� ����
random_search = {
               'C': [0.1, 0.5, 1.0, 1.5, 2.0, 10, 100],
               'gamma': [0.1, 0.5, 1.0, 1.5, 2.0, 10, 100],
               'kernel': ['linear', 'sigmoid', 'rbf'] 
               }


#RandomizedSearchCV�� �̿��� ��ü ����
random_search = RandomizedSearchCV(SVC(), random_search, cv=5)

#random_search �� �н�
random_search.fit(x_train,y_train)

#��� ���
print("test set score: {}".format(random_search.score(x_test, y_test)))

print("���� ������ �Ķ���� : {}".format(random_search.best_params_))
print("���� ������ ���ھ� ��: {}".format(random_search.best_score_))