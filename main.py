import pandas as pd
import numpy as np
from sklearn.feature_selection import RFE
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# loading datafile
df = pd.read_csv("data.csv")

# analysis
app_categories = ['mesajlasma', 'oyun', 'sosyal_medya', 'video', 'muzik', 'toplam_kullanim']
print(df.groupby("cinsiyet").mean()[app_categories])
print(df.groupby("mezuniyet").agg({'puan': 'mean', 'toplam_kullanim': 'mean'}))
print(df.groupby("alan").agg({'puan': 'mean', 'puan': 'std'}))
# TODO: generate charts from groupby objects

# filling missing values
# TODO: will be added after real-life data (e.g. df['alan'].interpolate())

# converting categoric variables to numeric values
df['alan'] = df['alan'].replace('SAY', 0).replace('EA', 1).replace('SOZ', 2)
df['mezuniyet'] = df['mezuniyet'].replace('OGRENCI', 0).replace('MEZUN', 1)
df['cinsiyet'] = df['cinsiyet'].replace('KADIN', 0).replace('ERKEK', 1)

# normalizing continious variables
cont_vars = df[['puan', 'mesajlasma', 'oyun', 'sosyal_medya', 'video', 'muzik', 'toplam_kullanim']]
normalized_cont_vars = (cont_vars - cont_vars.min()) / (cont_vars.max() - cont_vars.min())
df[cont_vars.columns] = normalized_cont_vars
del cont_vars, normalized_cont_vars

# feature extraction and selection (ANOVA and RFE)
# TODO: will be added after real-life data
response = df['puan']
features = df[['mesajlasma', 'oyun', 'sosyal_medya', 'video', 'muzik', 'toplam_kullanim',
               'alan', 'mezuniyet', 'cinsiyet']]

# linear regression with 10 fold cross validation
linreg = LinearRegression(fit_intercept=True)
num_folds = 2
model_parameters = np.zeros((num_folds, 12))

for i in range(num_folds):
    # split training set into test and training partitions
    X_train, X_test, y_train, y_test = train_test_split(features, response, test_size=0.10)
    # fit the linear regression model by training set
    linreg.fit(X_train, y_train)
    # make predictions on testing set
    y_test_pred = linreg.predict(X_test)
    # store model parameters and results
    fold_row = np.append(linreg.coef_,
                         [linreg.intercept_, mean_squared_error(y_test, y_test_pred), r2_score(y_test, y_test_pred)])
    model_parameters[i, :] = fold_row
    del X_train, X_test, y_train, y_test, y_test_pred
    del fold_row

# form average model
df_model_parameters = pd.DataFrame(model_parameters)
df_model_parameters.columns = np.append(features.columns.values, ['kesisim', 'MSE', 'R2'])
df_model_parameters.mean()

# TODO: plot







