#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml

from requests import get, post
from os.path import join, dirname


class XoxzoApi(object):

    def __init__(self):
        self.config = yaml.load(open(join(dirname(__file__), "config.yml")))

    def call(self, caller, recipient, message, language="en"):
        """
        Make a text to speech call
        :param caller: Caller number, Required=True, DataType=Numeric, Example=+8190123456789
        :param recipient: Call recipient, Required=Yes, DataType=E.164, Example=+8190123456789
        :param message: text to playback, Required=Yes, DataType=UTF-8, Example=Hello world!
        :param language: language of the text, Required=Yes, DataType=ISO 639-1, Example=en
        :return: boolean of successful call
        """
        data = {
            "caller": caller,
            "recipient": recipient,
            "tts_message": message,
            "tts_lang": language
        }

        result = post("%s/voice/simple/playback/" % self.config["api_url"],
                      auth=(self.config["api_sid"], self.config["auth_token"]),
                      data=data)

        if not result.status_code == 201:
            return False

        call_id = result.json()[0]["callid"]

        status = self.get_call_status(call_id)

        if status == "ANSWERED":
            return True
        else:
            return False

    def calls(self, caller, recipients, message, language="en"):
        """
        Make multiple text to speech call
        :param caller: Caller number, Required=True, DataType=Numeric, Example=+8190123456789
        :param recipients: Call recipients, Required=Yes, DataType=E.164, Example=[+8190123456789, +60123456789]
        :param message: text to playback, Required=Yes, DataType=UTF-8, Example=Hello world!
        :param language: language of the text, Required=Yes, DataType=ISO 639-1, Example=en
        :return: Call status
        """
        status = {}
        for recipient in recipients:
            status[recipient] = self.call(caller, recipient, message, language)

        return status

    def get_call_status(self, call_id):
        """
        Get call status using callid
        :param call_id: Call id return from voice api
        :return: ANSWERED, FAILED, IN PROGRESS, NO ANSWER
        """
        result = get("%s/voice/simple/playback/%s/" % (self.config["api_url"], call_id),
                     auth=(self.config["api_sid"], self.config["auth_token"]))

        if not result.status_code == 200:
            return None

        return result.json()["status"]
