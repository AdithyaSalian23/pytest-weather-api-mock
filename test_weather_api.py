import pytest

import sys
import os
sys.path.append(os.path.dirname(__file__))

from weather_api import get_weather

from unittest.mock import patch, Mock
import requests
from weather_api import get_weather

# ✅ Success response
@patch("weather_api.requests.get")
def test_get_weather_success(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"temperature": "25°C"}
    mock_get.return_value = mock_response

    assert get_weather("mumbai") == "25°C"

# ❌ Failure response (e.g., 404 error)
@patch("weather_api.requests.get")
def test_get_weather_http_error(mock_get):
    mock_response = Mock()
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("404 Not Found")
    mock_get.return_value = mock_response

    result = get_weather("unknown")
    assert "Error:" in result


# ⚠️ Partial data (no temperature key)
@patch("weather_api.requests.get")
def test_get_weather_partial_data(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"humidity": "60%"}
    mock_get.return_value = mock_response

    assert get_weather("delhi") == "No temp data"
