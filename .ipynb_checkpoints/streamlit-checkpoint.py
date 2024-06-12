import streamlit as st
import pandas as pd
import plotly.express as px 
import os
import datetime

st.title("My Dashboard")

def load_file(path):
    if file is not None:
        st.write("Selected file Name: " + file.name)

        ext = str(path.name).split(".")[-1]
        if(ext == 'csv'):
            df=pd.read_csv(path,encoding="ISO-8859-1")
        elif ext == 'xlsx':
            df=pd.read_excel(path)
    else:
        df = pd.read_csv(r"ipl_data.csv",encoding="ISO-8859-1")
        return df
file = st.file_uploader("Uploader file",type=({"csv","xlsx"}))

df = load_file(file)

with st.expander("open uploaded file"):
    st.write(df)



df.sort_values(['first_ings_score','first_ings_wkts','second_ings_score','second_ings_wkts','margin','highscore'],
                axis=0,ascending=[False,False,False,False,False,False],inplace=True)
print(df.head(10))



### Graph  b/w team1 or team2 for toss winner
fig=px.bar(df.head(20),x='team1',y='team2',color='toss_winner',title="Graph  b/w team1 or team2 for toss winner",width=1000)
st.plotly_chart(fig)



### Graph  b/w team1 or team2 for venue and date
fig=px.bar(df.head(20),x='team1',y='team2',color='venue',title="Graph  b/w team1 or team2 for venue and date",hover_data=['date'],width=1000)
st.plotly_chart(fig)


### Graph  b/w first_ings_score and second_ings_score on the basis of winner
fig=px.bar(df,x='first_ings_score',y='second_ings_score',color='match_winner',title="Graph  b/w first_ings_score and second_ings_score on the basis of winner",width=1000)
st.plotly_chart(fig)



### Graph  b/w date and match_winner 
fig=px.bar(df.head(20),x='date',y='match_winner',color='won_by',title="Graph  b/w date and match_winner ",width=1000)
st.plotly_chart(fig)



### Graph  b/w team1 and team2 for (match_winner,highscore,best_bowling,player_of_the_match )
fig=px.scatter(df.head(20),x='team1',y='team2',color='match_winner',size='highscore',title="Graph  b/w team1 and team2 for (match_winner,highscore,best_bowling,player_of_the_match )",
               hover_data=['best_bowling','player_of_the_match'],width=1000)
st.plotly_chart(fig)



### Graph b/w margin and match_winner
fig=px.pie(df.head(20),names='match_winner',title="Graph b/w margin and match_winner",values='margin')
st.plotly_chart(fig)