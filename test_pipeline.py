import pandas as pd
import pytest
from pipeline.main import shape


@pytest.fixture #a piece of pre-determined data used by a test
def make_df():
    d = {'col1': [1, 2, 3, 4, 7], 'col2': [4, 5, 6, 9, 5], 'col3': [7, 8, 12, 1, 11]}
    df = pd.DataFrame(data=d)
    return df

@pytest.mark.test
def test_shape(make_df):  # Utilize the fixture by passing it as an argument
    assert shape(make_df)==5  # check number of rows, here should be 5, but assertion is 10. So the test fails. 
