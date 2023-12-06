#��Ű��/ �Լ� ���� 
import streamlit as st
import pandas as pd
import FinanceDataReader as fdr
import datetime
import matplotlib.pyplot as plt
import matplotlib 
from io import BytesIO
import plotly.graph_objects as go
import pandas as pd

@st.cache_data
def get_stock_info():
    base_url =  "http://kind.krx.co.kr/corpgeneral/corpList.do"    
    method = "download"
    url = "{0}?method={1}".format(base_url, method)   
    df = pd.read_html(url, header=0)[0]
    df['�����ڵ�']= df['�����ڵ�'].apply(lambda x: f"{x:06d}")     
    df = df[['ȸ���','�����ڵ�']]
    return df

def get_ticker_symbol(company_name):     
    df = get_stock_info()
    code = df[df['ȸ���']==company_name]['�����ڵ�'].values    
    ticker_symbol = code[0]
    return ticker_symbol

# �ڵ� ���� �߰�
ticker_symbol = get_ticker_symbol(stock_name)     
start_p = date_range[0]               
end_p = date_range[1] + datetime.timedelta(days=1) 
df = fdr.DataReader(ticker_symbol, start_p, end_p, exchange="KRX")
df.index = df.index.date
st.subheader(f"[{stock_name}] �ְ� ������")
st.dataframe(df.head())