

# from google.colab import drive
# drive.mount('/content/drive')

# import numpy as np

# import matplotlib as mpl
# import matplotlib.pyplot as plt

# from sklearn.metrics import roc_curve , auc

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

class mode:
  def just(__self__,l):
    trainn = pd.read_csv("./phishing.csv")
    missing  = pd.concat([trainn.isnull().sum()],axis = 1 , keys=['Train'])
    alldata = trainn.drop(["class","Index"],axis =1)
    trainn.head
    for col in trainn.dtypes[trainn.dtypes == "object"].index:
      for_dummy = trainn.pop(col)
      trainn = pd.concat([trainn, pd.get_dummies(for_dummy,prefix=col)],axis=1)
    labels = trainn.pop("class")
    x_train,x_test,y_train,y_test = train_test_split(alldata, labels,test_size = 0.2, random_state = 42)
    rf = RandomForestClassifier()
    rf.fit(x_train,y_train)
    outputt= rf.predict(l)

    return outputt




# y_pred = ob.rf.predict(x_test)


    # 11054 rows and 32 columns
    # print(trainn.shape)
     # print(trainn.head())
         # trainn.columns
    # alldata.columns
       # trainn.head()

          # labels.head
    # labels.shape
    # x_train,x_test,y_train,y_test = train_test_split(trainn, labels,test_size = 0.30)
    # print(x_test.shape)
    # rf = RandomForestClassifier()
    # rf.fit(x_train,y_train)
    # example =np.array([l]) 
    # outputt= rf.predict(example)
    # print(outputt)

        # print(x_test.shape)
         # example =np.array([l]) 
          # print(outputt)
          #y_pred = rf.predict(x_test)