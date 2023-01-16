from networktables import NetworkTables
import cv2
from cone import ConePipe
from cube import CubePipe
from cscore import CameraServer

CameraServer.enableLogging()
camera = CameraServer.startAutomaticCapture()
camera.setResolution(600, 480)


# x = 0;
# y = 0;

def processConeInfo():
    conePipeline.process(camera)
    # center_x_positions = []
    # center_y_positions = []
    # widths = []
    # heights = []


def processCubeInfo():
    cubePipeline.process(camera)


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
