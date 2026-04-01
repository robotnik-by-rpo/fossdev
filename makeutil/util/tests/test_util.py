import pytest
from http_conn import http_conn

def test_base_util():
    http_conn("https://www.wikipedia.org/")

def test_util_text():
    http_conn("https://www.wikipedia.org/","-t")

def test_util_json():
    http_conn("https://www.wikipedia.org/","-j")

if __name__ == "__main__":
    test_base_util()
    test_util_text()
    test_util_json()

