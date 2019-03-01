import os, subprocess
from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile

def load_standard_import_tool_plugin():
    '''
    Download the 1.2 release of StandardImportToolPlugin from Github and unzip it locally.
    '''
    StandardImportToolPluginDir = os.path.join(".","StandardImportToolPlugin")
    #extra subdir in the archive    
    StandardImportToolPluginExe = os.path.join(StandardImportToolPluginDir,"Release", "StandardImportToolPlugin.exe")
    if not os.path.exists(StandardImportToolPluginExe):
        resp = urlopen('https://github.com/cat-cfs/StandardImportToolPlugin/releases/download/1.2/Release.zip')
        zipfile = ZipFile(BytesIO(resp.read()))

        #os.makedirs(StandardImportToolPluginDir)
        zipfile.extractall(path=StandardImportToolPluginDir)
    return StandardImportToolPluginExe


