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

def handle_checkbox_click(row_index):
    selected_rows[row_index] = not selected_rows[row_index]

# Display the DataFrame with checkboxes
st.write("Data:")
for i, row in df.iterrows():
    is_selected = selected_rows[i]
    row_label = f"{row['Column 1']} {row['Column 2']}"
    checkbox = st.checkbox(row_label, is_selected, key=f"checkbox_{i}")
    if checkbox:
        handle_checkbox_click(i)

# Add a delete button
if st.button("Delete Selected Rows"):
    df = df[~df.index.isin([i for i, row in df.iterrows() if selected_rows[i]])]
    selected_rows = [False] * len(df)
    st.write("Data:")
    for i, row in df.iterrows():
        is_selected = selected_rows[i]
        row_label = f"{row['Column 1']} {row['Column 2']}"
        checkbox = st.checkbox(row_label, is_selected, key=f"checkbox_{i}")
        if checkbox:
            handle_checkbox_click(i)
