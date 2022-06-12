import os,sys
import streamlit as st
import json 
import pandas as pd
from streamlit_agraph import Config, Edge, Node, agraph

sys.path.append("./knowledge_graph_easy_plot")
from data_process import extract_graph_data
from PIL import Image

# print(os.listdir())
st.set_page_config(page_title="Knowledge Graph", page_icon="💗")  # , layout="wide"

image = Image.open("./data/logo-new.png")
# image = Image.open("logo-new.png")

st.sidebar.image(image,caption="",use_column_width='always')

st.sidebar.write("#### Upload your own data")
uploaded_file = st.sidebar.file_uploader("the marvel data default")
if uploaded_file is None:
    nodes,edges = extract_graph_data()
else:
    nodes,edges = extract_graph_data(uploaded_file)

downloader =  st.sidebar.expander('Download Sample Data')
with open('./data/marvel.xlsx', 'rb') as f:
# with open('marvel.xlsx', 'rb') as f:
    downloader.download_button('Download', f, file_name='marvel.xlsx')
downloader.write("Source cod: [Github](https://github.com/kevin-meng/graph_in_life)")


with  st.sidebar.expander('Graph Settings',expanded=True): # expand default
    width = st.text_input("width",value=800,help=' the width of the graph')
    height = st.text_input("gravheightity",value=800, help="the height  of the graph")
    directed =  st.selectbox("directed",options=["False","True"], help="if directed")


with  st.sidebar.expander('React-D3-graph Settings'):
    alphaTarget = st.text_input("alphaTarget",value=0.05,
                                              help='he simulation “cools down”. When alpha reaches alphaTarget, the simulation stops;')
    gravity = st.text_input("gravity",value=-300,
                                      help="""
                                      this will define how close nodes are to each other. 
                                      If value is positive, nodes will attract each other. 
                                      If value is negative, nodes will repel each other. Most of the times this is what we want, so nodes don"t overlap.'
                                      """)
    linkLength = st.text_input("linkLength",value=100,
                                 help = 'the length of each link from the center of the nodes it joins.')
    linkStrength = st.text_input("linkStrength",value=0.1,
                                 help='Overlapping nodes are resolved through iterative relaxation. ')
    disableLinkForce = st.selectbox("disableLinkForce",options=["False","True"],
                                                      help="Completely disables d3 force link and simulation to re-trigger so that one can obtain precise render of node positions ")
    st.write('More infomation:[docs](https://danielcaldas.github.io/react-d3-graph/docs/index.html)')



# config use https://danielcaldas.github.io/react-d3-graph/sandbox/index.html?data=marvel
# https://danielcaldas.github.io/react-d3-graph/docs/2.1.0.html#config-d3
d3_config = {
    "alphaTarget": eval(alphaTarget),
    "gravity": eval(gravity), #  -250,
    "linkLength": eval(linkLength),
    "linkStrength": eval(linkStrength),
    "disableLinkForce": eval(disableLinkForce)
  }


config = Config(width=eval(width), 
                height=eval(height), 
                directed=eval(directed),
                nodeHighlightBehavior=True, 
                highlightColor="#F7A7A6", # or "blue"
                collapsible=True,
                node={'labelProperty':'label',"renderLabel":True},
                link={'labelProperty': 'label', 'renderLabel': False},
                initialZoom=1,
                # d3= d3_config,
                # **kwargs e.g. node_size=1000 or node_color="blue"
                ) 


return_value = agraph(nodes=nodes, 
                      edges=edges, 
                      config=config)

st.markdown("---")

