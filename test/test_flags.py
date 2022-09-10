from code.flags import flag_cases_without_consent, flag_repeated_users
from pathlib import Path

import pandas as pd
import pytest


@pytest.fixture(
    params=[
        [
            Path(__file__).parents[0].joinpath("test_data/flag_test1.csv"),
            Path(__file__).parents[0].joinpath("test_data/flag_test1.yaml"),
        ],
        [
            Path(__file__).parents[0].joinpath("test_data/flag_test2.csv"),
            Path(__file__).parents[0].joinpath("test_data/flag_test2.yaml"),
        ],
        [
            Path(__file__).parents[0].joinpath("test_data/flag_test3.csv"),
            Path(__file__).parents[0].joinpath("test_data/flag_test3.yaml"),
        ],
    ]
)
def flag_test_cases(request):
    dataframe = pd.read_csv(request.param[0])
    yield dataframe, request.param[1]


def test_flag_cases_without_consent(flag_test_cases):
    flag_dataframe, yaml_filename = flag_test_cases
    assert all(
        flag_cases_without_consent(flag_dataframe)["flag_consent"]
        == flag_dataframe["no_consent"]
    )


def test_flag_repeated_users(flag_test_cases):
    flag_dataframe, yaml_filename = flag_test_cases
    assert all(
        flag_repeated_users(flag_dataframe)["flag_repeated"]
        == flag_dataframe["repeated_user"]
    )


def test_flag_cases_with_fake_observations(flag_test_cases):
    flag_dataframe, yaml_filename = flag_test_cases
    assert all(
        flag_repeated_users(flag_dataframe, yaml_filename)["flag_fake"]
        == flag_dataframe["fake_user"]
    )


def test_flag_speeders(flag_test_cases):
    """TODO: Need to check all columns created by this test, and add timing data to test data frames"""  # noqa : E501
    raise NotImplementedError


def test_flag_critical_question_below_threshold(flag_test_cases):
    raise NotImplementedError


def test_flag_nonsensical_free_text(flag_test_cases):
    raise NotImplementedError
