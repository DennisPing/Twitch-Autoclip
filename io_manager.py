import os
import sys
import requests

class IO_Manager:
    """
    A class to manage user input and file output
    Supports quit functionality
    """

    def __init__(self):
        self.cwd = os.getcwd()

    def prompt_input(self):
        print("Type 'q' or 'quit' anytime to quit.")
        prompts = []
        prompts.append(self.prompt_url())
    
    def check_quit(self, userinput):
        if userinput.lower() == 'q' or userinput.lower() == 'quit':
            sys.exit()
        return

    def prompt_url(self):
        url = input("Enter a Twitch VOD URL: ")
        self.check_quit(url)
        try:
            response = requests.get(url)
        except requests.ConnectionError as exception:
            print("Error, invalid URL")

        split = url.split("/")
        try:
            split[2] == "www.twitch.tv" and split[3] == "videos"
        except ValueError:
            print("Not a Twitch VOD URL")
        return split[4]


    def get_streamer(self):
        streamers = ['jakenbakelive','fuslie','supcaitlin']

        options = {
            '1':'jakenbakelive',
            '2':'fuslie',
            '3':'supcaitlin'
        }
        while True:
            try: 
                for i, each in enumerate(streamers):
                    print(f"{i+1}: {streamers[i]}")
                selected = input("Select a streamer to analyze: ")
                self.check_quit(selected)
                return options[selected]
            except ValueError:
                print("Invalid streamer selection")
                print()
                continue

