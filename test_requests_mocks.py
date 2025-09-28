
from mock_requests import weather_city

def test_get_weather(mocker):
    mock_get = mocker.patch("mock_requests.requests.get")

    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {'temperature': 25, 'condition': 'Sunny'}

    result = weather_city('Uruguay')

    assert result == {'temperature': 25, 'condition': 'Sunny'}
    mock_get.assert_called_once_with("https://api.weather.com/v1/Uruguay")

    assert mock_get.call_count == 1