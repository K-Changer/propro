import streamlit as st
import pandas as pd  # st�� �Է°� ��¸� ����� �� ���� ������ ������ ���̽� �ڵ�� �����˴ϴ�.

data = pd.DataFrame
(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)
# �Է�
st.title('1. �Է¹�ư��')
button_result = st.button('Hit me')
print(button_result)

# ��ư�� ������ �������������� �����ϵ��� ������ ������ּ���
st.write(button_result)
st.data_editor(data)
st.checkbox('Check me out')
st.radio('Pick one:', ['nose','ear'])
st.selectbox('Select', [1,2,3])
st.multiselect('Multiselect', [1,2,3])
st.slider('Slide me', min_value=0, max_value=10)
st.select_slider('Slide to select', options=[1,'2'])
st.text_input('Enter some text')
st.number_input('Enter a number')
st.text_area('Area for textual entry')
st.date_input('Date input')
st.time_input('Time entry')
st.file_uploader('File uploader')
st.download_button(
    label="Download data as CSV",
    data='�ȳ��ϼ���',
    file_name='app_df.csv',
    mime='text/csv')
st.camera_input("���߲,ʵ�!")
st.color_picker('Pick a color')

# ���
st.title('2. ��¸޼����')
st.text('Fixed width text')
st.markdown('_Markdown_') # see #*
st.caption('Balloons. Hundreds of them...')
st.latex(r''' e^{i\pi} + 1 = 0 ''')
st.write('Most objects') # df, err, func, keras!
st.write(['st', 'is <', 3]) # see *
st.title('My title')
st.header('My header')
st.subheader('My sub')
st.code('for i in range(8): foo()')

# * optional kwarg unsafe_allow_html = True

# ���
