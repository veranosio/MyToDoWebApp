
import streamlit as st

import functions
todos = functions.plik_load()

def AddNewTodo():
    if st.session_state["NewTodo"]:
        new_todo = st.session_state["NewTodo"]+"\n"
        todos.append(new_todo)
        print(todos)
        functions.plik_write(todos)

#def RemovedFromApp():


st.title("To Do app")
#colSub = st.subheader("This is your agenda.")


#todos = unique(todos)#todos = set(todos) #other solution todos = unique(todos)
#todos2 = todos
#col2,coll = st.columns(2)
YourAgenda, CompletedTitle = st.columns(2)

with YourAgenda:
    st.write("This is your agenda.")
    for items in todos:
        st.checkbox(items, key=items)
with CompletedTitle:
    st.write("completed")
    for items in todos:
        if st.session_state[items]:
            st.write("Done")
            if st.session_state["Removetodo"]:
                kkk = todos.index(items)
                todos.pop(kkk)
                functions.plik_write(todos)
                st.rerun()
        else:
            st.write("Not done")






st.text_input(label="", placeholder="Enter a task...", on_change=AddNewTodo, key="NewTodo")
st.button(label="Remove Task",key="Removetodo",help="If you mark more than one Todo"
                                                    " only one will be removed",disabled=False )

# if st.session_state["Removetodo"]:
#
#     if check <= 1:
#         kkk = todos.index(items)
#         todos.pop(kkk)
#         functions.plik_write(todos)
#         st.rerun()
#     else:
#         pass

    # st.session_state[items]
    # if st.session_state[items]:
    #     kkk = todos.index(items)
    #     todos.pop(kkk)
    #     functions.plik_write(todos)
    #     del st.session_state[items]
    #     st.rerun()


# for index, items in enumerate(todos):
#     checkbox = st.checkbox(items,key=items)
#     #st.session_state[items]
#     if checkbox:
#         todos.pop(index)
#         functions.plik_write(todos)
#         st.rerun()





# st.session_state
# print(st.session_state["Removetodo"])