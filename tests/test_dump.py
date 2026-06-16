import pytest

from kubiks import Percent, dumps

def test_dump1():
    assert dumps({
        'percent': Percent(67),
        'float': 0.012,
        'string': "Hi!",
        'list': [Percent(12), Percent(52)],
        'dict': {
            'name': "Kubik",
            'int': 12,
            'bool': False,
            'null': None}
        }) == """{
    percent |= 67%
    float |= 0.012
    string |= "Hi!"
    list |= [12%, 52%]
    dict |= {
        name |= "Kubik"
        int |= 12
        bool |= false
        null |= null
    }
}"""