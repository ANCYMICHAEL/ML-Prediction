import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np

df=pd.read_csv('demopre.csv')[20:].sample(frac=4,replace=True)
# df2=pd.read_csv('pre1.csv')[20:]
# df=pd.concat([df,df2])
# df.fillna(0, inplace=True)
# df = df.reset_index()

# Binary

df1=df[['SMA','SMA_b','WMA_b','STCK_b','MOM_b','LWR_b','ADO_b','CCI_b','TREND']]

X=df1.drop(['TREND'],axis=1).values

print(np.any(np.isnan(X)))


# std_scaler = StandardScaler()
 
# df_scaled = std_scaler.fit_transform(X.to_numpy())
# df_scaled = pd.DataFrame(df_scaled, columns=['SMA_b','WMA_b','STCK_b','MOM_b','LWR_b','CCI_b'])
# X=df_scaled.values

y=df1['TREND'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)



from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,classification_report
import pickle

clf = RandomForestClassifier(max_depth=100, random_state=0)

clf.fit(X_train, y_train)

pickle.dump(clf,open('clf.pkl','wb'))

pred=clf.predict(X_test)

as1= accuracy_score(pred,y_test)

print(as1)

cr=classification_report(pred,y_test)
print()
print('===========Classification Report============')
print(cr)
print('====================================')
print()

from sklearn.svm import SVC

clf=SVC(gamma='auto')

clf.fit(X_train, y_train)

pred=clf.predict(X_test)

as1= accuracy_score(pred,y_test)

print(as1)

cr=classification_report(pred,y_test)
print()
print('===========Classification Report============')
print(cr)
print('====================================')
print()

from sklearn.ensemble import GradientBoostingClassifier

clf=GradientBoostingClassifier(n_estimators=100, learning_rate=1.0,max_depth=1, random_state=0)

clf.fit(X_train, y_train)

pred=clf.predict(X_test)

as1= accuracy_score(pred,y_test)

print(as1)

cr=classification_report(pred,y_test)
print()
print('===========Classification Report============')
print(cr)
print('====================================')
print()

from sklearn.neural_network import MLPClassifier

clf=MLPClassifier(random_state=1, max_iter=300)

clf.fit(X_train, y_train)

pred=clf.predict(X_test)

as1= accuracy_score(pred,y_test)

print(as1)

cr=classification_report(pred,y_test)
print()
print('===========Classification Report============')
print(cr)
print('====================================')
print()

from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM

#LSTM neural network

lstm_model = Sequential()
lstm_model.add(LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1],1)))
lstm_model.add(LSTM(units=50))
lstm_model.add(Dense(1,activation='sigmoid'))
lstm_model.compile(loss='binary_crossentropy', optimizer='adam')
lstm_model.fit(np.reshape(X_train,(X_train.shape[0],X_train.shape[1],1)), y_train, epochs=3, batch_size=128, verbose=2)

sc=lstm_model.evaluate(np.reshape(X_test,(X_test.shape[0],X_test.shape[1],1)),y_test)

print(sc)