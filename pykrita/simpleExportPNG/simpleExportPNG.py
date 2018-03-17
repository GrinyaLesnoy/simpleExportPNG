import sys 
import importlib
import krita
from krita import * 
class simpleExportPNGExtension(krita.Extension):
    def __init__(self, parent):
        super().__init__(parent)
		
    def setup(self):
        try:
            action = krita.Krita.instance().createAction("simpleExportPNG", "Export to PNG")
            action.setToolTip("simple Export to PNG")
            action.triggered.connect(self.exportPNG)
        except:
            pass 
		
    def createActions(self, window):
        action = window.createAction("simpleExportPNG", "Export to PNG", "tools/scripts")
        action.setToolTip("simple Export to PNG")
        action.triggered.connect(self.exportPNG)

    def exportPNG(self):
        d = Krita.instance().activeDocument()
        path=d.fileName()
        if(path==''):
            return
        path=path[:path.rfind('.')]+'.png'  
        i = InfoObject();
        i.setProperty("alpha", True)
        i.setProperty("compression", 3) 
        d.exportImage(path,i)
		 

Scripter.addExtension(simpleExportPNGExtension(krita.Krita.instance()))