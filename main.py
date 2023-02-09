import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridUpdateMode
from st_aggrid.grid_options_builder import GridOptionsBuilder
import time

tab1, tab2, tab3 = st.tabs(["Time Entry", "Reports", "Team"])

#with open("timesheet.txt", "w") as f:
#    st.write("File deleted")


def get_all_resources():
        try:
                my_data = pd.read_csv("timesheet.txt", sep="\t")
        except:
                my_data = pd.DataFrame(
                        {
                                "Name": ['ABC'],
                                "Rate": [123]
                        }
                )

        return my_data


def insert_resource(name, rate):
        new_row = {'Name': name, 'Rate': rate}
        df = get_all_resources()
        df = df.append(new_row, ignore_index=True)
        df.to_csv("timesheet.txt", index=False, sep="\t")


def delete_resource(name):
        my_data = pd.read_csv("timesheet.txt", sep="\t")
        index_to_delete = my_data[my_data['Name'] == name].index
        my_data.drop(index_to_delete, inplace=True)
        my_data.to_csv("timesheet.txt", index=False, sep="\t")
        return "Resources deleted."
        
        
def refresh_gid():
    df = get_all_resources()
        
    # Create a checkbox for each row in the DataFrame
    selected_rows = [False] * len(df)
    
    # Display the DataFrame with checkboxes
    st.write("Data:")
    for i, row in df.iterrows():
        is_selected = selected_rows[i]
        row_label = f"{row['Name']} {row['Rate']}"
        checkbox = st.checkbox(row_label, is_selected, key=f"checkbox_{i}")
        if checkbox:
                selected_rows[i] = not selected_rows[i]
    
    return df;

        
with tab1:
        st.header("A cat")
        st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
        
        with open("timesheet.txt", "r") as f:
            data = f.read()
            st.write(data)

with tab2:
        st.header("A dog")
        st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
        st.header("Team")
        name = st.text_input("Name", value="")
        rate = st.number_input("Rate", value=0.00)

        save_button = st.button("Save member")

        if save_button:
                if name and rate:
                        insert_resource(name, rate)
                        st.success('Saved', icon="✅")

        grid_table = refresh_gid()

        delete_button = st.button("Delete member")

        if delete_button:
                for row in selected_row:
                        msg = delete_resource(row["Name"])
                st.success(msg, icon="✅")
                    
                df = df[~df.index.isin([i for i, row in df.iterrows() if selected_rows[i]])]
                st.write(df)
