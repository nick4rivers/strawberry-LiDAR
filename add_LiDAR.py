import os
from qgis.core import iface
from PyQt5.QtWidgets import QFileDialog

# ----- File picker and path to directory of LiDAR ------
message_text = 'Select a directory of....'
iface.messageBar().pushMessage(message_text, duration=5)
work_path = QFileDialog.getExistingDirectory()

# ---- get a list of the directories ----
dir_list = os.listdir(work_path)
print(len(dir_list))

# ---- loop to add all LiDAR tiles ----
for dir in dir_list:
    lidar_path = os.path.join(work_path, dir, dir + '.tif')
    print(lidar_path)
    iface.addRasterLayer(lidar_path)
