import os,sys
import streamlit as st
import json 
import pandas as pd
from streamlit_agraph import Config, Edge, Node, agraph

sys.path.append("./knowledge_graph_easy_plot")
from data_process import extract_graph_data
from utils import (set_node_value, set_link_value, load_pickle)
from PIL import Image


st.set_page_config(page_title="Knowledge Graph", page_icon="💗")  # , layout="wide"
image = Image.open("./data/logo-new.png")
# image = Image.open("logo-new.png")

st.sidebar.image(image,caption="",use_column_width='always')


with  st.sidebar.expander('Graph Settings',expanded=False): # expand default
    width = st.text_input("width",value=800,help=' the width of the graph')
    height = st.text_input("gravheightity",value=800, help="the height  of the graph")
    # directed =  st.selectbox("directed",options=["False","True"], help="if directed")


with  st.sidebar.expander('Node Settings',expanded=False): # expand default
    node_label_position = st.selectbox("node.labelPosition",options=['left','right','top','bottom','center'])
    node_render_label = st.checkbox("node.renderLabel",value=True)
    node_label_properity = st.text_input("node.labelProperty",value='id')
    node_color = st.text_input("node.color",value='#ACDBC9')
    node_stroke_color = st.text_input("node.strokeColor",value='#ACDBC9')
    node_show_svg = st.checkbox("node.showSvg",value=True,help=' use the svg if svg link exists')
    node_default = {
                    "id":"",
                    "size":250,
                    "color":node_color,
                    "labelProperty":node_label_properity,
                    "renderLabel":node_render_label,
                    "labelPosition":node_label_position,
                    "svg":"",
                    "symbolType":"circle",
                    "showSvg":node_show_svg,
                    "strokeColor":node_stroke_color
                    }
    # print(node_default)

with  st.sidebar.expander('Edge Settings',expanded=False): # expand default
    directed =  st.selectbox("directed",options=["False","True"], help="if directed")
    link_type = st.selectbox("link.type",options=['STRAIGHT','CURVE_SMOOTH','CURVE_FULL'])
    link_render_label = st.checkbox("link.renderLabel",value=True)
    link_color = st.text_input("node.color",value='#F7A7A6')
    link_label_property = st.text_input("link.labelProperty",value='label')
    link_default = {"color":"#F7A7A6",
                    "type":link_type,
                    # "semanticStrokeWidth":False,
                    # "strokeWidth":1.5,
                    "labelProperty":link_label_property,
                    "renderLabel":link_render_label,
                    # "linkValue":1
                    }
    

with  st.sidebar.expander('React-D3-graph Settings'):
    alphaTarget = st.text_input("alphaTarget",value=0.05,
                                              help='he simulation “cools down”. When alpha reaches alphaTarget, the simulation stops;')
    gravity = st.text_input("gravity",value=-200,
                                      help="""
                                      this will define how close nodes are to each other. 
                                      If value is positive, nodes will attract each other. 
                                      If value is negative, nodes will repel each other. Most of the times this is what we want, so nodes don"t overlap.'
                                      """)
    linkLength = st.text_input("linkLength",value=50,
                                 help = 'the length of each link from the center of the nodes it joins.')
    linkStrength = st.text_input("linkStrength",value=0.2,
                                 help='Overlapping nodes are resolved through iterative relaxation. ')
    disableLinkForce = st.selectbox("disableLinkForce",options=["False","True"],
                                                      help="Completely disables d3 force link and simulation to re-trigger so that one can obtain precise render of node positions ")
    st.write('More infomation:[docs](https://danielcaldas.github.io/react-d3-graph/docs/index.html)')



st.sidebar.write("#### Upload your own data")
uploaded_file = st.sidebar.file_uploader("the marvel data default")
if uploaded_file is None:
    # nodes,edges = extract_graph_data(node_default=node_default,link_default=link_default)
    nodes,edges = extract_graph_data()

else:
    # nodes,edges = extract_graph_data(uploaded_file,node_default=node_default,link_default=link_default)
    nodes,edges = extract_graph_data(uploaded_file)

# print(node_default)
# print(link_default)

graph_nodes = []
for n in nodes.values():
    print(set_node_value(n,node_default))
    graph_nodes.append(Node(**set_node_value(n,node_default)))
    
graph_links = []
for n in edges.values():
    print(set_link_value(n,link_default))
    graph_links.append(Edge(**set_link_value(n,link_default)))


downloader =  st.sidebar.expander('Download Sample Data')
with open('./data/marvel.xlsx', 'rb') as f:
# with open('marvel.xlsx', 'rb') as f:
    downloader.download_button('Download', f, file_name='marvel.xlsx')
downloader.write("Source cod: [Github](https://github.com/kevin-meng/graph_in_life)")


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
                # node={'labelProperty':node_label_properity,"renderLabel":node_render_label},
                # link={'labelProperty': link_label_property, 'renderLabel': link_render_label, "type":link_type},
                initialZoom=1,
                d3= d3_config,
                # **kwargs e.g. node_size=1000 or node_color="blue"
                ) 


# return_value = agraph(nodes=nodes, 
#                       edges=edges, 
#                       config=config)

return_value = agraph(nodes=graph_nodes, 
                      edges=graph_links, 
                      config=config)

st.markdown("---")

