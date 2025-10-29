import streamlit as st
st.title('시윤의 첫 번째 앱!')
st.subheader('짱신기하다')
st.write('고구마튀김맛있었겠다...')
st.write('http://naver.com')
st.link_button("네이버 바로가기", 'http://naver.com')

name = st.text_input('이름을 입력해주세요: ')
if st.button('환영인사'):
    st.write(name+'님 안녕하세요!!')
    st.balloons()
    st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQnW2mhPxMZdtNYy3mx8nAa5OrCNbtMDUfUKw&s')

st.success('성공!')
st.warning('경고!')
st.error('오류!')
st.info('안내문')
