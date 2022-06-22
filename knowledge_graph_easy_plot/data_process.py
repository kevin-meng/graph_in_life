import pandas as pd
from streamlit_agraph import Config, Edge, Node, agraph
from utils import (set_node_value, load_pickle)


# def extract_graph_data(filename="./data/marvel.xlsx"):
#     df_nodes = pd.read_excel(filename,sheet_name='nodes')
#     df_links = pd.read_excel(filename,sheet_name='links')

#     nodes = df_nodes.T.to_dict()
#     links = df_links.T.to_dict()

#     graph_nodes = []
#     for n in nodes.values():
#         graph_nodes.append(Node(**set_node_value(n)))
        
#     graph_links = []
#     for n in links.values():
#         graph_links.append(Edge(**n))
        
#     return graph_nodes,graph_links


def extract_graph_data(filename="./data/marvel.xlsx",node_default=dict(),link_default=dict()):
    df_nodes = pd.read_excel(filename,sheet_name='nodes')
    df_links = pd.read_excel(filename,sheet_name='links')

    nodes = df_nodes.T.to_dict()
    links = df_links.T.to_dict()

    return nodes, links
