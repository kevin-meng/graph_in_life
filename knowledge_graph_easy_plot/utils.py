import pickle
import pandas as pd

def load_pickle(dir):
    with open(dir,'rb') as f:
        out_file = pickle.load(f)
    return out_file


def set_node_value(d,node_default=None):
    """
    set the missing value use default.
    """
    # node_default = {"id":'',
    #             "size":250,
    #             "color":'#ACDBC9',
    #             "renderLabel":True,
    #             "labelPosition":'right',
    #             "svg":'',
    #             "symbolType":'circle',
    #             "strokeColor":''}

    d = {k:v for k,v in d.items() if pd.notnull(v)}
    for k,v in node_default.items():
        if pd.isnull(d.get(k)):
            d[k] = node_default.get(k,"")
    if not node_default['showSvg']:
        d['svg'] = ''
    return d



def set_link_value(d,link_default=None):
    """
    set the missing value use default.
    """
    # link_default = {"color":"#F7A7A6",
    #                 "type":"STRAIGHT",
    #                 "semanticStrokeWidth":False,
    #                 "strokeWidth":1.5,
    #                 # "labelProperty":'',
    #                 # "renderLabel":False,
    #                 # "labelPosition":'right',
    #                 "linkValue":1,}
    
    d = {k:v for k,v in d.items() if pd.notnull(v)}
    for k,v in link_default.items():
        if pd.isnull(d.get(k)):
            d[k] = link_default.get(k,"")
    return d


