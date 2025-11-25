import pytest

from lab02.src.arrays import min_max


@pytest.mark.parametrize(
    "massive,expected",
    [
        ([3, -1, 5, 5, 0], (-1, 5)),
        ([42], (42, 42)),
        ([-5, -2, -9], (-9, -2)),
        ([], ValueError),
        ([1.5, 2, 2.0, -3.1], (-3.1, 2)),
    ],
)
def test_min_max(massive, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            min_max(massive)
    else:
        assert min_max(massive) == expected
