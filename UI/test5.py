from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtWebEngineWidgets import QWebEnginePage, QWebEngineView

# Create an application
app = QApplication([])

# And a window
win = QWidget()
win.setWindowTitle('QWebView Interactive Demo')

# And give it a layout
layout = QVBoxLayout()
win.setLayout(layout)

# Create and fill a QWebView
view = QWebEngineView()
view.setHtml('''
  <html>
    <head>
      <title>A Demo Page</title>

      <script language="javascript">
        // Completes the full-name control and
        // shows the submit button
        function test() {
          var fname = document.getElementById('fname').value;
          var lname = document.getElementById('lname').value;
          var full = fname + ' ' + lname;

          document.getElementById('fullname').value = full;
          document.getElementById('submit-btn').style.display = 'block';

          return full;
        }
      </script>
    </head>
    <body>
      <form>
        <label for="fname">First name:</label>
        <input type="text" name="fname" id="fname"></input>
        <br />
        <label for="lname">Last name:</label>
        <input type="text" name="lname" id="lname"></input>
        <br />
        <label for="fullname">Full name:</label>
        <input disabled type="text" name="fullname" id="fullname"></input>
        <br />
        <input style="display: none;" type="submit" id="submit-btn"></input>
      </form>
    </body>
  </html>
''')

# A button to call our JavaScript
button = QPushButton('Set Full Name')

# Interact with the HTML page by calling the completeAndReturnName
# function; print its return value to the console
# --------------------------------PyQt4语法----------------------------- #
# def complete_name():                                                  # 报错
#     frame = view.page().mainFrame()                                   # PyQt4中的mainFrame在PyQt5中已废弃
#     print(frame.evaluateJavaScript('completeAndReturnName();'))       #
# --------------------------------------------------------------------- #

# --------------------------------PyQt5语法-----------------------------
def js_callback(result):
    print(result)

def complete_name():
    view.page().runJavaScript('test();', js_callback)  # PyQt5使用runJavaScript修正
    # res=view.page().runJavaScript('test();')
    # print(res)
# ---------------------------------------------------------------------

# Connect 'complete_name' to the button's 'clicked' signal
button.clicked.connect(complete_name)

# Add the QWebView and button to the layout
layout.addWidget(view)
layout.addWidget(button)

# Show the window and run the app
win.show()
app.exec_()
