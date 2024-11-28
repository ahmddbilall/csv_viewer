import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="CSV Data Analyzer", page_icon="📊")

st.title("CSV Data Analyzer")
st.write("Upload a CSV file to explore and analyze the data.")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file:
    data = pd.read_csv(uploaded_file)

    st.subheader("Dataset Overview")
    st.write("**Shape:**", data.shape)
    st.write("**Columns:**", list(data.columns))
    st.write("**First 5 Rows:**")
    st.write(data.head())

    st.subheader("Summary Statistics")
    st.write(data.describe())

    st.subheader("Null Value Analysis")
    null_data = data.isnull().sum().reset_index()
    null_data.columns = ["Column", "Missing Values"]
    null_data["Percentage"] = (null_data["Missing Values"] / len(data)) * 100
    st.write(null_data)

    st.subheader("Visualizations")

    num_cols = data.select_dtypes(include=["float64", "int64"]).columns
    if not num_cols.empty:
        st.write("**Histogram for Numerical Columns**")
        col_to_plot = st.selectbox("Select a column", num_cols)
        plt.figure(figsize=(8, 5))
        sns.histplot(data[col_to_plot], kde=True, bins=30)
        st.pyplot(plt)
    else:
        st.write("No numerical columns available for histogram.")

    cat_cols = data.select_dtypes(include=["object", "category"]).columns
    if not cat_cols.empty:
        st.write("**Pie Chart for Categorical Columns**")
        col_to_plot = st.selectbox("Select a categorical column", cat_cols)
        plt.figure(figsize=(8, 5))
        data[col_to_plot].value_counts().plot.pie(autopct="%1.1f%%", startangle=90, cmap="Set3")
        st.pyplot(plt)
    else:
        st.write("No categorical columns available for pie chart.")

    st.subheader("Custom Query")
    query = st.text_input("Enter a query (e.g., Age > 30 & Gender == 'Male')")
    if query:
        try:
            filtered_data = data.query(query)
            st.write("Filtered Data:")
            st.write(filtered_data)
        except Exception as e:
            st.error(f"Error in query: {e}")
