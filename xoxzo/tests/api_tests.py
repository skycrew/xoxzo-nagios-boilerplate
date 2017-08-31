from mock import patch, call
from unittest import TestCase
from xoxzo.api import XoxzoApi


class TestApi(TestCase):

    @patch("xoxzo.api.yaml")
    def setUp(self, mock_yaml):
        mock_yaml.load.return_value = {
            "api_sid": "1234567890Qwerty",
            "auth_token": "Qwerty1234567890",
            "api_url": "https://api.mock.com"
        }
        self.api = XoxzoApi()

    @patch("xoxzo.api.post")
    def test_call(self, mock_post):
        caller = "+601312345678"
        recipient = "+60123456789"
        message = "Hello world"
        self.api.call(caller, recipient, message)

        mock_post.assert_called_once_with("https://api.mock.com/voice/simple/playback/",
                                          auth=("1234567890Qwerty", "Qwerty1234567890"),
                                          data={"tts_message": "Hello world",
                                                "tts_lang": "en",
                                                "caller": "+601312345678",
                                                "recipient": "+60123456789"})

    @patch("xoxzo.api.XoxzoApi.call")
    def test_calls(self, mock_call):
        caller = "+601312345678"
        recipients = ["+60123456789", "+60199999999"]
        message = "Hello world"
        self.api.calls(caller, recipients, message)

        self.assertTrue(mock_call.called)
        self.assertEqual(2, mock_call.call_count)

        mock_call.assert_has_calls([call("+601312345678", "+60123456789", "Hello world", "en"),
                                    call("+601312345678", "+60199999999", "Hello world", "en")])

    @patch("xoxzo.api.get")
    def test_get_call_status(self, mock_get):
        self.api.get_call_status("12345")

        mock_get.assert_called_once_with("https://api.mock.com/voice/simple/playback/12345/",
                                         auth=("1234567890Qwerty", "Qwerty1234567890"))
