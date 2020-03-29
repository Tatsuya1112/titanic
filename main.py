import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import numpy as np
from sklearn.preprocessing import LabelEncoder

trainset_path = "./train.csv"
testset_path = "./test.csv"
encoder = LabelEncoder()

# train
trainset = pd.read_csv(trainset_path)
trainset = trainset.dropna(subset=["Age", "Fare", "Sex", "Embarked", "Pclass", "SibSp", "Parch"])
trainset["Sex"] = encoder.fit_transform(trainset["Sex"])
trainset["Embarked"] = encoder.fit_transform(trainset["Embarked"])

inputs = trainset.loc[:, ["Age", "Fare", "Sex", "Embarked", "Pclass", "SibSp", "Parch"]]
labels = trainset.loc[:, ["Survived"]]

clf = DecisionTreeClassifier(max_depth=3)
clf.fit(inputs, labels)

# test
testset = pd.read_csv(testset_path)
testset = testset.fillna(train.median())
testset["Sex"] = encoder.fit_transform(testset["Sex"])
testset["Embarked"] = encoder.fit_transform(testset["Embarked"])

inputs = testset.loc[:, ["Age", "Fare", "Sex", "Embarked", "Pclass", "SibSp", "Parch"]]
predicts = clf.predict(inputs)

# submit
outputs = pd.DataFrame({"PassengerId":testset["PassengerId"], "Survived":predicts})
outputs.to_csv("submission.csv", index=False)