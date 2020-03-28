import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import numpy as np

train_path = "./train.csv"
test_path = "./test.csv"

# train
train = pd.read_csv(train_path)
train = train.dropna(subset=["Age", "Fare", "Sex", "Embarked", "Pclass", "SibSp", "Parch"])

encoder = LabelEncoder()
train["Sex"] = encoder.fit_transform(train["Sex"])
train["Embarked"] = encoder.fit_transform(train["Embarked"])

inputs = train.loc[:, ["Age", "Fare", "Sex", "Embarked", "Pclass", "SibSp", "Parch"]]
labels = train.loc[:, ["Survived"]]

clf = DecisionTreeClassifier(max_depth=3)
clf.fit(inputs, labels)

# import graphviz
# from sklearn.tree import export_graphviz
# from sklearn import tree
# from sklearn.preprocessing import LabelEncoder
# dot_data = tree.export_graphviz(clf, out_file=None)
# graph = graphviz.Source(dot_data)
# graph.render("graph")

# test
test = pd.read_csv(test_path)
test = test.fillna(train.median())

encoder = LabelEncoder()
test["Sex"] = encoder.fit_transform(test["Sex"])
test["Embarked"] = encoder.fit_transform(test["Embarked"])

inputs = test.loc[:, ["Age", "Fare", "Sex", "Embarked", "Pclass", "SibSp", "Parch"]]

predicts = clf.predict(inputs)
outputs = pd.DataFrame({"PassengerId":test["PassengerId"], "Survived":predicts})
outputs.to_csv("submission.csv", index=False)