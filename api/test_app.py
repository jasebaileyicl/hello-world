
from app import process_query


def test_knows_about_dinos():
    assert process_query("dinos") == "dinos are great"


def test_does_not_know_about_stars():
    assert process_query("stars") == "what?"
