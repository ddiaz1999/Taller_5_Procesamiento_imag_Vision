import cv2
import os
import json
from camera_model import *

if __name__ == '__main__':

    path = r'C:\Users\di-di\PycharmProjects\Taller_5_Procesamiento_imag_Vision'
    file_name = 'calibration1.json'
    json_file = os.path.join(path, file_name)

    with open(json_file) as fp:
        json_data = json.load(fp)

    K, d, h, tilt, pan = json_data.values()
    K = np.array(K)

    # intrinsics parameters
    width = 585
    height = 1024
    
    #extrinsics parameters
    R = set_rotation(tilt, pan, 0) #(tilt, pan, skew)
    t = np.array([0, -d, h])
    
    # create camera
    camera = projective_camera(K, width, height, R, t)

    lenght_side = 1
    half_lenght = lenght_side/2
    cube_3D = np.array([[half_lenght, half_lenght, -half_lenght], [half_lenght, -half_lenght, -half_lenght], [-half_lenght, -half_lenght, -half_lenght], [-half_lenght, half_lenght, -half_lenght],
                        [half_lenght, half_lenght, half_lenght], [half_lenght, -half_lenght, half_lenght], [-half_lenght, -half_lenght, half_lenght], [-half_lenght, half_lenght, half_lenght]])

    cube_2D = projective_camera_project(cube_3D, camera)
    print(cube_2D)
    image_projective = 255 * np.ones(shape=[camera.height, camera.width, 3], dtype=np.uint8)
    cv2.line(image_projective, (cube_2D[0][0], cube_2D[0][1]), (cube_2D[1][0], cube_2D[1][1]), (255, 0, 0), 3)
    cv2.line(image_projective, (cube_2D[0][0], cube_2D[0][1]), (cube_2D[3][0], cube_2D[3][1]), (255, 0, 0), 3)

    cv2.line(image_projective, (cube_2D[1][0], cube_2D[1][1]), (cube_2D[5][0], cube_2D[5][1]), (255, 0, 0), 3)
    cv2.line(image_projective, (cube_2D[1][0], cube_2D[1][1]), (cube_2D[2][0], cube_2D[2][1]), (255, 0, 0), 3)

    cv2.line(image_projective, (cube_2D[2][0], cube_2D[2][1]), (cube_2D[3][0], cube_2D[3][1]), (255, 0, 0), 3)
    cv2.line(image_projective, (cube_2D[2][0], cube_2D[2][1]), (cube_2D[6][0], cube_2D[6][1]), (255, 0, 0), 3)

    cv2.line(image_projective, (cube_2D[3][0], cube_2D[3][1]), (cube_2D[7][0], cube_2D[7][1]), (255, 0, 0), 3)

    cv2.line(image_projective, (cube_2D[4][0], cube_2D[4][1]), (cube_2D[5][0], cube_2D[5][1]), (255, 0, 0), 3)
    cv2.line(image_projective, (cube_2D[4][0], cube_2D[4][1]), (cube_2D[7][0], cube_2D[7][1]), (255, 0, 0), 3)

    cv2.line(image_projective, (cube_2D[6][0], cube_2D[6][1]), (cube_2D[5][0], cube_2D[5][1]), (255, 0, 0), 3)
    cv2.line(image_projective, (cube_2D[6][0], cube_2D[6][1]), (cube_2D[7][0], cube_2D[7][1]), (255, 0, 0), 3)

    cv2.line(image_projective, (cube_2D[0][0], cube_2D[0][1]), (cube_2D[4][0], cube_2D[4][1]), (255, 0, 0), 3)

    cv2.imshow("Image", image_projective)
    cv2.waitKey(0)
