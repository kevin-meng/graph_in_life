import pickle
import pandas as pd


def load_pickle(dir):
    with open(dir,'rb') as f:
        out_file = pickle.load(f)
    return out_file


def set_node_value(d):
    """
    set the missing value use default
    """
    node_default = {"id":'',
                "size":250,
                "color":'#ACDBC9',
                "renderLabel":True,
                "labelPosition":'right',
                "svg":'',
                "symbolType":'circle',
                "strokeColor":''}
    
    for k,v in d.items():
        if pd.notnull(v):
            # print(v)
            d[k] = v
        else:
            d[k] = node_default.get(k,"")
    return d



def set_node_value(d):
    """
    set the missing value use default
    """
    node_default = {"color":'#F7A7A6',
                    "type":'STRAIGHT',
                    "semanticStrokeWidth":False,
                    "strokeWidth":1.5,
                    "labelProperty":'',
                    "renderLabel":False,
                    "labelPosition":'right',
                    "linkValue":1,}
    
    for k,v in d.items():
        if pd.notnull(v):
            # print(v)
            d[k] = v
        else:
            d[k] = node_default.get(k,"")
    return d

