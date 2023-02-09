import streamlit as st
import pandas as pd

# Create a sample DataFrame
data = {
    'Column 1': [1, 2, 3, 4, 5],
    'Column 2': ['A', 'B', 'C', 'D', 'E']
}
df = pd.DataFrame(data)

# Create a checkbox for each row in the DataFrame
selected_rows = [False] * len(df)

def handle_checkbox_change(change, row_index):
    selected_rows[row_index] = change

# Display the DataFrame with checkboxes
st.write("Data:")
for i, row in df.iterrows():
    st.write(st.checkbox(row, selected_rows[i], key=i, on_change=lambda change, i=i: handle_checkbox_change(change, i)), df)
