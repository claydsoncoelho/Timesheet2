import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridUpdateMode
from st_aggrid.grid_options_builder import GridOptionsBuilder

tab1, tab2, tab3 = st.tabs(["Time Entry", "Reports", "Team"])

#with open("timesheet.txt", "w") as f:
#    st.write("File deleted")

        
def insert_resource(df):
        df.to_csv("timesheet.txt", index=False, sep="\t")


def delete_resource(name):
        header = ["Name", "Rate"]
        my_data = pd.read_csv("timesheet.txt", sep="\t", header=None, names=header)
        index_to_delete = my_data[my_data['Name'] == name].index
        my_data.drop(index_to_delete, inplace=True)
        st.write(my_data) 
        my_data.to_csv("timesheet.txt", index=False, sep="\t")
        return "Resources deleted."


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
                
        st.write(my_data)
        return my_data


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
        name = st.text_input("Name", value="", key="Name")
        rate = st.number_input("Rate", value=0.00, key="Rate")

        resource_list = get_all_resources()
    
        gd = GridOptionsBuilder.from_dataframe(resource_list)
        gd.configure_selection(selection_mode='multiple', use_checkbox=True)
        gridoptions = gd.build()

        grid_table = AgGrid(resource_list, gridOptions=gridoptions, update_mode=GridUpdateMode.SELECTION_CHANGED)
    
        selected_row = grid_table["selected_rows"]
    
        if len(selected_row) == 0:
                st.session_state.disabled_delete = True
                st.session_state.disabled_save = False
        elif len(selected_row) == 1:
                st.session_state.disabled_delete = False
                st.session_state.disabled_save = False
        elif len(selected_row) > 1:
                st.session_state.disabled_save = True
                st.session_state.disabled_delete = False
        
        if 'save_button' not in st.session_state:
                st.session_state.disabled_save = False
        
        save_button = st.button("Save member", key='save_button', disabled=st.session_state.disabled_save)
    
        if save_button:
                if name and rate:
                        insert_resource(resource_list, name, rate)
                        st.success('Saved', icon="✅")
            
        if 'delete_button' not in st.session_state:
                st.session_state.disabled_save = True
        
        delete_button = st.button("Delete member", key='delete_button', disabled=st.session_state.disabled_delete)
    
        if delete_button:
                for row in selected_row:
                        msg = delete_resource(row["Name"])
                st.success(msg, icon="✅")
