import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QDialog, QPushButton
from PyQt5.QtCore import QTimer, Qt

class ReminderDialog(QDialog):
    def __init__(self, parent=None):
        super(ReminderDialog, self).__init__(parent)

        self.setWindowTitle("Reminder")
        self.setGeometry(300, 300, 300, 100)

        layout = QVBoxLayout()
        label = QLabel("Reminder: Take a break!")
        label.setAlignment(Qt.AlignCenter)

        close_button = QPushButton("Close")
        close_button.clicked.connect(self.close)

        layout.addWidget(label)
        layout.addWidget(close_button)

        self.setLayout(layout)
        self.setStyleSheet("QDialog { background-color: crimson; }")

class ReminderApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Reminder App')
        self.setGeometry(300, 300, 300, 100)

        layout = QVBoxLayout()

        self.label = QLabel('Get ready for your reminder in 20 minutes!')
        self.label.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.label)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.show_reminder)
        self.timer.start(20 * 60 * 1000)  # 20 minutes in milliseconds

    def show_reminder(self):
        reminder_dialog = ReminderDialog(self)
        reminder_dialog.exec_()

        # Reset the timer for the next reminder
        self.timer.start(20 * 60 * 1000)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    reminder_app = ReminderApp()
    reminder_app.show()
    sys.exit(app.exec_())
