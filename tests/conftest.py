import allure
import pytest
import requests
from dotenv import load_dotenv
from pytest_voluptuous import S

@pytest.fixture(autouse=True)
def env():
    load_dotenv()