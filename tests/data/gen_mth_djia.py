# coding: utf-8
import pandas as pa
djia = pa.read_csv('./DJIA.csv', index_col='DATE', parse_dates=True)
djia = djia.astype('object').convert_objects(convert_numeric=True)
by = lambda x: lambda y: getattr(y, x)
djia_std_mth = djia.groupby([by('year'), by('month')]).std()
print djia_std_mth.head(30)
