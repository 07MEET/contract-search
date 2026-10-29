from pathlib import Path

import pytest
from streamlit.testing.v1 import AppTest

from clausesearch.data import DATA_DIR

APP = str(Path(__file__).resolve().parent.parent / "app.py")
pytestmark = pytest.mark.skipif(
    not (DATA_DIR / "benchmarks" / "cuad.json").exists(), reason="run scripts/download_data.py first"
)


def test_app_shows_passages_for_a_question():
    at = AppTest.from_file(APP, default_timeout=60).run()
    at.text_input[0].input("What is the governing law for this contract?").run()
    assert not at.exception
    assert not at.warning
    assert any("characters" in m.value for m in at.markdown)


def test_app_says_so_when_nothing_matches():
    at = AppTest.from_file(APP, default_timeout=60).run()
    at.text_input[0].input("zebra giraffe").run()
    assert not at.exception
    assert "No relevant clause" in at.warning[0].value
