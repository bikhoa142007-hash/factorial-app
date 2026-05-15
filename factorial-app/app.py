import streamlit as st
from factorial import fact
import os

def load_users():
    try:
       if os.path.exists("users.txt"):
           with open("users.txt", "r", encoding="utf-8") as f:
               users = [line.strip() for line in f.readlines() if line.strip()]
           return users
       else:
           st.error("File 'users.txt' không tồn tại")
           return []
    except Exception as e:
        st.error(f"Đã xảy ra lỗi khi đọc file: {e}")
        return []
def login_page():
    st.title("Đăng nhập")
    # Input username
    username = st.text_input("Tên đăng nhập: ")
    if st.button("Đăng nhập"):
        if username:
            users =load_users()
            if username in users:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.rerun()
            else:
                st.session_state.show_greeting = True
                st.session_state.username = username
                st.rerun()
        else:
            st.warning("Vui lòng nhập tên người dùng!")
def factorial_calculator():
    st.title("Factorial Calculator")
    st.write(f"Xin chào, {st.session_state.username}!")
    if st.button("Đăng xuất"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()
    st.divider()
    number = st.number_input("Nhập vào một số:",
                             min_value=0,
                             max_value=900)
    if st.button("Tính giai thừa"):
        result = fact(number)
        st.write(f"Giai thừa của {number} là {result}")
def greeting_page():
    st.title("Xin chào")
    st.write(f"Xin chào {st.session_state.username}!")
    st.write("Bạn không có quyền truy cập vào chức năng tính giai thừa")
    if st.button("Quay lại đăng nhập"):
        st.session_state.show_greeting = False
        st.session_state.username = ""
        st.rerun()

def main():
    if 'logged in' not in st.session_state:
        st.session_state.logged_in = False
    if 'username' not in st.session_state:
        st.session_state.username = ""
    if 'show_greeting' not in st.session_state:
        st.session_state.show_greeting = False
    if st.session_state.logged_in:
        factorial_calculator()
    elif st.session_state.show_greeting:
        greeting_page()
    else:
        login_page()
    if __name__ == "__main__":
        main()