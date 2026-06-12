from pathlib import Path
import pytest

from kubiks import load


def get_example(name: str) -> Path:
    return Path(__file__).resolve().parents[1] / "examples" / name

def test_load_1():
    assert load(str(get_example("app_config.kbk"))) != None

def test_load_2():
    assert load(str(get_example("user.kbk"))) != None

def test_load_3():
    with pytest.raises(SyntaxError):
        load(str(get_example("incorrect_game.kbk")))
