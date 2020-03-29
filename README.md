# titanic

``max_depth=3``の決定木を用いてタイタニック号の乗客が生存したかどうかの予測を行います。

![aaaaa](https://user-images.githubusercontent.com/45190789/77848231-5a5e9000-71fe-11ea-94d5-c037f9f48fc5.png)


# datasets

https://www.kaggle.com/c/titanic よりダウンロード

## shape

```
trainset.shape:  (891, 12)
testset.shape:  (418, 11)
```

## trainset.info()

```
RangeIndex: 891 entries, 0 to 890
Data columns (total 12 columns):
PassengerId    891 non-null int64
Survived       891 non-null int64
Pclass         891 non-null int64
Name           891 non-null object
Sex            891 non-null object
Age            714 non-null float64
SibSp          891 non-null int64
Parch          891 non-null int64
Ticket         891 non-null object
Fare           891 non-null float64
Cabin          204 non-null object
Embarked       889 non-null object
dtypes: float64(2), int64(5), object(5)
```

# train

``"Age", "Fare", "Sex", "Embarked", "Pclass", "SibSp", "Parch"`` を説明変数とする決定木を作成した。``"Sex", "Embarked"``は``LabelEncoder``を用いて文字列を数字
