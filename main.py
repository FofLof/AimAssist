from networktables import NetworkTables
import cv2
from cone import ConePipe
from cube import CubePipe
from cscore import CameraServer

CameraServer.enableLogging()
camera = CameraServer.startAutomaticCapture()
camera.setResolution(600, 480)

table = NetworkTables.getTable("/vision")


# x = 0;
# y = 0;

def processConeInfo():
    conePipeline.process(camera)
    center_x_positions = []
    center_y_positions = []
    widths = []
    heights = []

    for contour in conePipeline.find_contours_output:
        x, y, w, h = cv2.boundingRect(contour)
        center_x_positions.append(x + w / 2)  # X and Y are coordinates of the top-left corner of the bounding box
        center_y_positions.append(y + h / 2)
        widths.append(w)
        heights.append(y)
        # Publish to the '/vision' network table
    table.putNumberArray("centerX", center_x_positions)
    table.putNumberArray("centerY", center_y_positions)
    table.putNumberArray("width", widths)
    table.putNumberArray("height", heights)


def processCubeInfo():
    cubePipeline.process(camera)
    center_x_positions = []
    center_y_positions = []
    widths = []
    heights = []

    for blob in cubePipeline.find_blobs_output:
        x, y, w, h = cv2.boundingRect(blob)
        center_x_positions.append(x + w / 2)  # X and Y are coordinates of the top-left corner of the bounding box
        center_y_positions.append(y + h / 2)
        widths.append(w)
        heights.append(y)
        # Publish to the '/vision' network table
    table.putNumberArray("cubeCenterX", center_x_positions)
    table.putNumberArray("cubeCenterY", center_y_positions)
    table.putNumberArray("cubeWidth", widths)
    table.putNumberArray("cubeHeight", heights)


def main():
    processCubeInfo()
    processConeInfo()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    NetworkTables.initialize(server="10.20.73.2")
    conePipeline = ConePipe()
    cubePipeline = CubePipe()
    while True:
        main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
