import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QFileDialog

app = QApplication(sys.argv)

a = QtWidgets.QWidget()
a.show()
# options = QFileDialog.Options()
# file_name, _ = QFileDialog.getOpenFileName(a, "Open Data File", "",
#                                            "Data Files (*.docx,*.zip);;zip_files (*.zip);;All Files (*)",
#                                            options=options)
b = QFileDialog(a)

b.setFileMode(QFileDialog.ExistingFile)
b.setNameFilter('Data file_path (*.abf *.docx *.zip)')
if b.exec():
    file_name = b.selectedFiles()
    print(file_name)
b.show()


# print(file_name)
# print(_)
app.exec()
