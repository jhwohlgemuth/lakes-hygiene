from pathlib import Path
import polars as pl

from lib.core import add

FIXTURES = Path("./tests/fixtures/")


def test_core():
    expected = 42
    assert add(40, 2) == 42


def test_fixture():
    df = pl.read_csv(FIXTURES / "data.csv")
    assert df.shape[0] == 3
