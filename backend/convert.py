#!/usr/bin/env python3

import sys
import subprocess
import os
import json

def downloadChromeExtension(url):
    print("Downloading Chrome Extension")
    filename = "Extension.crx"

    slashIndex = url.rfind("/")
    extensionID = url[(slashIndex+1):]


    chromeVersion = "83.0.4103.116"

    extensionURL = "https://clients2.google.com/service/update2/crx?response=redirect&prodversion=" + chromeVersion + "&acceptformat=crx2,crx3&x=id%3D" + extensionID + "%26uc"

    subprocess.run(["curl", "-L", extensionURL, "-o", filename])
    return filename

def downloadFirefoxExtension(url):
    print("Downloading Firefox Extension")
    print("We don't support Firefox extensions just yet. Stay tuned for more upcoming.")
    exit()
    filename = "Extension.xpi"
    subprocess.run(["curl", "-L", extensionURL, "-o", filename])
    return filename

def downloadExtension(url):
    print("Downloading Extension")
    if "chrome.google.com/webstore/detail" in url:
        print ("Chrome Web Store URL detected")
        return downloadChromeExtension(url)
    elif "addons.mozilla.org/en-US/firefox/addon" in url:
        print ("Firefox Extension URL detected")
        return downloadFirefoxExtension(url)
    else:
        return print("Invalid URL detected! Please pass in the URL of the extension's page in the Chrome Web Store or Firefox Browser Add-Ons gallery.")

def extractExtension(filename):
    print("Extracting Extension")
    extract = subprocess.run(["unzip", filename, "-d", "Extension"]);
    if extract.returncode == 0:
        print("Extension extracted successfully")
    elif extract.returncode == 1:
        print("Expected error in extension extraction due to extra bytes in extension header")
    elif extract.returncode != 1:
        print ("Unknown error in extension extraction")

def convertExtension():
    print("Converting Extension to Safari compatible WebExtension")

    retval = os.system("echo yes | xcrun safari-web-extension-converter --no-open --copy-resources Extension")

    if retval != 0:
        print("Error in conversion of extension to Xcode Project!")
        print("This may simply indicate that certain APIs the extension are unsupported by Safari, or it may indicate that there was a more serious problem with the conversion.")
        print("In any case, the converted extension may not fully work on Safari. You have been warned.")

def compileXcodeProject():
    print("Compiling Generated Xcode Project")
    with open("Extension/manifest.json", "r") as f:
        extensionData = json.load(f)
    extensionName = extensionData['name']
    os.chdir(extensionName)
    subprocess.run(["xcodebuild"])

    return extensionName

def openExtensionApp(extensionName):
    appName = extensionName + ".app"
    appPath = "build/Release/" + appName
    subprocess.run(["open", appPath])

extensionFile = downloadExtension(sys.argv[1])
extractExtension(extensionFile)
convertExtension()
extName = compileXcodeProject()
openExtensionApp(extName)
