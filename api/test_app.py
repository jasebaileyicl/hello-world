
from app import process_query


def test_knows_about_dinos():
    assert process_query("dinos") == "dinos are great"


def test_does_not_know_about_stars():
    assert process_query("stars") == "what?"


def test_returns_name_of_team():
    # what%20is%20your%20name?
    assert process_query("What is your name?") == "test2"
