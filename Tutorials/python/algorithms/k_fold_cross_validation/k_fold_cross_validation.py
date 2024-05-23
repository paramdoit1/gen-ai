from unicodedata import digit
from sklearn.datasets import load_digits
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

from sklearn.model_selection import cross_val_score, KFold, StratifiedKFold

digits  = load_digits()

logistic_reg_cross_val_score = cross_val_score(LogisticRegression(solver = 'lbfgs', max_iter=9000),
digits.data, digits.target, cv=4)

random_forest_cross_val_score = cross_val_score(RandomForestClassifier(n_estimators=50),
digits.data, digits.target, cv=4)

svc_cross_val_score = cross_val_score(SVC(gamma='auto'),
digits.data, digits.target, cv=4)

print('logistic_reg_cross_val_score: ', logistic_reg_cross_val_score)
print('random_forest_cross_val_score: ', random_forest_cross_val_score)
print('svc_cross_val_score: ', svc_cross_val_score)

k_folds = KFold(n_splits=4)

logistic_reg_cross_val_score_k_fold = cross_val_score(LogisticRegression(solver = 'lbfgs', max_iter=9000),
digits.data, digits.target, cv=k_folds)

random_forest_cross_val_score_k_fold = cross_val_score(RandomForestClassifier(n_estimators=50),
digits.data, digits.target, cv=k_folds)

svc_cross_val_score_k_fold = cross_val_score(SVC(gamma='auto'),
digits.data, digits.target, cv=k_folds)

print('logistic_reg_cross_val_score_k_fold: ', logistic_reg_cross_val_score_k_fold)
print('random_forest_cross_val_score_k_fold: ', random_forest_cross_val_score_k_fold)
print('svc_cross_val_score_k_fold: ', svc_cross_val_score_k_fold)

s_folds = StratifiedKFold(n_splits=4)

logistic_reg_cross_val_score_s_fold = cross_val_score(LogisticRegression(solver = 'lbfgs', max_iter=9000),
digits.data, digits.target, cv=s_folds)

random_forest_cross_val_score_s_fold = cross_val_score(RandomForestClassifier(n_estimators=50),
digits.data, digits.target, cv=s_folds)

svc_cross_val_score_s_fold = cross_val_score(SVC(gamma='auto'),
digits.data, digits.target, cv=s_folds)

print('logistic_reg_cross_val_score_s_fold: ', logistic_reg_cross_val_score_s_fold)
print('random_forest_cross_val_score_s_fold: ', random_forest_cross_val_score_s_fold)
print('svc_cross_val_score_s_fold: ', svc_cross_val_score_s_fold)
