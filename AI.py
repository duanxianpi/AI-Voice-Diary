# This Python file uses the following encoding: utf-8

import sys
import requests
from time import sleep

class AI:
    def __init__(self):
        self.headers = {
           "authorization": "d17d0a4a360b4d57961faf6c4e169b6e",
           "content-type": "application/json"
        }
        self.transcript_endpoint = "https://api.assemblyai.com/v2/transcript"
        self.upload_endpoint = 'https://api.assemblyai.com/v2/upload'


    def read_record(self,filename):
        print("Tes")
        with open(filename, 'rb') as _file:
            print("Tes")
            while True:
                self.data = _file.read(5242880)
                print("Tes")
                if not self.data:
                    break
                yield self.data

    def getTranscript(self,filename):
        self.upload_response = requests.post(
           self.upload_endpoint,
           headers=self.headers, data=self.read_record(filename)
        )
        self.transcript_request = {'audio_url': self.upload_response.json()['upload_url'],"auto_highlights": True}
        self.transcript_response = requests.post(self.transcript_endpoint, json=self.transcript_request, headers=self.headers)
    # set up polling
        self.polling_response = requests.get(self.transcript_endpoint+"/"+self.transcript_response.json()['id'], headers=self.headers)
       # filename = self.transcript_response.json()['id'] + '.txt'
    # if our status isn’t complete, sleep and then poll again
        while self.polling_response.json()['status'] != 'completed':
           self.polling_response = requests.get(self.transcript_endpoint+"/"+self.transcript_response.json()['id'], headers=self.headers)
           print("File is", self.polling_response.json()['status'])
        return self.polling_response.json()


