import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

#st.set_page_config(layout='wide',page_title='StartUp Analysis')

df = pd.read_csv("startup_cleaned.csv")
df['date'] = pd.to_datetime(df['date'],errors='coerce')
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year
df.rename(columns={'amount':'amount in crs'},inplace=True)
st.header('App by Jaswanth Palla')
st.subheader('Complete Analysis Of Sartups in India From (2014- 2020)')
st.dataframe(df)



######################################################################################################
############################# OVERALL ANALYSIS #################################################
def load_overall_analysis():
    st.title('Overall Analysis')

    # total invested amount
    total = round(df['amount in crs'].sum())
    # max amount infused in a startup
    max_funding = df.groupby('startup')['amount in crs'].max().sort_values(ascending=False).head(1).values[0]
    # avg ticket size
    avg_funding = df.groupby('startup')['amount in crs'].sum().mean()
    # total funded startups
    num_startups = df['startup'].nunique()

    col1,col2,col3,col4 = st.columns(4)

    with col1:
        st.metric('Total',str(total) + ' Cr')
    with col2:
        st.metric('Max', str(max_funding) + ' Cr')

    with col3:
        st.metric('Avg',str(round(avg_funding)) + ' Cr')

    with col4:
        st.metric('No of Funded Startups',num_startups)

    st.header('MoM graph')
    selected_option = st.selectbox('Select Type',['Total','Count'])
    if selected_option == 'Total':
        temp_df = df.groupby(['year', 'month'])['amount in crs'].sum().reset_index()
    else:
        temp_df = df.groupby(['year', 'month'])['amount in crs'].count().reset_index()

    temp_df['x_axis'] = temp_df['month'].astype('str') + '-' + temp_df['year'].astype('str')

    #### 2015 analysis starts
    tempdf_15  =     temp_df[   (temp_df['year']==2015)  ]
    st.header('2015 Analysis')
    st.dataframe(tempdf_15)

    fig0, ax0 = plt.subplots()
    ax0.plot(tempdf_15['month'],tempdf_15['amount in crs'])
    st.pyplot(fig0)


    #### 2016 analysis starts
    tempdf_16 = temp_df[(temp_df['year'] == 2016)]
    st.header('2016 Analysis')
    st.dataframe(tempdf_16)

    fig1, ax1 = plt.subplots()
    # st.dataframe(temp_df)
    ax1.plot(tempdf_16['month'], tempdf_16['amount in crs'])
    st.pyplot(fig1)

    #### 2017 analysis starts
    tempdf_17 = temp_df[(temp_df['year'] == 2017)]
    st.header('2017 Analysis')
    st.dataframe(tempdf_17)

    fig2, ax2 = plt.subplots()
    ax2.plot(tempdf_17['month'], tempdf_17['amount in crs'])
    st.pyplot(fig2)

    #### 2018 analysis starts
    tempdf_18 = temp_df[(temp_df['year'] == 2018)]
    st.header('2018 Analysis')
    st.dataframe(tempdf_18)

    fig3, ax3 = plt.subplots()
    ax3.plot(tempdf_18['month'], tempdf_18['amount in crs'])
    st.pyplot(fig3)



    #### 2019 analysis starts
    tempdf_19 = temp_df[(temp_df['year'] == 2019)]
    st.header('2019 Analysis')
    st.dataframe(tempdf_19)

    fig4, ax4 = plt.subplots()
    # st.dataframe(temp_df)
    ax4.plot(tempdf_19['month'], tempdf_19['amount in crs'])
    st.pyplot(fig4)

    #### 2020 analysis starts
    tempdf_20 = temp_df[(temp_df['year'] == 2020)]
    st.header('2020 Analysis')
    st.dataframe(tempdf_20)

    fig5, ax5 = plt.subplots()
    # st.dataframe(temp_df)
    ax5.plot(tempdf_20['month'], tempdf_20['amount in crs'])
    st.pyplot(fig5)

    ###########################################   INVESTOR FUNCTION    #########################################
    ##########################################################################################################

###########################################   INVESTOR FUNCTION    #########################################
##########################################################################################################

def load_investor_details(investor):
    st.title(investor)
    # load the recent 5 investments of the investor
    last5_df = df[df['investors'].str.contains(investor)].head()[['date', 'startup', 'vertical', 'city', 'round', 'amount in crs']]
    st.subheader('Most Recent Investments')
    st.dataframe(last5_df)

    col1, col2 = st.columns(2)
    with col1:
       # biggest investments
       big_series = df[df['investors'].str.contains(investor)].groupby('startup')['amount in crs'].sum().sort_values(ascending=False).head()
       st.subheader('Biggest Investments')
       #st.dataframe(b)
       fig, ax = plt.subplots()
       ax.bar(big_series.index,big_series.values)

       st.pyplot(fig)

    with col2:
        try:
         vertical_series = df[df['investors'].str.contains(investor)].groupby('vertical')['amount in crs'].sum()
         st.subheader('Sectors invested in')
         #st.dataframe(vertical_series)
         fig1,ax1 = plt.subplots()
         ax1.pie(vertical_series,labels=vertical_series.index,autopct="%0.01f%%")
         st.pyplot(fig1)
        except:
         st.error('the data is not sufficient to plot graph kindly other investor')


        #### using round and city
    col3, col4 = st.columns(2)
    with col3:
      try:
        round_series=df[df['investors'].str.contains(investor)].groupby('round')['amount in crs'].sum()
        st.subheader('Analysis based on round')
        st.dataframe(round_series)
        fig2,ax2 = plt.subplots()
        plt.figure(figsize=(1,2))
        ax2.pie(round_series, labels=round_series.index, autopct="%0.01f%%")
        st.pyplot(fig2)
      except:
          st.error('the data is not sufficient to plot graph kindly other investor')


    with col4:
        try:
         st.subheader('Analysis based on city')
         city_series = df[df['investors'].str.contains(investor)].groupby('city')['amount in crs'].sum()
         st.dataframe(city_series)
         fig3, ax3 = plt.subplots()
         ax3.bar(city_series.index,city_series.values)
         st.pyplot(fig3)
        except:
            st.error('the data is not sufficient to plot graph kindly other investor')

#### """"yearly analysis """""   ################

    df['year'] = df['date'].dt.year
    year_series = df[df['investors'].str.contains(investor)].groupby('year')['amount in crs'].sum()

    st.subheader('Year On  Investment')
    if year_series.count() < 2:
        st.error('Please Kindly Ignore Yearly Analysis as The size Is Not Sufficient To Plot The Graph')

    st.dataframe(year_series)

    fig14,ax14 = plt.subplots()
    ax14.plot(year_series.index,year_series.values)
    st.pyplot(fig14)


######################################################################################################
################################# STARTUP FUNCTION ##################################################


def load_startup_details(startup):
    st.header(startup+'Analysis')
    last5_df = df[df['startup'].str.contains(startup)][['date', 'startup', 'vertical', 'city', 'round', 'amount in crs']]
    st.dataframe(last5_df)

#############################################################################################################

    st.subheader('vertical analysis')
    try:
     vertical_series = df[df['startup'].str.contains(startup)].groupby('vertical')['amount in crs'].sum()
     st.dataframe(vertical_series)
     if vertical_series.count() < 1:
       st.error('data is not sufficient to plot graph please selct another startup')
     else:
      fig1,ax1 = plt.subplots()
      ax1.bar(vertical_series.index, vertical_series.values)
      st.pyplot(fig1)
    except:
        st.error('data is not present to plot ikindly select other startup')


    st.subheader('vertical proportion chart analysis')
    vertical_series = df[df['startup'].str.contains(startup)].groupby('vertical')['amount in crs'].sum()
    try:
      if vertical_series.count() < 1:
        st.error('data is not sufficient to plot graph please selct another startup')
      else:
       fig2,ax2 = plt.subplots()
       ax2.pie(vertical_series,labels=vertical_series.index, autopct="%0.01f%%")
       st.pyplot(fig2)
    except:
       st.error('data is not present to  pie chart plot ikindly select other startup')



######################################################################################################

    st.subheader('sub--vertical analysis')
    subvertical_series = df[df['startup'].str.contains(startup)].groupby('subvertical')['amount in crs'].sum()
    st.dataframe(subvertical_series)
    try:
      if subvertical_series.size <1:
       st.error('Please  kindly ignore the carts as the is not sufficient to plot select anoher one from dropdown')
      else:
       fig3,ax3 = plt.subplots()
       ax3.bar(subvertical_series.index, subvertical_series.values)
       st.pyplot(fig3)
    except:
        st.error('data is not present to plot kindly select other startup')


    st.subheader(' sub--vertical proportion chart analysis')
    subvertical_series = df[df['startup'].str.contains(startup)].groupby('subvertical')['amount in crs'].sum()
    try:
     if subvertical_series.size <1:
         st.error('Please  kindly ignore the carts as the is not sufficient to plot select anoher one from dropdown')
     else:
        fig4,ax4 = plt.subplots()
        ax4.pie(subvertical_series,labels=subvertical_series.index, autopct="%0.01f%%")
        st.pyplot(fig4)
    except:
        st.error('data is not present to plot kindly select other startup')
##########################################################################################################

    st.subheader('round-- analysis')
    round_series = df[df['startup'].str.contains(startup)].groupby('round')['amount in crs'].sum()
    st.dataframe(round_series)
    try:
      if  round_series.count()<1:
        st.error('Please  kindly ignore the carts as the is not sufficient to plot select anoher one from dropdown')
      else:
        fig4, ax4 = plt.subplots()
        ax4.bar(round_series.index,round_series.values)
        st.pyplot(fig4)
    except:
      st.error('data is not present to plot kindly select other startup')


    st.subheader('round--  Proportion analysis')
    round_series = df[df['startup'].str.contains(startup)].groupby('round')['amount in crs'].sum()
    try:
      if round_series.count()<1:
         st.error('Please  kindly ignore the carts as the is not sufficient to plot select anoher one from dropdown')
      else:
        fig5, ax5 = plt.subplots()
        ax5.pie(round_series, labels=round_series.index,autopct="%0.01f%%")
        st.pyplot(fig5)
    except:
        st.error('data is not present to plot kindly select other startup')

##################################################################################

    st.subheader('city-- Analysis')
    city_series = df[df['startup'].str.contains(startup)].groupby('city')['amount in crs'].sum()
    st.dataframe(city_series)
    try:
        if city_series.count()<1:
          st.error('data is not present to plot kindly select other startup')
        else:
          fig6, ax6 = plt.subplots()
          ax6.bar(city_series.index,city_series.values)
          st.pyplot(fig6)
    except:
        st.error('data is not present to plot kindly select other startup')



    st.subheader('city--  Proportion Analysis')
    city_series = df[df['startup'].str.contains(startup)].groupby('city')['amount in crs'].sum()
    try:
        if city_series.count()<1:
          st.error('data is not present to plot kindly select other startup')
        else:
          fig7, ax7 = plt.subplots()
          ax7.pie(city_series,labels=city_series.index,autopct="%0.01f%%")
          st.pyplot(fig7)
    except:
        st.error('data is not present to plot kindly select other startup')


###########################################################################################################
#################################################################################################
  ####### option selcting from  and making if functions to work and sidebar using and dropdown

st.sidebar.title('Startup Funding Analysis')

option = st.sidebar.selectbox('Select One',['Overall Analysis','StartUp','Investor'])

if option == 'Overall Analysis':
    load_overall_analysis()

elif option == 'StartUp':
    st.title('StartUp Analysis')
    slected_startup=st.sidebar.selectbox('Select StartUp',sorted(df['startup'].unique().tolist()))
    btn1 = st.sidebar.button('Find StartUp Details')
    if btn1:
        load_startup_details(slected_startup)

else:
    selected_investor = st.sidebar.selectbox('Select StartUp',sorted(set(df['investors'].str.split(',').sum())))
    btn2 = st.sidebar.button('Find Investor Details')
    if btn2:
        load_investor_details(selected_investor)
