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

if __name__ == '__main__':
    main()
