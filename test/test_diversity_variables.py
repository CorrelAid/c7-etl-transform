"""Test most complex diversity variable calculation"""
from pathlib import Path

import pandas as pd
import pytest

from transform_code.diversity_variables import (
    dv_get_beeintraechtigung_oder_behinderung,
    dv_get_schwerbehinderung,
)


@pytest.fixture(
    params=[
        Path(__file__).parents[0].joinpath("test_data/dv_test_schwerbehinderung.csv")
    ]
)
def disability_dataframe(request):
    dataframe = pd.read_csv(request.param)
    yield dataframe


def test_schwerbehinderung(disability_dataframe):
    assert all(
        dv_get_schwerbehinderung(disability_dataframe)
        == disability_dataframe["schwerbehinderung"]
    )


def test_beeintraechtigung(disability_dataframe):
    assert all(
        dv_get_beeintraechtigung_oder_behinderung(disability_dataframe)
        == disability_dataframe["behindert_oder_eingeschraenkt"]
    )
