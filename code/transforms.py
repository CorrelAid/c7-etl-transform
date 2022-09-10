import pandas as pd
import numpy as np
from pathlib import Path

def flag_cases_without_consent(survey_data_frame: pd.DataFrame, question_id : str):
    """
    Creates new flag_consent column
    :param survey_data_frame: survey dataframe
    :param question_id: id for consent question
    :return: dataframe with added flag_consent column
    """
    # column will include "Ja" if yes, otherwise will be a nan
    assert set(survey_data_frame[question_id].values) != set(["Ja", np.nan]), f"Are you sure that '{question_id}' is the consent column?"

    survey_data_frame["flag_consent"] = survey_data_frame[question_id].apply(lambda question_id : question_id == "Ja")

    return survey_data_frame

def flag_repeated_users(survey_data_frame: pd.DataFrame, question_id : str):
    """
    Creates new flag_repeated column
    :param survey_data_frame: survey dataframe
    :param question_id: id for user id (token / seed) question
    :return: dataframe with added flag_repeated column
    """

    survey_data_frame["flag_repeated"] = test_data.duplicated(subset=[question_id], keep=False)

    return survey_data_frame

def flag_cases_with_fake_observations(survey_data_frame :  pd.DataFrame, input_file_path: Path):
    """
    Creates new flag_fake column
    :param survey_data_frame: survey dataframe
    :param input_file_path: with csv with manually coded fake/repeated observations, each row in the format <column name>,<value>
    :return: dataframe with added flag_fake column
    """
    # create a dictionary for the apply
    flagged_respondents = pd.read_csv(input_file_path, names = ["field", "val"], index_col=False)
    flagged_field_dictionary = {field : [] for field in flagged_respondents["field"].unique()}
    for _, row in flagged_respondents.iterrows():
        flagged_field_dictionary[row["field"]].append(row["val"])

    survey_data_frame["flag_fake"] = survey_data_frame.apply(lambda row: any([row[field] in suspicious_values for field, suspicious_values in flagged_field_dictionary.items()]), axis=1)
    return survey_data_frame

def flag_speeders(survey_data_frame :  pd.DataFrame):
    """

    :param survey_data_frame:
    :return:
    """
    raise NotImplementedError

def flag_critical_question_below_threshold(survey_data_frame: pd.DataFrame, question_id : str):
    """

    :param survey_data_frame:
    :return:
    """
    raise NotImplementedError

def flag_nonsensical_free_text(survey_data_frame :  pd.DataFrame):
    """

    :param survey_data_frame:
    :return:
    """
    raise NotImplementedError
