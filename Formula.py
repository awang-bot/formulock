import streamlit as st

st.set_page_config(
    page_title = "Password Formula",
    page_icon="🔐",
)

# options for the drop down menus
options = ["Choose an Option", "Website",
           "Username", "Generated String", "Numeric Code"]

# initialize the elements list
elements = [None] * 4

# function to update the elements list


def update_elements(idx, value):
    elements[idx] = value

# function to check if a value is in the elements list


def value_in_elements(value):
    return value in elements


st.markdown(
    """
        # Password Formula
    """
)

# First Element
st.markdown(
    """
    ### First Element
    """
)
first_element = st.selectbox("Choose an Option", options, index=0, key="first-choose")
update_elements(0, first_element)

if first_element in ["Website", "Username"]:
    first_capitalization = st.checkbox("Capitalized", key="first-checkbox")
else:
    first_capitalization = None

if first_element != "Numeric Code":
    first_length = st.slider("Length", min_value=3,
                             max_value=20, value=3, key="first-slider")
else:
    first_length = None

if first_element == "Numeric Code":
    first_code = st.text_input("Enter Numeric Code")
else:
    first_code = None

# Second Element
st.markdown(
    """
    ### Second Element
    """
)
second_element = st.selectbox("Choose an Option", options, index=0, key="second-choose")
update_elements(1, second_element)

if second_element in ["Website", "Username"]:
    second_capitalization = st.checkbox("Capitalized", key="second-checkbox")
else:
    second_capitalization = None

if second_element != "Numeric Code":
    second_length = st.slider("Length", min_value=3,
                              max_value=20, value=3, key="second-slider")
else:
    second_length = None

if second_element == "Numeric Code":
    second_code = st.text_input("Enter Numeric Code")
else:
    second_code = None

# Third Element
st.markdown(
    """
    ### Third Element
    """
)
third_element = st.selectbox("Choose an Option", options, index=0, key="third-choose")
update_elements(2, third_element)

if third_element in ["Website", "Username"]:
    third_capitalization = st.checkbox("Capitalized", key="third-checkbox")
else:
    third_capitalization = None

if third_element != "Numeric Code":
    third_length = st.slider("Length", min_value=3,
                             max_value=20, value=3, key="third-slider")
else:
    third_length = None

if third_element == "Numeric Code":
    third_code = st.text_input("Enter Numeric Code")
else:
    third_code = None

# Fourth Element
st.markdown(
    """
    ### Fourth Element
    """
)
fourth_element = st.selectbox("Choose an Option", options, index=0, key="fourth-choose")
update_elements(2, fourth_element)

if fourth_element in ["Website", "Username"]:
    fourth_capitalization = st.checkbox("Capitalized", key="fourth-checkbox")
else:
    fourth_capitalization = None

if fourth_element != "Numeric Code":
    fourth_length = st.slider("Length", min_value=3,
                             max_value=20, value=3, key="fourth-slider")
else:
    fourth_length = None

if fourth_element == "Numeric Code":
    fourth_code = st.text_input("Enter Numeric Code")
else:
    fourth_code = None

