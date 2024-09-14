#This code is a snippet of a larger project I did that uses computer vision to grade photos through attributes such as red eye detection, facial recognition, blur, saturation, brightness, etc. It also enhances the photo using what it found through the analysis.

import PIL.Image
from PIL import Image
import time
import cv2
import numpy as np
import math

class blur:

    def blur1():
        pic1Blur = fileDict["pic1"]

        try:
            dummy1 = Image.open(pic1Blur)
            time.sleep(0.05)
            dummy1.close
        except (FileNotFoundError, AttributeError):
            return "error"

        img1 = cv2.imread(pic1Blur, cv2.IMREAD_GRAYSCALE)
        laplacian1 = cv2.Laplacian(img1, cv2.CV_64F).var()

        if laplacian1 <= 50:
            blurDict["picOneBlur"] = -3
        elif laplacian1 > 50 and laplacian1 <= 125:
            blurDict["picOneBlur"] = 5.75
        elif laplacian1 > 125 and laplacian1 <= 200:
            blurDict["picOneBlur"] = 6
        elif laplacian1 > 200 and laplacian1 <= 400:
            blurDict["picOneBlur"] = 6.5
        elif laplacian1 > 400 and laplacian1 <= 1000:
            blurDict["picOneBlur"] = 6.75
        else:
            blurDict["picOneBlur"] = 7

    def blur2():
        pic2Blur = fileDict["pic2"]

        try:
            dummy2 = Image.open(pic2Blur)
            time.sleep(0.05)
            dummy2.close
        except (FileNotFoundError, AttributeError):
            return "error"

        img2 = cv2.imread(pic2Blur, cv2.IMREAD_GRAYSCALE)
        laplacian2 = cv2.Laplacian(img2, cv2.CV_64F).var()

        if laplacian2 <= 50:
            blurDict["picTwoBlur"] = -3
        elif laplacian2 > 50 and laplacian2 <= 125:
            blurDict["picTwoBlur"] = 5.75
        elif laplacian2 > 125 and laplacian2 <= 200:
            blurDict["picTwoBlur"] = 6
        elif laplacian2 > 200 and laplacian2 <= 400:
            blurDict["picTwoBlur"] = 6.5
        elif laplacian2 > 400 and laplacian2 <= 1000:
            blurDict["picTwoBlur"] = 6.75
        else:
            blurDict["picTwoBlur"] = 7

    def blur3():
        pic3Blur = fileDict["pic3"]

        try:
            dummy3 = Image.open(pic3Blur)
            time.sleep(0.05)
            dummy3.close
        except (FileNotFoundError, AttributeError):
            return "error"

        img3 = cv2.imread(pic3Blur, cv2.IMREAD_GRAYSCALE)
        laplacian3 = cv2.Laplacian(img3, cv2.CV_64F).var()

        if laplacian3 <= 50:
            blurDict["picThreeBlur"] = -3
        elif laplacian3 > 50 and laplacian3 <= 125:
            blurDict["picThreeBlur"] = 5.75
        elif laplacian3 > 125 and laplacian3 <= 200:
            blurDict["picThreeBlur"] = 6
        elif laplacian3 > 200 and laplacian3 <= 400:
            blurDict["picThreeBlur"] = 6.5
        elif laplacian3 > 400 and laplacian3 <= 1000:
            blurDict["picThreeBlur"] = 6.75
        else:
            blurDict["picThreeBlur"] = 7

    def blur4():
        pic4Blur = fileDict["pic4"]

        try:
            dummy4 = Image.open(pic4Blur)
            time.sleep(0.05)
            dummy4.close
        except (FileNotFoundError, AttributeError):
            return "error"

        img4 = cv2.imread(pic4Blur, cv2.IMREAD_GRAYSCALE)
        laplacian4 = cv2.Laplacian(img4, cv2.CV_64F).var()

        if laplacian4 <= 50:
            blurDict["picFourBlur"] = -3
        elif laplacian4 > 50 and laplacian4 <= 125:
            blurDict["picFourBlur"] = 5.75
        elif laplacian4 > 125 and laplacian4 <= 200:
            blurDict["picFourBlur"] = 6
        elif laplacian4 > 200 and laplacian4 <= 400:
            blurDict["picFourBlur"] = 6.5
        elif laplacian4 > 400 and laplacian4 <= 1000:
            blurDict["picFourBlur"] = 6.75
        else:
            blurDict["picFourBlur"] = 7

    def blur5():
        pic5Blur = fileDict["pic5"]

        try:
            dummy5 = Image.open(pic5Blur)
            time.sleep(0.05)
            dummy5.close
        except (FileNotFoundError, AttributeError):
            return "error"

        img5 = cv2.imread(pic5Blur, cv2.IMREAD_GRAYSCALE)
        laplacian5 = cv2.Laplacian(img5, cv2.CV_64F).var()

        if laplacian5 <= 50:
            blurDict["picFiveBlur"] = -3
        elif laplacian5 > 50 and laplacian5 <= 125:
            blurDict["picFiveBlur"] = 5.75
        elif laplacian5 > 125 and laplacian5 <= 200:
            blurDict["picFiveBlur"] = 6
        elif laplacian5 > 200 and laplacian5 <= 400:
            blurDict["picFiveBlur"] = 6.5
        elif laplacian5 > 400 and laplacian5 <= 1000:
            blurDict["picFiveBlur"] = 6.75
        else:
            blurDict["picFiveBlur"] = 7


class contrast:

    def contrast1():
        cImg1 = fileDict["pic1"]

        try:
            cDummy1 = Image.open(cImg1)
            time.sleep(0.05)
            cDummy1.close
        except (FileNotFoundError, AttributeError):
            return "error"

        cImg1Read = cv2.imread(cImg1)
        cImg1Gray = cv2.cvtColor(cImg1Read, cv2.COLOR_BGR2GRAY)
        contr1 = cImg1Gray.std()

        if contr1 < 30:
            contrastDict["picOneContrast"] = 2
        elif contr1 >= 30 and contr1 < 50:
            contrastDict["picOneContrast"] = 5.3
        elif contr1 >= 50 and contr1 < 150:
            contrastDict["picOneContrast"] = 3.3
        else:
            contrastDict["picOneContrast"] = 1.5

    def contrast2():
        cImg2 = fileDict["pic2"]

        try:
            cDummy2 = Image.open(cImg2)
            time.sleep(0.05)
            cDummy2.close
        except (FileNotFoundError, AttributeError):
            return "error"

        cImg2Read = cv2.imread(cImg2)
        cImg2Gray = cv2.cvtColor(cImg2Read, cv2.COLOR_BGR2GRAY)
        contr2 = cImg2Gray.std()

        if contr2 < 30:
            contrastDict["picTwoContrast"] = 2
        elif contr2 >= 30 and contr2 < 50:
            contrastDict["picTwoContrast"] = 5.3
        elif contr2 >= 50 and contr2 < 150:
            contrastDict["picTwoContrast"] = 3.3
        else:
            contrastDict["picTwoContrast"] = 1.5

    def contrast3():
        cImg3 = fileDict["pic3"]

        try:
            cDummy3 = Image.open(cImg3)
            time.sleep(0.05)
            cDummy3.close
        except (FileNotFoundError, AttributeError):
            return "error"

        cImg3Read = cv2.imread(cImg3)
        cImg3Gray = cv2.cvtColor(cImg3Read, cv2.COLOR_BGR2GRAY)
        contr3 = cImg3Gray.std()

        if contr3 < 30:
            contrastDict["picThreeContrast"] = 2
        elif contr3 >= 30 and contr3 < 50:
            contrastDict["picThreeContrast"] = 5.3
        elif contr3 >= 50 and contr3 < 150:
            contrastDict["picThreeContrast"] = 3.3
        else:
            contrastDict["picThreeContrast"] = 1.5

    def contrast4():
        cImg4 = fileDict["pic4"]

        try:
            cDummy4 = Image.open(cImg4)
            time.sleep(0.05)
            cDummy4.close
        except (FileNotFoundError, AttributeError):
            return "error"

        cImg4Read = cv2.imread(cImg4)
        cImg4Gray = cv2.cvtColor(cImg4Read, cv2.COLOR_BGR2GRAY)
        contr4 = cImg4Gray.std()

        if contr4 < 30:
            contrastDict["picFourContrast"] = 2
        elif contr4 >= 30 and contr4 < 50:
            contrastDict["picFourContrast"] = 5.3
        elif contr4 >= 50 and contr4 < 150:
            contrastDict["picFourContrast"] = 3.3
        else:
            contrastDict["picFourContrast"] = 1.5

    def contrast5():
        cImg5 = fileDict["pic5"]

        try:
            cDummy5 = Image.open(cImg5)
            time.sleep(0.05)
            cDummy5.close
        except (FileNotFoundError, AttributeError):
            return "error"

        cImg5Read = cv2.imread(cImg5)
        cImg5Gray = cv2.cvtColor(cImg5Read, cv2.COLOR_BGR2GRAY)
        contr5 = cImg5Gray.std()

        if contr5 < 30:
            contrastDict["picFiveContrast"] = 2
        elif contr5 >= 30 and contr5 < 50:
            contrastDict["picFiveContrast"] = 5.3
        elif contr5 >= 50 and contr5 < 150:
            contrastDict["picFiveContrast"] = 3.3
        else:
            contrastDict["picFiveContrast"] = 1.5


class brightness:

    def brightness1():
        imgBright1 = fileDict["pic1"]

        try:
            bDummy1 = Image.open(imgBright1)
            time.sleep(0.05)
            bDummy1.close
        except (FileNotFoundError, AttributeError):
            return "error"

        imgBrightRead1 = cv2.imread(imgBright1)
        imgBrightHSV = cv2.cvtColor(imgBrightRead1, cv2.COLOR_BGR2HSV)
        imgBrightVal1 = imgBrightHSV[..., 2].mean()

        if imgBrightVal1 < 45:
            brightDict["picOneBrightness"] = -2.6
        elif imgBrightVal1 >= 45 and imgBrightVal1 < 53:
            brightDict["picOneBrightness"] = -1.8
        elif imgBrightVal1 >= 53 and imgBrightVal1 < 165:
            brightDict["picOneBrightness"] = 8.25
        else:
            brightDict["picOneBrightess"] = -4

    def brightness2():
        imgBright2 = fileDict["pic2"]

        try:
            bDummy2 = Image.open(imgBright2)
            time.sleep(0.05)
            bDummy2.close
        except (FileNotFoundError, AttributeError):
            return "error"

        imgBrightRead2 = cv2.imread(imgBright2)
        imgBrightHSV = cv2.cvtColor(imgBrightRead2, cv2.COLOR_BGR2HSV)
        imgBrightVal2 = imgBrightHSV[..., 2].mean()

        if imgBrightVal2 < 45:
            brightDict["picTwoBrightness"] = -2.6
        elif imgBrightVal2 >= 45 and imgBrightVal2 < 53:
            brightDict["picTwoBrightness"] = -1.8
        elif imgBrightVal2 >= 53 and imgBrightVal2 < 165:
            brightDict["picTwoBrightness"] = 8.25
        else:
            brightDict["picTwoBrightness"] = -4

    def brightness3():
        imgBright3 = fileDict["pic3"]

        try:
            bDummy3 = Image.open(imgBright3)
            time.sleep(0.05)
            bDummy3.close
        except (FileNotFoundError, AttributeError):
            return "error"

        imgBrightRead3 = cv2.imread(imgBright3)
        imgBrightHSV = cv2.cvtColor(imgBrightRead3, cv2.COLOR_BGR2HSV)
        imgBrightVal3 = imgBrightHSV[..., 2].mean()

        if imgBrightVal3 < 45:
            brightDict["picThreeBrightness"] = -2.6
        elif imgBrightVal3 >= 45 and imgBrightVal3 < 53:
            brightDict["picThreeBrightness"] = -1.8
        elif imgBrightVal3 >= 53 and imgBrightVal3 < 165:
            brightDict["picThreeBrightness"] = 8.25
        else:
            brightDict["picThreeBrightness"] = -4

    def brightness4():
        imgBright4 = fileDict["pic4"]

        try:
            bDummy4 = Image.open(imgBright4)
            time.sleep(0.05)
            bDummy4.close
        except (FileNotFoundError, AttributeError):
            return "error"

        imgBrightRead4 = cv2.imread(imgBright4)
        imgBrightHSV = cv2.cvtColor(imgBrightRead4, cv2.COLOR_BGR2HSV)
        imgBrightVal4 = imgBrightHSV[..., 2].mean()

        if imgBrightVal4 < 45:
            brightDict["picFourBrightness"] = -2.6
        elif imgBrightVal4 >= 45 and imgBrightVal4 < 53:
            brightDict["picFourBrightness"] = -1.8
        elif imgBrightVal4 >= 53 and imgBrightVal4 < 165:
            brightDict["picFourBrightness"] = 8.25
        else:
            brightDict["picFourBrightness"] = -4

    def brightness5():
        imgBright5 = fileDict["pic5"]

        try:
            bDummy5 = Image.open(imgBright5)
            time.sleep(0.05)
            bDummy5.close
        except (FileNotFoundError, AttributeError):
            return "error"

        imgBrightRead5 = cv2.imread(imgBright5)
        imgBrightHSV = cv2.cvtColor(imgBrightRead5, cv2.COLOR_BGR2HSV)
        imgBrightVal5 = imgBrightHSV[..., 2].mean()

        if imgBrightVal5 < 45:
            brightDict["picFiveBrightness"] = -2.6
        elif imgBrightVal5 >= 45 and imgBrightVal5 < 53:
            brightDict["picFiveBrightness"] = -1.8
        elif imgBrightVal5 >= 53 and imgBrightVal5 < 165:
            brightDict["picFiveBrightness"] = 8.25
        else:
            brightDict["picFiveBrightness"] = -4


class saturation:

    def saturation1():
        imgSat1 = fileDict["pic1"]

        try:
            sDummy1 = Image.open(imgSat1)
            time.sleep(0.05)
            sDummy1.close
        except (FileNotFoundError, AttributeError):
            return "error"

        imgSatRead1 = cv2.imread(imgSat1)
        imgSatHSV = cv2.cvtColor(imgSatRead1, cv2.COLOR_BGR2HSV)
        imgSatVal1 = imgSatHSV[..., 1].mean()

        if imgSatVal1 < 75:
            satDict["picOneSaturation"] = -2
        elif imgSatVal1 >= 75 and imgSatVal1 < 125:
            satDict["picOneSaturation"] = 6
        elif imgSatVal1 >= 125 and imgSatVal1 < 200:
            satDict["picOneSaturation"] = -0.5
        else:
            satDict["picOneSaturation"] = -4.7

    def saturation2():
        imgSat2 = fileDict["pic2"]

        try:
            sDummy2 = Image.open(imgSat2)
            time.sleep(0.05)
            sDummy2.close
        except (FileNotFoundError, AttributeError):
            return "error"

        imgSatRead2 = cv2.imread(imgSat2)
        imgSatHSV = cv2.cvtColor(imgSatRead2, cv2.COLOR_BGR2HSV)
        imgSatVal2 = imgSatHSV[..., 1].mean()

        if imgSatVal2 < 75:
            satDict["picTwoSaturation"] = -2
        elif imgSatVal2 >= 75 and imgSatVal2 < 125:
            satDict["picTwoSaturation"] = 6
        elif imgSatVal2 >= 125 and imgSatVal2 < 200:
            satDict["picTwoSaturation"] = -0.5
        else:
            satDict["picTwoSaturation"] = -4.7

    def saturation3():
        imgSat3 = fileDict["pic3"]

        try:
            sDummy3 = Image.open(imgSat3)
            time.sleep(0.05)
            sDummy3.close
        except (FileNotFoundError, AttributeError):
            return "error"

        imgSatRead3 = cv2.imread(imgSat3)
        imgSatHSV = cv2.cvtColor(imgSatRead3, cv2.COLOR_BGR2HSV)
        imgSatVal3 = imgSatHSV[..., 1].mean()

        if imgSatVal3 < 75:
            satDict["picThreeSaturation"] = -2
        elif imgSatVal3 >= 75 and imgSatVal3 < 125:
            satDict["picThreeSaturation"] = 6
        elif imgSatVal3 >= 125 and imgSatVal3 < 200:
            satDict["picThreeSaturation"] = -0.5
        else:
            satDict["picThreeSaturation"] = -4.7

    def saturation4():
        imgSat4 = fileDict["pic4"]

        try:
            sDummy4 = Image.open(imgSat4)
            time.sleep(0.05)
            sDummy4.close
        except (FileNotFoundError, AttributeError):
            return "error"

        imgSatRead4 = cv2.imread(imgSat4)
        imgSatHSV = cv2.cvtColor(imgSatRead4, cv2.COLOR_BGR2HSV)
        imgSatVal4 = imgSatHSV[..., 1].mean()

        if imgSatVal4 < 75:
            satDict["picFourSaturation"] = -2
        elif imgSatVal4 >= 75 and imgSatVal4 < 125:
            satDict["picFourSaturation"] = 6
        elif imgSatVal4 >= 125 and imgSatVal4 < 200:
            satDict["picFourSaturation"] = -0.5
        else:
            satDict["picFourSaturation"] = -4.7

    def saturation5():
        imgSat5 = fileDict["pic5"]

        try:
            sDummy5 = Image.open(imgSat5)
            time.sleep(0.05)
            sDummy5.close
        except (FileNotFoundError, AttributeError):
            return "error"

        imgSatRead5 = cv2.imread(imgSat5)
        imgSatHSV = cv2.cvtColor(imgSatRead5, cv2.COLOR_BGR2HSV)
        imgSatVal5 = imgSatHSV[..., 1].mean()

        if imgSatVal5 < 75:
            satDict["picFiveSaturation"] = -2
        elif imgSatVal5 >= 75 and imgSatVal5 < 125:
            satDict["picFiveSaturation"] = 6
        elif imgSatVal5 >= 125 and imgSatVal5 < 200:
            satDict["picFiveSaturation"] = -0.5
        else:
            satDict["picFiveSaturation"] = -4.7


class redEye:

    def redEye1():
        imgRed1 = fileDict["pic1"]

        try:
            rDummy1 = Image.open(imgRed1)
            time.sleep(0.05)
            rDummy1.close
        except (FileNotFoundError, AttributeError):
            return "error"

        if redEyeDict["pic1RedEye"] == 0:
            redEyeScoresDict["pic1RedEyeScore"] = 0
        elif redEyeDict["pic1RedEye"] == 1 or redEyeDict["pic1RedEye"] == 2:
            redEyeScoresDict["pic1RedEyeScore"] = -7.1
        else:
            redEyeScoresDict["pic1RedEyeScore"] = -8.8

    def redEye2():
        imgRed2 = fileDict["pic2"]

        try:
            rDummy2 = Image.open(imgRed2)
            time.sleep(0.05)
            rDummy2.close
        except (FileNotFoundError, AttributeError):
            return "error"

        if redEyeDict["pic2RedEye"] == 0:
            redEyeScoresDict["pic2RedEyeScore"] = 0
        elif redEyeDict["pic2RedEye"] == 1 or redEyeDict["pic2RedEye"] == 2:
            redEyeScoresDict["pic2RedEyeScore"] = -7.1
        else:
            redEyeScoresDict["pic2RedEyeScore"] = -8.8

    def redEye3():
        imgRed3 = fileDict["pic3"]

        try:
            rDummy3 = Image.open(imgRed3)
            time.sleep(0.05)
            rDummy3.close
        except (FileNotFoundError, AttributeError):
            return "error"

        if redEyeDict["pic3RedEye"] == 0:
            redEyeScoresDict["pic3RedEyeScore"] = 0
        elif redEyeDict["pic3RedEye"] == 1 or redEyeDict["pic3RedEye"] == 2:
            redEyeScoresDict["pic3RedEyeScore"] = -7.1
        else:
            redEyeScoresDict["pic3RedEyeScore"] = -8.8

    def redEye4():
        imgRed4 = fileDict["pic4"]

        try:
            rDummy4 = Image.open(imgRed4)
            time.sleep(0.05)
            rDummy4.close
        except (FileNotFoundError, AttributeError):
            return "error"

        if redEyeDict["pic4RedEye"] == 0:
            redEyeScoresDict["pic4RedEyeScore"] = 0
        elif redEyeDict["pic4RedEye"] == 1 or redEyeDict["pic4RedEye"] == 2:
            redEyeScoresDict["pic4RedEyeScore"] = -7.1
        else:
            redEyeScoresDict["pic4RedEyeScore"] = -8.8

    def redEye5():
        imgRed5 = fileDict["pic5"]

        try:
            rDummy5 = Image.open(imgRed5)
            time.sleep(0.05)
            rDummy5.close
        except (FileNotFoundError, AttributeError):
            return "error"

        if redEyeDict["pic5RedEye"] == 0:
            redEyeScoresDict["pic5RedEyeScore"] = 0
        elif redEyeDict["pic5RedEye"] == 1 or redEyeDict["pic5RedEye"] == 2:
            redEyeScoresDict["pic5RedEyeScore"] = -7.1
        else:
            redEyeScoresDict["pic5RedEyeScore"] = -8.8


def redEyeInit():
    redCounter = 0

    for picFile in fileDict.values():
        try:
            reDummy = Image.open(picFile)
            time.sleep(0.05)
            reDummy.close
        except (FileNotFoundError, AttributeError):
            continue

        redCounter = 0
        redDictPartParam = 0

        fileImg = cv2.imread(picFile)
        imgOut = fileImg.copy()

        haarEye = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
        eyeDetect = haarEye.detectMultiScale(fileImg, 1.05, 4)

        for x, y, w, h in eyeDetect:
            eyeCrop = fileImg[y:y + h, x:x + w]

            b, g, r = cv2.split(eyeCrop)
            bg = cv2.add(b, g)
            eyeMask = ((r > (bg - 20)) & (r > 80)).astype(np.uint8) * 255

            redCounter = redCounter + 1
            redEyeList.append(redCounter)

        redDictPartParam = redDictPartParam + 1
        redDictParam = "pic" + str(redDictPartParam) + "RedEye"
        redEyeDict[redDictParam] = redCounter


class faces:

    def face1():
        imgFace1 = fileDict["pic1"]

        try:
            fDummy1 = Image.open(imgFace1)
            time.sleep(0.05)
            fDummy1.close
        except (NameError, AttributeError):
            return "error"

        imgFaceRead1 = cv2.imread(imgFace1)
        imgFaceReadGray1 = cv2.cvtColor(imgFaceRead1, cv2.COLOR_BGR2GRAY)
        imgFaceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        faces1bef = imgFaceCascade.detectMultiScale(imgFaceReadGray1, scaleFactor=1.05, minNeighbors=4,
                                                    minSize=(35, 35))
        faces1 = len(faces1bef)

        if faces1 == 0:
            faceDict["picOneFaces"] = -10
        elif faces1 > 0:
            faceDict["picOneFaces"] = 0
        else:
            pass

    def face2():
        imgFace2 = fileDict["pic2"]

        try:
            fDummy2 = Image.open(imgFace2)
            time.sleep(0.05)
            fDummy2.close
        except (NameError, AttributeError):
            return "error"

        imgFaceRead2 = cv2.imread(imgFace2)
        imgFaceReadGray2 = cv2.cvtColor(imgFaceRead2, cv2.COLOR_BGR2GRAY)
        imgFaceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        faces2bef = imgFaceCascade.detectMultiScale(imgFaceReadGray2, scaleFactor=1.05, minNeighbors=4,
                                                    minSize=(35, 35))
        faces2 = len(faces2bef)

        if faces2 == 0:
            faceDict["picTwoFaces"] = -10
        elif faces2 > 0:
            faceDict["picTwoFaces"] = 0
        else:
            pass

    def face3():
        imgFace3 = fileDict["pic3"]

        try:
            fDummy3 = Image.open(imgFace3)
            time.sleep(0.05)
            fDummy3.close
        except (NameError, AttributeError):
            return "error"

        imgFaceRead3 = cv2.imread(imgFace3)
        imgFaceReadGray3 = cv2.cvtColor(imgFaceRead3, cv2.COLOR_BGR2GRAY)
        imgFaceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        faces3bef = imgFaceCascade.detectMultiScale(imgFaceReadGray3, scaleFactor=1.05, minNeighbors=4,
                                                    minSize=(35, 35))
        faces3 = len(faces3bef)

        if faces3 == 0:
            faceDict["picThreeFaces"] = -10
        elif faces3 > 0:
            faceDict["picThreeFaces"] = 0
        else:
            pass

    def face4():
        imgFace1 = fileDict["pic4"]

        try:
            fDummy4 = Image.open(imgFace4)
            time.sleep(0.05)
            fDummy4.close
        except (NameError, AttributeError):
            return "error"

        imgFaceRead4 = cv2.imread(imgFace4)
        imgFaceReadGray4 = cv2.cvtColor(imgFaceRead4, cv2.COLOR_BGR2GRAY)
        imgFaceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        faces4bef = imgFaceCascade.detectMultiScale(imgFaceReadGray4, scaleFactor=1.05, minNeighbors=4,
                                                    minSize=(35, 35))
        faces4 = len(faces4bef)

        if faces4 == 0:
            faceDict["picFourFaces"] = -10
        elif faces4 > 0:
            faceDict["picFourFaces"] = 0
        else:
            pass

    def face5():
        imgFace5 = fileDict["pic5"]

        try:
            fDummy5 = Image.open(imgFace5)
            time.sleep(0.05)
            fDummy5.close
        except (NameError, AttributeError):
            return "error"

        imgFaceRead5 = cv2.imread(imgFace5)
        imgFaceReadGray5 = cv2.cvtColor(imgFaceRead5, cv2.COLOR_BGR2GRAY)
        imgFaceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        faces5bef = imgFaceCascade.detectMultiScale(imgFaceReadGray5, scaleFactor=1.05, minNeighbors=4,
                                                    minSize=(35, 35))
        faces5 = len(faces5bef)

        if faces5 == 0:
            faceDict["picFiveFaces"] = -10
        elif faces5 > 0:
            faceDict["picFiveFaces"] = 0
        else:
            pass
