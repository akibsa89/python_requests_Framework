import pytest
import json
import os
from datetime import datetime

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # Add timestamp to report file name
    report_dir = "../reports"
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    config.option.htmlpath = f"{report_dir}/report_{now}.html"

    @pytest.fixture(scope="session", autouse=True)
    def setup_teardown():
        print("\nSetting up resources...")
        yield
        print("\nTearing down resources...")
#hi
@pytest.fixture
def load_user_data():
    """Fixture to load JSON test data"""
    json_file_path = os.path.join(os.path.dirname(__file__), "../data/test_data.json")
    with open(json_file_path) as json_file:
        data = json.load(json_file)
    return data

'''os.path.dirname(__file__) → Gets the directory where conftest.py is located.
../data/test_data.json → Moves one level up & go to root level (..) and into the data/ folder to find test_data.json.'''


