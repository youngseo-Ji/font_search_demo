import pandas as pd
#import seaborn as sns
from basic_recomm.models import Font_keyword_value

def make_db_font():
    df = pd.read_excel("C:/Study/font_mid_study/fmproject/basic_recomm/font_vad.xlsx", sheet_name="Sheet4", engine='openpyxl')

    font_list = df['Unnamed: 0'].values.tolist()
    df.drop(['Unnamed: 0'], axis=1, inplace=True)

    for i in range(0, 25):
        fk = Font_keyword_value()
        fk.font_name = font_list[i]

        fk_val = df.iloc[i].tolist()
        fk.key_value = fk_val

        fk.save()
