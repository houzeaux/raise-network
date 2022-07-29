import streamlit as st

import pandas as pd
from altair_styles import hide_menu_style, reduce_header_height_style, remove_altair_action_menu, unblur_header

st.set_page_config(page_title="Guillaume Matrix", layout="wide")
st.markdown(hide_menu_style, unsafe_allow_html=True)

### LAYOUT
#sidebar = st.sidebar
main_panel = st.container()
footer = st.container()

main_panel.markdown(reduce_header_height_style, unsafe_allow_html=True)
main_panel.markdown(unblur_header,unsafe_allow_html=True)

# doing the upper menu
#
#sidebar.image("imgs/logo.png",width=200)
#sidebar.write("## Risk Score Calculator")

data = pd.read_csv("data/coefficients.csv").set_index("Name")

columns = list(data.columns)
rows = ["All rows"]+list(data.index)

selector_columns, spacer, selector_rows = main_panel.columns([3,1,3])
col = selector_columns.selectbox(
        'Select a Column',
        columns
        )
row = selector_rows.selectbox(
        'Select a Row',
        rows
        )

if row == "All rows":
    for name,content in data.iterrows():
        main_panel.markdown( "#### "+ name +": " )
        main_panel.markdown("         " + str(content[col])  )
else:
    main_panel.write( "#### " + str(data.loc[row,col])  )



