#!/usr/bin/env python3
import os

def ReadFile(FileName: str) -> list[str]:
    return open(FileName, "r").readlines()

def Main():
    Channels = [Channel.split('|')[0].strip() for Channel in ReadFile("./Ongoing.txt") if Channel]
    for Channel in Channels:
        os.system(f"google-chrome-stable --incognito https://youtube.com/channel/{Channel}")

if __name__=="__main__":
    Main()