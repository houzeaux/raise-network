import streamlit as st

import pandas as pd
from altair_styles import hide_menu_style, reduce_header_height_style, remove_altair_action_menu, unblur_header

st.set_page_config(page_title="Guillaume Matrix", layout="wide")
st.markdown(hide_menu_style, unsafe_allow_html=True)

### LAYOUT
sidebar = st.sidebar
main_panel = st.container()
footer = st.container()

main_panel.markdown(reduce_header_height_style, unsafe_allow_html=True)
main_panel.markdown(unblur_header,unsafe_allow_html=True)
#
# Sidebar
#
st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        width: 450px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        width: 450px;
        margin-left: -450px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
sidebar.image("imgs/raise.png",width=200)
sidebar.write("## T6.2 Establishment of a European RAISE network ")
sidebar.write("")
sidebar.write("The task contributors represent the responsible institutions per participating country. In this task, they establish a European AISee network by implementing country-dependent access and contact nodes. They connect the activities of RAISE to those of their network, national, European and international. That is, FZJ establishes connections, e.g., to GCS, HAICU, and IRT in Germany as well as to PRACE together with BSC at European level. UOI connects as a hub to the Nordic countries with NeiC and COST Action CA18203, and together with RTU to EOSC-NORDIC. CYI acts as hub for the EM, has strong links with SESAME, with the Balkans through NI4OS-Europe, as well as links with the oil and gas industry (the Delphi consortium, see Sec. 4.2.2). It extends its reach to other industries through the SimEA ERA Chair project. RTU acts as a hub for the Baltic Region through SESAME Net. RWTH employs its channels to Gauss Alliance and HPC.NRW. CERN connects to INFN, Siemens, and E4 Computer Engineering. CERFACS establishes connections with academics (ISAE-Supaero, IRT, ONERA) and industrial partners (AIRBUS, CNES, Safran) among other within the interdisciplinary institute ANITI and the Helios multi- laboratory workgroup. FM exploits its industrial partner network. Partners involved in other CoEs or European projects establish corresponding connections, i.e., to EXCELLERAT, POP, EoCoE-II, EPI, DEEP, EMME-CARE, etc. (see. Sec. 1.3.3, Tab. 4). Furthermore, connections to ETP4HPC are established. ")

#sidebar.image("imgs/map.png",width=400)


footer.image("imgs/raise.png",width=200)

data = pd.read_csv("data/interactions.csv").set_index("Interaction description")
data = data.sort_values(by="Region")

columns = list(data.columns)


main_panel.markdown("Task 6.2 aims at developing a European RAISE Network to: raise awareness on technical developments and services implemented in the project; enhance their impact; dynamize the use through Europe of Artificial Intelligence (AI) in an High-Performance Computing (HPC) context. Connecting smaller (≤Tier-2) HPC centers, local academic institutions, industry, and SMEs to RAISE’s developments and expertise will allow to uncover new user communities and to provide corresponding service and education. Hence, the CoE RAISE will act as an enabler for AI-based Exascale technologies. Visualize our activities in creating this European network by selecting a category and then a corresponding item." )        

link = '[Map](./imgs/map.png)'
main_panel.markdown(link, unsafe_allow_html=True)
#if(main_panel.button("Show map")):
#    main_panel.text("Display map")
    
selector_columns, spacer, selector_rows = main_panel.columns([3,1,3])
col = selector_columns.selectbox(
        'Select a category',
        ('Region','Activity','Institution/company')
        )
datafilter = data[col].unique()
rows = ["All items"]+list(datafilter)
row = selector_rows.selectbox(
        'Select an item of the category',
        rows
        )
#
# Text in main screen
#
if col == "Region":
    
    if row == "All items":
        main_panel.markdown("###  All regions" )        
        main_panel.markdown( "  " )        
        for name,content in data.iterrows():
            main_panel.markdown( "#####  " + str(content[1]) + " region, " + str(content[0]) )
            main_panel.markdown( "* Activity:    "+str(content[2]) )
            main_panel.markdown( "* Institution: "+str(content[3]) )
            main_panel.markdown( "* Community:   "+str(content[4]) )
            main_panel.markdown( "* Period:      "+str(content[5]) )
            main_panel.markdown( "* Description: "+ "*" + name + "*" +": " )
    else:
        main_panel.markdown( "###  " + row + " region" )        
        main_panel.markdown( "  " )        
        for name,content in data.loc[data[col]==row,:].iterrows():
            main_panel.markdown( "#####  " + str(content[0]) +':' )
            main_panel.markdown( "* Activity:    "+str(content[2]) )
            main_panel.markdown( "* Institution: "+str(content[3]) )
            main_panel.markdown( "* Community:   "+str(content[4]) )
            main_panel.markdown( "* Period:      "+str(content[5]) )
            main_panel.markdown( "* Description: "+ "*" + name + "*" )
            
if col == "Activity":
    
    if row == "All items":
        main_panel.markdown("###  All regions" )        
        main_panel.markdown( "  " )        
        for name,content in data.iterrows():
            main_panel.markdown( "#####  " + str(content[1]) + " region, " + str(content[0]) )
            main_panel.markdown( "* Activity:    "+str(content[2]) )
            main_panel.markdown( "* Institution: "+str(content[3]) )
            main_panel.markdown( "* Community:   "+str(content[4]) )
            main_panel.markdown( "* Period:      "+str(content[5]) )
            main_panel.markdown( "* Description: "+ "*" + name + "*" +": " )
    else:
        main_panel.markdown( "###  " + row + " region" )        
        main_panel.markdown( "  " )        
        for name,content in data.loc[data[col]==row,:].iterrows():
            main_panel.markdown( "#####  " + str(content[0]) +':' )
            main_panel.markdown( "* Activity:    "+str(content[2]) )
            main_panel.markdown( "* Institution: "+str(content[3]) )
            main_panel.markdown( "* Community:   "+str(content[4]) )
            main_panel.markdown( "* Period:      "+str(content[5]) )
            main_panel.markdown( "* Description: "+ "*" + name + "*" )
else:
    
    if row == "All items":
        main_panel.markdown("###  All institutions and companies" )        
        main_panel.markdown( "  " )        
        for name,content in data.iterrows():
            main_panel.markdown("#####  " + str(content[1]) + " region, " + str(content[0]) )
            main_panel.markdown( "* Activity:    "+str(content[2]) )
            main_panel.markdown( "* Institution: "+str(content[3]) )
            main_panel.markdown( "* Community:   "+str(content[4]) )
            main_panel.markdown( "* Period:      "+str(content[5]) )
            main_panel.markdown( "* Description: "+ "*" + name + "*" )
    else:
        main_panel.markdown( "###  Institution/company: " + row )        
        main_panel.markdown( "  " )        
        for name,content in data.loc[data[col]==row,:].iterrows():
            main_panel.markdown("#####  " + str(content[1]) + " region, " + str(content[0]) )
            main_panel.markdown( "* Community:   "+str(content[4]) )
            main_panel.markdown( "* Period:      "+str(content[5]) )
            main_panel.markdown( "* Description: "+ "*" + name + "*" )
        

