import os
from pathlib import Path
def getFiles(startpath=".", beginswith="", contains="", endswith=""):
    #TODO add contains support
    tfiles = list(Path(startpath).rglob(beginswith+"*"+endswith))
    abspath = os.path.abspath(startpath)
    fullnames = [os.path.join(abspath, file) for file in tfiles]
    return fullnames
