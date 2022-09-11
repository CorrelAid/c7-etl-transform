from pathlib import Path

import pandas as pd
import pytest
import yaml

from transform_code.flags import (
    flag_cases_with_fake_observations,
    flag_cases_without_consent,
    flag_repeated_users,
    flag_speeders,
)


@pytest.fixture(
    params=[
        [
            # mixed data ids users
            Path(__file__).parents[0].joinpath("test_data/flag_test1.csv"),
            Path(__file__).parents[0].joinpath("test_data/inputs/flag_test1.yaml"),
            Path(__file__).parents[0].joinpath("test_data/inputs/timings.yaml"),
        ],
        [
            # strings in user ids
            Path(__file__).parents[0].joinpath("test_data/flag_test2.csv"),
            Path(__file__).parents[0].joinpath("test_data/inputs/flag_test2.yaml"),
            Path(__file__).parents[0].joinpath("test_data/inputs/timings.yaml"),
        ],
        [
            # numbers in user ids
            Path(__file__).parents[0].joinpath("test_data/flag_test3.csv"),
            Path(__file__).parents[0].joinpath("test_data/inputs/flag_test3.yaml"),
            Path(__file__).parents[0].joinpath("test_data/inputs/timings.yaml"),
        ],
    ]
)
def flag_test_cases(request):
    dataframe = pd.read_csv(request.param[0], sep=";")
    yield dataframe, request.param[1], request.param[1]


def test_flag_cases_without_consent(flag_test_cases):
    flag_dataframe, _, _ = flag_test_cases
    assert all(
        flag_cases_without_consent(flag_dataframe, question_id="consent_field")[
            "flag_consent"
        ]
        == flag_dataframe["no_consent"]
    )


def test_flag_repeated_users(flag_test_cases):
    flag_dataframe, _, _ = flag_test_cases
    assert all(
        flag_repeated_users(flag_dataframe, question_id="participant_id")[
            "flag_repeated"
        ]
        == flag_dataframe["repeated_user"]
    )


def test_flag_cases_with_fake_observations(flag_test_cases):
    flag_dataframe, yaml_filename, _ = flag_test_cases
    assert all(
        flag_cases_with_fake_observations(flag_dataframe, yaml_filename)["flag_fake"]
        == flag_dataframe["fake_user"]
    )


def test_flag_speeders(flag_test_cases):
    flag_dataframe, _, timing_yaml = flag_test_cases
    with open(timing_yaml, "rb") as f:
        timing_yaml = yaml.safe_load(f)
    for timing_entry in timing_yaml:
        assert all(
            flag_speeders(flag_dataframe, timing_yaml)[f"flag_{timing_entry}"]
            == flag_dataframe[f"{timing_entry}_speeder"]
        )


def test_flag_critical_question_below_threshold(flag_test_cases):
    raise NotImplementedError


def test_flag_nonsensical_free_text(flag_test_cases):
    raise NotImplementedError
