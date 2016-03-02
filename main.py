import htmlPy
import os
#from PyQt4 import QtGui


# Initial configurations
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# GUI initialization
app = htmlPy.AppGUI(title=u"Instrument Cluster Control", maximized=True)

# GUI configurations
app.template_path = os.path.abspath(".")
app.static_path = os.path.abspath(".")

# app.window.setWindowIcon(QtGui.QIcon(BASE_DIR + "/img/Tesla.png"))
app.template = ("index.html", {'cwd': BASE_DIR})

class Buttons(htmlPy.Object):


    def __init__(self):
        super(Buttons, self).__init__()
        return

    @htmlPy.Slot()
    def helloWorld(self):
        app.evaluate_javascript("alert('Hello World')")
        return

app.bind(Buttons())
app.start()
