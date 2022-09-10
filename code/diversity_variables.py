import pandas as pd
import yaml
from pathlib import Path
from typing import List, Union

def dv_set_leaf(survey_data_frame: pd.DataFrame,
                    cols: List[str],
                    values: List[Union[str,bool]],
                    operator: str,
                    target: str):
    """
    Append column to dataframe based on specified logic

    :param: survey_data_frame: survey dataframe
    :param: cols: list of colums that define the target variable
    :param: values: values that cols are expected to equal
    :param: operator: if all values on cols have to equal or any
    :param: target: column name of newly created column in survey_data_frame
    """
    if operator=="AND":
        is_true = survey_data_frame.loc[:,cols].apply(lambda x: x == values, axis=1).all(axis=1)
    else:
        is_true = survey_data_frame.loc[:,cols].apply(lambda x: x == values, axis=1).any(axis=1)
    survey_data_frame[target] = is_true


def dv_set(survey_data_frame: pd.DataFrame, conf_path: Path) -> pd.DataFrame:
    """
    Set diversity variables in survey_data_frame given yaml config

    :param: survey_data_frame: survey dataframe
    :param: conf_path: path to yaml file
    :return:
    """
    if not conf_path.exists():
        raise 
    with conf_path.open('r') as f:
        conf = yaml.safe_load(f)

    while "LEVEL" in conf.keys():
        for key, item in conf.items():
            if key=="LEVEL":
                continue
            cols = item["COL"]
            values = [True] * len(cols) if "VAL" not in item.keys() else item["VAL"]
            operator = "OR" if "RELATION" not in item.keys() else item["RELATION"]
            dv_set_leaf(survey_data_frame,cols,values,operator,key)
        conf = conf["LEVEL"]    

    return survey_data_frame    