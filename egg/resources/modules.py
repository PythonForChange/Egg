import pip
import importlib as il
from egg.resources.constants import white

def install(name: str):
    pip.main(['install', name])
    return "Done"

class Repo():
    def __init__(self,name: str):
        self.name=name
    def pull(self,package: str,functions: str):
        funcs=functions.split(" ")
        try:
            package="github_com.PythonForChange."+self.name+"."+package
            _temp = il.__import__(package, globals(), locals(), funcs, 0)
            return _temp
        except:
            print(white+"Pull failed")