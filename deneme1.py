import sys
from taurus.qt.qtgui.panel import TaurusForm
from taurus.qt.qtgui.application import TaurusApplication

app = TaurusApplication(sys.argv)

attrs = [ 'state', 'position', 'velocity', 'acceleration' ]
model = [ 'motor/icepap/01/%s' % attr for attr in attrs ]

w = TaurusForm()
w.model = model
w.show()
sys.exit(app.exec_())