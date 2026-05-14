from numpy.random import f
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io
from PIL import Image

# Hiển thị tiêu đề và tải lên file Excel
st.title("Phân tích dữ liệu điểm số học sinh")
uploaded_file = st.file_uploader("Chọn file Exel (có cột 'Điểm số')", type=["xlsx"])
# Hàm tính điểm trung bình
def calculate_average(scores):
    return sum(scores) / len(scores)
def percentage_distribution(scores):
    bins = {"90-100": 0, "80-89": 0, "70-79": 0, "60-69": 0, "<60": 0}
    for score in scores:
        if score >= 90:
            bins["90-100"] = 1
        elif score >= 80:
            bins["80-89"] = 1
        elif score >= 70:
            bins["70-79"] = 1
        elif score >= 60:
            bins["60-69"] = 1
        else:
            bins["<60"] = 1
    return bins
# Khi  có file được tải lên, hiển thị dữ liệu và biểu đồ
if uploaded_file:
# Đọc dữ liệu từ file Excel
# dropna() để loại bỏ các giá trị thiếu và astype(f) để chuyển đổi dữ liệu thành kiểu float
     df = pd.read_excel(uploaded_file)
     scores = df['Điểm số'].dropna().astype(float).tolist()
     if scores:
         st.write("Tổng số học sinh:", len(scores), "Điểm trung bình:", round(calculate_average(scores), 2))
         # Phân loại điểm
         dist = percentage_distribution(scores)
         labels = list(dist.keys())
         values = list(dist.values())
         fig, ax = plt.subplots(figsize=(3, 3))
         ax.pie(
              values,
              labels=labels,
              autopct="%1.1f%%",
              textprops={"fontsize": 3.5})
         ax.axis("equal")
         plt.tight_layout(pad=0.1)
         buf = io.BytesIO()
         fig.savefig(buf, format="png", dpi=300)
         buf.seek(0)
         st.markdown("Biểu đồ phân phối điểm số:")
         img = Image.open(buf)
         col1, col2, col3 = st.columns([1, 2, 1])
         with col2:
                st.image(img, use_column_width=True)
                st.markdown("Biểu đồ phân phối điểm số:")