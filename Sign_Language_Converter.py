import cv2
import mediapipe as mp
import time
from math import sqrt
import pyttsx3
from tkinter import *
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

pictures = 1
paused = False
draw = 0
hel = 0
okhelp = 1
voice = 1


class HandDetector:
    def __init__(self):
        self.mphands = mp.solutions.mediapipe.solutions.hands
        self.hands = self.mphands.Hands()
        self.mpdraw = mp.solutions.mediapipe.solutions.drawing_utils

    def detect_hands(self, frame):
        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(frameRGB)
        return results.multi_hand_landmarks

    def draw_landmarks(self, frame, hand_landmarks):
        self.mpdraw.draw_landmarks(frame, hand_landmarks, self.mphands.HAND_CONNECTIONS,
                                   landmark_drawing_spec=self.mpdraw.DrawingSpec(
                                       (0, 0, 255), 4, 4),
                                   connection_drawing_spec=self.mpdraw.DrawingSpec((0, 255, 0), 2, 1))


def distance(x1, y1, x2, y2):
    return sqrt((x2-x1)**2+(y2-y1)**2)


def calculate_centroid(x1, y1, x2, y2, x3, y3):
    Cx = (x1 + x2 + x3) / 3
    Cy = (y1 + y2 + y3) / 3
    return Cx, Cy


def openfile():
    file = askopenfile(mode="r", filetypes=[
                       ('Video Files', ['*.mp4', '*.mov'])])
    if file is not None:
        global filename
        filename = file.name
        global cap
        cap = cv2.VideoCapture(filename)
        global pictures
        pictures = 0
        global okhelp
        okhelp = 0


def P():
    global paused
    paused = True


def R():
    global paused
    paused = False


def live():
    global cap
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 3000)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 3000)
    global pictures
    pictures = 1
    global paused
    paused = False
    global okhelp
    okhelp = 1


def dra():
    global draw
    draw = 1


def Rem():
    global draw
    draw = 0


def needhel():
    live()
    if okhelp:
        global hel
        hel = 1


def remhel():
    if okhelp:
        global hel
        hel = 0


def needvoice():
    global voice
    voice = 1


def remvoice():
    global voice
    voice = 0


# *********************************************************************************************
root = Tk()
root.title("Sign Language Converter")
root.config(bg="grey")
root.geometry("700x640")
label = Label(root)
label.pack()
f1 = LabelFrame(root)
f1.pack()
L1 = Label(f1)
L1.pack()

b1 = Button(root, text='Recorded Videos', height=3,
            width=17, command=lambda: openfile())
b1.place(x=10, y=300)

b2 = Button(root, text='Live', height=3, width=17, command=lambda: live())
b2.place(x=10, y=450)

b3 = Button(root, text='Draw Landmarks', height=3,
            width=17, command=lambda: dra())
b3.place(x=10, y=50)

b4 = Button(root, text='Remove Landmarks', height=3,
            width=17, command=lambda: Rem())
b4.place(x=10, y=100)

b5 = Button(root, text='Pause', height=3, width=17, command=lambda: P())
b5.place(x=1455, y=300)

b6 = Button(root, text='Resume', height=3, width=17, command=lambda: R())
b6.place(x=1455, y=450)

b7 = Button(root, text='Help Live', height=3,
            width=17, command=lambda: needhel())
b7.place(x=1455, y=50)

b8 = Button(root, text='Remove Help', height=3,
            width=17, command=lambda: remhel())
b8.place(x=1455, y=100)

b9 = Button(root, text='Voice', height=3,
            width=17, command=lambda: needvoice())
b9.place(x=10, y=600)

b10 = Button(root, text='Silent', height=3,
             width=17, command=lambda: remvoice())
b10.place(x=1455, y=600)


img = cv2.imread("img1.jpg")
r, c, _ = img.shape

img2 = cv2.imread("img2.jpg")
r2, c2, _ = img2.shape

img3 = cv2.imread("img3.jpg")
r3, c3, _ = img3.shape

img4 = cv2.imread("img4.jpg")
r4, c4, _ = img4.shape

img5 = cv2.imread("img5.jpg")
r5, c5, _ = img5.shape

img6 = cv2.imread("img6.jpg")
r6, c6, _ = img6.shape

img7 = cv2.imread("img7.jpg")
r7, c7, _ = img7.shape

img8 = cv2.imread("img8.jpg")
r8, c8, _ = img8.shape

img9 = cv2.imread("img9.jpg")
r9, c9, _ = img9.shape

img10 = cv2.imread("img10.jpg")
r10, c10, _ = img10.shape

# *********************************************************************************************

engine = pyttsx3.init()
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 3000)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 3000)

hand_detector = HandDetector()

ctime = 0
ptime = 0

speaking = ""

while True:
    if not paused:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)

    if pictures == 1 and hel == 1:
        frame[0:r, 0:c] = img
        frame[r:r+r2, 0:c] = img2
        frame[r+r2:r+r2+r3, 0:c] = img3
        frame[r+r2+r3:r+r2+r3+r4, 0:c] = img4
        frame[r+r2+r3+r4:r+r2+r3+r4+r5, 0:c] = img5

        frame[0:r, 1280-c6: 1280] = img6
        frame[r:r+r2, 1280-c6: 1280] = img7
        frame[r+r2:r+r2+r3, 1280-c6: 1280] = img8
        frame[r+r2+r3:r+r2+r3+r4, 1280-c6: 1280] = img9
        frame[r+r2+r3+r4:r+r2+r3+r4+r5, 1280-c6: 1280] = img10

    count = 0
    x_cor = []
    y_cor = []
    play = 0
    sentence = "Unknown"
    hand_landmarks = hand_detector.detect_hands(frame)
    if hand_landmarks:
        for hand in hand_landmarks:
            point = []
            for i in range(21):
                mark = hand.landmark[i]
                height, width, channels = frame.shape
                px, py = int(mark.x*width), int(mark.y*height)
                # print(i, "=", px, py)
                point.append((px, py))
                x_cor.append(px)
                y_cor.append(py)
            x1 = int(min(x_cor)-30)
            y1 = int(min(y_cor)-30)
            x2 = int(max(x_cor)+30)
            y2 = int(max(y_cor)+30)

            d1, d2 = calculate_centroid(
                x_cor[5], y_cor[5], x_cor[0], y_cor[0], x_cor[17], y_cor[17])

            if draw:
                hand_detector.draw_landmarks(frame, hand)
                cv2.circle(frame, (int(d1), int(d2)), 5, (0, 0, 255), -1)
                cv2.line(frame, (x_cor[5], y_cor[5]),
                         (int(d1), int(d2)), (0, 255, 0), 2)
                cv2.line(frame, (x_cor[0], y_cor[0]),
                         (int(d1), int(d2)), (0, 255, 0), 2)
                cv2.line(frame, (x_cor[17], y_cor[17]),
                         (int(d1), int(d2)), (0, 255, 0), 2)

            if y_cor[8] < y_cor[5] and y_cor[12] < y_cor[9] and y_cor[16] > y_cor[13] and y_cor[20] > y_cor[17] and x_cor[4] > x_cor[5]:
                sentence = "Victory"
                play = 1
                if pictures == 1 and hel == 1:
                    cv2.rectangle(frame, (0, r+r2),
                                  (180, r+r2+r3), (0, 0, 255), 5)

            if distance(point[0][0], point[0][1], point[8][0], point[8][1]) < distance(point[0][0], point[0][1], point[6][0], point[6][1]) and distance(point[0][0], point[0][1], point[12][0], point[12][1]) < distance(point[0][0], point[0][1], point[10][0], point[10][1]) and distance(point[0][0], point[0][1], point[16][0], point[16][1]) < distance(point[0][0], point[0][1], point[14][0], point[14][1]) and distance(point[0][0], point[0][1], point[20][0], point[20][1]) < distance(point[0][0], point[0][1], point[18][0], point[18][1]) and distance(point[2][0], point[2][1], point[8][0], point[8][1]) < distance(point[4][0], point[4][1], point[5][0], point[5][1]) and distance(point[0][0], point[0][1], point[20][0], point[20][1]) < distance(point[0][0], point[0][1], point[1][0], point[1][1]):
                sentence = "All the best"
                play = 1
                if pictures == 1 and hel == 1:
                    cv2.rectangle(frame, (0, 0), (180, r), (0, 0, 255), 5)

            if y_cor[8] < y_cor[5] and y_cor[20] < y_cor[17] and y_cor[12] > y_cor[9] and y_cor[16] > y_cor[13] and x_cor[4] < x_cor[5]:
                sentence = "I hate You"
                play = 1
                if pictures == 1 and hel == 1:
                    cv2.rectangle(frame, (0, r+r2+r3+r4),
                                  (180, r+r2+r3+r4+r5), (0, 0, 255), 5)

            if y_cor[12] < y_cor[9] and y_cor[16] < y_cor[13] and y_cor[20] < y_cor[17] and y_cor[8] > y_cor[5] and x_cor[8] < x_cor[5] and x_cor[4] < x_cor[2]:
                sentence = "Ok hand Sign"
                play = 1
                if pictures == 1 and hel == 1:
                    cv2.rectangle(frame, (0, r), (180, r+r2), (0, 0, 255), 5)

            if y_cor[12] > y_cor[9] and y_cor[16] > y_cor[13] and y_cor[20] > y_cor[17] and y_cor[8] < y_cor[5] and x_cor[4] > x_cor[9]:
                sentence = "Lumber one team"
                play = 1
                if pictures == 1 and hel == 1:
                    cv2.rectangle(frame, (1280-c6, 0),
                                  (1280, r6), (0, 0, 255), 5)

            if distance(point[4][0], point[4][1], point[8][0], point[8][1]) < distance(point[4][0], point[4][1], point[6][0], point[6][1]) and distance(point[4][0], point[4][1], point[12][0], point[12][1]) < distance(point[4][0], point[4][1], point[10][0], point[10][1]) and distance(point[4][0], point[4][1], point[16][0], point[16][1]) < distance(point[4][0], point[4][1], point[14][0], point[14][1]) and distance(point[4][0], point[4][1], point[20][0], point[20][1]) < distance(point[4][0], point[4][1], point[18][0], point[18][1]) and distance(point[0][0], point[0][1], point[8][0], point[8][1]) > distance(point[0][0], point[0][1], point[6][0], point[6][1]) and distance(point[0][0], point[0][1], point[12][0], point[12][1]) > distance(point[0][0], point[0][1], point[10][0], point[10][1]) and distance(point[0][0], point[0][1], point[16][0], point[16][1]) > distance(point[0][0], point[0][1], point[14][0], point[14][1]) and distance(point[0][0], point[0][1], point[20][0], point[20][1]) > distance(point[0][0], point[0][1], point[18][0], point[18][1]):
                sentence = "Call the Doctor"
                play = 1
                if pictures == 1 and hel == 1:
                    cv2.rectangle(frame, (0, r+r2+r3),
                                  (180, r+r2+r3+r4), (0, 0, 255), 5)

            if y_cor[8] > y_cor[5] and y_cor[12] > y_cor[9] and y_cor[16] > y_cor[13] and x_cor[4] < x_cor[2] and x_cor[20] > x_cor[17]:
                sentence = "Thank You"
                play = 1
                if pictures == 1 and hel == 1:
                    cv2.rectangle(frame, (1280-c6, 0+r6),
                                  (1280, r6+r7), (0, 0, 255), 5)

            if y_cor[8] < y_cor[5] and y_cor[12] < y_cor[9] and y_cor[16] > y_cor[13] and y_cor[20] < y_cor[17] and x_cor[4] > x_cor[9]:
                sentence = "Good bye"
                play = 1
                if pictures == 1 and hel == 1:
                    cv2.rectangle(frame, (1280-c6, 0+r6+r7),
                                  (1280, r6+r7+r8), (0, 0, 255), 5)

            if y_cor[8] < y_cor[5] and y_cor[12] < y_cor[9] and y_cor[16] > y_cor[13] and y_cor[20] > y_cor[17] and x_cor[4] < x_cor[2]:
                sentence = "3 in Alternate"
                play = 1
                if pictures == 1 and hel == 1:
                    cv2.rectangle(frame, (1280-c6, 0+r6+r7+r8),
                                  (1280, r6+r7+r8+r9), (0, 0, 255), 5)

            if y_cor[8] < y_cor[5] and y_cor[12] > y_cor[9] and y_cor[16] > y_cor[13] and y_cor[20] < y_cor[17] and x_cor[4] > x_cor[5]:
                sentence = "Rock Hand Sign"
                play = 1
                if pictures == 1 and hel == 1:
                    cv2.rectangle(frame, (1280-c6, 0+r6+r7+r8+r9),
                                  (1280, r6+r7+r8+r9+r10), (0, 0, 255), 5)

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 5)

    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime = ctime

    if not paused:
        cv2.putText(frame, f"FPS: {int(fps)}", (200, 50),
                    cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 255), 3)
        cv2.putText(frame, f"Sign: {sentence}", (200, 125),
                    cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 255), 3)

    # cv2.imshow("Video", frame)

    imgk = ImageTk.PhotoImage(Image.fromarray(frame))
    L1["image"] = imgk

    root.update()

    k = cv2.waitKey(1)
    if k == 27:
        break

    if play and voice:
        if sentence != speaking:
            engine.say(sentence)
            engine.runAndWait()
            speaking = sentence

    if play == 0 and sentence == "Unknown":
        speaking = ""


cap.release()
cv2.destroyAllWindows()
