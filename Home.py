import streamlit as st
import pandas as pd
import time

# Configure the Streamlit page
st.set_page_config(
    page_title="Home Page",
    page_icon="❤️",
    layout="wide"
)

# Display various text elements
st.text("Greetings")
st.title("Raghul M Welcome")
st.header("This is Header")
st.subheader("This is subheader")
st.write("Hello world")
st.markdown("""This is *markdown* """)
st.json({"data": "This is streamlit"})
st.code("""
print("Hello Raghul")
a = 10
""", language="python", line_numbers=True)

# Display status messages
st.success("This is success")
st.error("This is error")
st.warning("Warning")
st.exception("TypeError")

# Input widgets
f_name = st.text_input("First Name")
password = st.text_input("Password", type="password")
message = st.text_area("Message")
date = st.date_input("Date")
appointment_time = st.time_input("Appointment Time")
age = st.number_input("Age", min_value=0, max_value=120)
gender = st.radio("Gender", ["Male", "Female"])
enable = st.toggle("Enable Picker")
level = st.checkbox("Level")

# Sliders & Selectors
countries = st.selectbox("Countries", ["Ghana", "UK", "India", "Germany"])
programming_language = st.multiselect("Programming Language", ["PYTHON", "GO", "C", "C++", "RUBY"])
rating = st.slider("Rating", 1, 5)
ranking = st.select_slider("Ranking", ["Intern", "Jr", "Senior", "TL", "Manager", "Director"])

st.divider()

if enable:
    st.write(f"Details: {f_name}, {password}")
    color = st.color_picker("Pick a color")
    st.write(color)

# Data handling and display
def load_data(data: str) -> pd.DataFrame:
    """Loads data from a CSV file and returns a DataFrame."""
    return pd.read_csv(data)

df = load_data("olympics2024.csv")
st.dataframe(df)
st.table(df.head(5))

edited_df = st.data_editor(df)  # Editable data

# Media elements
st.image("Proj.png", caption="Poster Careerpod")

if st.button("Take a Picture"):
    pic = st.camera_input("Take a photo")

# File upload and download
file_upload = st.file_uploader("Upload CSV", type="csv")
if file_upload:
    st.write(pd.read_csv(file_upload))

st.download_button("Download Data", "olympics2024.csv")

# Status elements
if st.button("Compute"):
    with st.spinner("Thinking..."):
        time.sleep(2)
        st.write("Vanakkam")
        st.toast("This is a warning ❤️")

if st.button("Progress"):
    with st.progress(10):
        time.sleep(2)
        st.write("Vanakkam")

# Chat elements
prompt = st.chat_input("Ask Something")
if prompt:
    with st.chat_message("human"):
        st.write(f"You typed: {prompt}")

# Layouts: Tabs
home_tab, about_tab = st.tabs(["Home", "About"])

with home_tab:
    st.subheader("This is the homepage")

with about_tab:
    st.subheader("This is the about page")
    st.dataframe(df)

# Layouts: Columns
col1, col2, col3 = st.columns(3)

with col1:
    st.title("Columns")

col2.dataframe(df)
col1.image("Proj.png", use_column_width=True)

# Containers
container = st.container()
container.write("Some content in a container")

row1 = st.columns(3)
row2 = st.columns(3)

for col in row1 + row2:
    tile = col.container()
    tile.title(":balloon:")

# Expanders and popovers
with st.expander("Expander"):
    st.dataframe(df)

with st.popover("Popover"):
    st.image("Proj.png")

# Plots
st.area_chart(df, x="Country", y="Total")
st.line_chart(df, x="Country", y="Total")
st.bar_chart(df, x="Country", y="Total")

# Form submission
with st.form("My Form"):
    f_name = st.text_input("First Name")
    password = st.text_input("Password", type="password")
    message = st.text_area("Message")
    date = st.date_input("Date")
    submit = st.form_submit_button("Submit")

# Links
st.link_button("LinkedIn", url="https://github.com/Raghul-M/")
