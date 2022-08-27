import pytest
import os


def test_temporary_db(monkeypatch, get_temporary_db_path_string):
    monkeypatch.setenv("DB_URL", get_temporary_db_path_string)
    assert os.getenv("DB_URL") == get_temporary_db_path_string
