import json

from networktables import NetworkTables
import cv2
from cone import ConePipe
from cube import CubePipe
from cscore import CameraServer, UsbCamera, VideoSource

CameraServer.enableLogging()
camera = CameraServer.startAutomaticCapture()
camera.setResolution(600, 480)

table = NetworkTables.getTable("/vision")

def processConeInfo():
    conePipeline.process(camera)
    center_x_positions = []
    center_y_positions = []
    widths = []
    heights = []
    area = []

    for contour in conePipeline.find_contours_output:
        x, y, w, h = cv2.boundingRect(contour)
        a = cv2.contourArea(contour)
        center_x_positions.append(x + w / 2)  # X and Y are coordinates of the top-left corner of the bounding box
        center_y_positions.append(y + h / 2)
        widths.append(w)
        heights.append(y)
        area.append(a)
        # Publish to the '/vision' network table
    table.putNumberArray("coneCenterX", center_x_positions)
    table.putNumberArray("coneCenterY", center_y_positions)
    table.putNumberArray("coneWidth", widths)
    table.putNumberArray("coneHeight", heights)
    table.putNumberArray("coneArea", area)


def processCubeInfo():
    cubePipeline.process(camera)
    center_x_positions = []
    center_y_positions = []
    widths = []
    heights = []
    area = []

    for contour in cubePipeline.find_contours_output:
        x, y, w, h = cv2.boundingRect(contour)
        a = cv2.contourArea(contour)
        center_x_positions.append(x + w / 2)  # X and Y are coordinates of the top-left corner of the bounding box
        center_y_positions.append(y + h / 2)
        widths.append(w)
        heights.append(y)
        area.append(a)
        # Publish to the '/vision' network table
    table.putNumberArray("cubeCenterX", center_x_positions)
    table.putNumberArray("cubeCenterY", center_y_positions)
    table.putNumberArray("cubeWidth", widths)
    table.putNumberArray("cubeHeight", heights)
    table.putNumberArray("cubeArea", area)


def main():
    processCubeInfo()
    processConeInfo()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    CameraServer.enableLogging()
    camera = CameraServer.startAutomaticCapture()
    camera.setResolution(600, 480)
    NetworkTables.initialize(server="10.20.73.2")
    conePipeline = ConePipe()
    cubePipeline = CubePipe()

    while True:
        main()

