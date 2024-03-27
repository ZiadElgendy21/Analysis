import plotly.express as px
import pandas as pd
import numpy as np

df=pd.read_csv("./sources/fifa_cleaned - fifa_cleaned.csv")

def best_10_players(col):
    df_top10=df.sort_values(by=col,ascending=False).head(10)
    fig=px.bar(df_top10,x='name',y=col,color=col,color_continuous_scale='purp',
           hover_data=['club','nationality','position','preferred_foot'],text_auto=True)
    fig.update_layout(title={'text':f'Best 10 {col}','x':.5,'y':.95},xaxis={'title':'Name'})
    return fig