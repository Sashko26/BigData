import  numpy  as  np
import  pandas  as  pd
import  matplotlib.pyplot  as  plt
import  folium

dataset_path  =  './Data/Map-Crime_Incidents-Previous_Three_Months.csv'

# считываем исходный набор данных (в формате значений, разделенных запятыми) в DataFrame
SF  =   pd.read_csv (dataset_path)


