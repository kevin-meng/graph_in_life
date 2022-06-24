import pandas as pd


def extract_graph_data(filename="./data/marvel.xlsx",node_default=dict(),link_default=dict()):
    df_nodes = pd.read_excel(filename,sheet_name='nodes')
    df_links = pd.read_excel(filename,sheet_name='links')

    nodes = df_nodes.T.to_dict()
    links = df_links.T.to_dict()

    return nodes, links
