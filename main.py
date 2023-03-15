import streamlit as st
import pandas as pd

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


def save_resources(df):
        df.to_csv("timesheet.txt", index=False, sep="\t")       
        

        
with tab1:
        st.header("A cat")
        st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
        st.header("A dog")
        st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:

        df = get_all_resources()
                                      
        # Display the DataFrame with checkboxes
        edited_df = st.experimental_data_editor(df, num_rows="dynamic")
        
        if save_button:
                save_resources(edited_df)
                st.success('Saved', icon="✅")
