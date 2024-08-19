import pandas as pd

from sklearn import svm
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score, GridSearchCV, RandomizedSearchCV

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

iris = load_iris()

cross_val_score_svm_1 = cross_val_score(svm.SVC(kernel = 'linear',gamma='auto', C=10), iris.data, iris.target, cv=5)
cross_val_score_svm_2 = cross_val_score(svm.SVC(kernel = 'rbf',gamma='auto', C=10), iris.data, iris.target, cv=5)
cross_val_score_svm_3 = cross_val_score(svm.SVC(kernel = 'rbf',gamma='auto', C=20), iris.data, iris.target, cv=5)

print('cross_val_score_1: ', cross_val_score_svm_1)
print('cross_val_score_2: ', cross_val_score_svm_2)
print('cross_val_score_3: ', cross_val_score_svm_3)

clf = GridSearchCV(svm.SVC(gamma='auto'), {
    'kernel': ['linear', 'rbf'],
    'C' : [10,20]
}, cv = 5, return_train_score= False)

clf.fit(iris.data, iris.target)
print(clf.cv_results_)


df = pd.DataFrame(clf.cv_results_)
df = df[['param_C', 'param_kernel', 'mean_test_score']]

print('Data Frame: ', df)
print('Best Score: ', clf.best_score_)
print('Best Parameters: ', clf.best_params_)

#Ramdomized Search CV

clf1 = RandomizedSearchCV(svm.SVC(gamma='auto'), {
    'kernel': ['linear', 'rbf'],
    'C' : [10,20]
}, cv = 5, return_train_score= False, n_iter=2)

clf1.fit(iris.data, iris.target)

df_random_cv = pd.DataFrame(clf1.cv_results_)
df_random_cv = df_random_cv[['param_C', 'param_kernel', 'mean_test_score']]

print('Data Frame df_random_cv:\n ', df_random_cv)


model_params = {
"svm" : {
    'model': svm.SVC(gamma='auto'), 
    'params': {
        'kernel': ['linear', 'rbf'],
        'C' : [1, 10,20]
    }
},
"random_forest" : {
    'model': RandomForestClassifier(), 
    'params': {
        'n_estimators' : [1,5,10,20,50,60, 80]
    }
},
"logistic_regression" : {
    'model': LogisticRegression(solver= 'liblinear', multi_class='auto'), 
    'params': {
        'C' : [1,5,20,30, 50,60]
    }
}
}

scores = []

for model_name, parameter in model_params.items():
    clf = GridSearchCV(parameter['model'], parameter['params'], cv =5, return_train_score=False)
    clf.fit(iris.data, iris.target)
    scores.append({
        'model' : model_name,
        'best_score': clf.best_score_,
        'best_params': clf.best_params_
    })

df_final = pd.DataFrame(scores, columns=['model', 'best_score', 'best_params'])
print('df_final: \n ', df_final)