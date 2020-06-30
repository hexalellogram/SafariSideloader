#!/usr/bin/env python3

import sys

def downloadChromeExtension(url):
    print("Downloading Chrome Extension")

def downloadFirefoxExtension(url):
    print("Downloading Firefox Extension")

def downloadExtension(url):
    print("Downloading Extension")
    if "chrome.google.com/webstore/detail" in url:
        print ("Chrome Web Store URL detected")
        downloadChromeExtension(url)
    elif "addons.mozilla.org/en-US/firefox/addon" in url:
        print ("Firefox Extension URL detected")
        downloadFirefoxExtension(url)
    else:
        print("Invalid URL detected! Please pass in the URL of the extension's page in the Chrome Web Store or Firefox Browser Add-Ons gallery.")

def extractExtension():
    print("extract")

def convertExtension():
    print("convert")

def compileXcodeProject():
    print("compile")

def runXcodeProject():
    print("run")

downloadExtension(sys.argv[1])
extractExtension()
compileXcodeProject()
runXcodeProject()
