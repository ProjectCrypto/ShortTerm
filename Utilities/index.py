
import os
import imp


def dynamicImport(path):
    name   = os.path.basename(path)
    pyFile = os.path.join(path,'index.py')
    module = imp.load_source(name,pyFile)
    
    return module