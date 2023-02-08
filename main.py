import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridUpdateMode
from st_aggrid.grid_options_builder import GridOptionsBuilder

tab1, tab2, tab3 = st.tabs(["Time Entry", "Reports", "Team"])


def insert_resource(name, rate):
    with open("timesheet.txt", "a") as f:
            f.write(f"{name}    {rate}\n")
    return name + " | " + str(rate)


def delete_resource(name):
    cnx = snowflake.connector.connect(**st.secrets["snowflake"])
    with cnx.cursor() as my_cur:
        sql_cmd = "DELETE FROM TIMESHEET_DB.PUBLIC.RESOURCES WHERE NAME = '" + name + "'"
        my_cur.execute(sql_cmd)
    cnx.close()
    return "Resources deleted."


def get_all_resources():
    header = ["Name", "Rate"]
    my_data = pd.read_csv("timesheet.txt", sep="\t", header=None, names=header)
    st.write(my_data)
    return my_data


with tab1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
    st.header("Team")
    name = st.text_input("Name", value="", key="Name")
    rate = st.number_input("Rate", value=0.00, key="Rate")

    resource_list = get_all_resources()
    #st.dataframe(resource_list.style.format({"Rate": "{:.2f}"}), use_container_width=True)
    
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
            msg = insert_resource(name, rate)
            st.success(msg, icon="✅")
            
    if 'delete_button' not in st.session_state:
        st.session_state.disabled_save = True
        
    delete_button = st.button("Delete member", key='delete_button', disabled=st.session_state.disabled_delete)
    
    if delete_button:
        for row in selected_row:
            msg = delete_resource(row["Name"])
        st.success(msg, icon="✅")




import streamlit as st

def main():
    st.title("Time Sheet Application")

    start_time = st.time_input("Start Time")
    end_time = st.time_input("End Time")
    task = st.text_input("Task Description")

    if st.button("Submit"):
        with open("timesheet.txt", "a") as f:
            f.write(f"{start_time} - {end_time}: {task}\n")
        st.success("Time sheet submitted!")
        
        with open("timesheet.txt", "r") as f:
            content = f.read()
        st.write(content)

if __name__ == '__main__':
    main()
