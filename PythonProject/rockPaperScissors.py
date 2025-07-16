import cv2
import random
import cvzone
from cvzone.HandTrackingModule import HandDetector
import time
print(dir(time))

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
detector = HandDetector(maxHands=1)

timer = 0
stateResult = False
stateGame   = False
score =[0,0] #[AI:Human]



while True:
    imgBG = cv2.imread("resources/emojis/BG.png")
    success, img = cap.read()

    imgScaled = cv2.resize(img, (0, 0), None,0.875, 0.875)
    imgScaled= imgScaled[:, 80:480]

    # Find Hands
    hands, img = detector.findHands(imgScaled)

    if stateGame:

        if stateResult is False :
            timer = time.time() - initialTime
            cv2.putText(imgBG,str(int(timer)),(605,435),cv2.FONT_HERSHEY_PLAIN,6,(255,0,255),4 )
            if timer > 3:
                stateResult = True
                timer = 0



                if hands:
                    playerMove=None
                    hand = hands[0]
                    fingers = detector.fingersUp(hand)
                    print(fingers)
                    if fingers ==[0,0,0,0,0]:# rock
                        playerMove =1
                    if fingers == [1, 1, 1, 1, 1]:#paper
                            playerMove = 2
                    if fingers == [0, 1, 1, 0, 0]:#scissor
                                playerMove = 3

                    randomNumber = random.randint(1, 3)

                    imgAI = cv2.imread(f'resources/emojis/{randomNumber}.png', cv2.IMREAD_UNCHANGED)
                    imgBG = cvzone.overlayPNG(imgBG, imgAI, (149, 310))
                    #player
                    if (playerMove == 1 and randomNumber == 3) or \
                            (playerMove == 2 and randomNumber == 1) or \
                            (playerMove == 3 and randomNumber == 2) :
                        score[1]+=1

                    # AI
                    if (playerMove == 3 and randomNumber == 1) or \
                            (playerMove == 1 and randomNumber == 2) or \
                            (playerMove == 2 and randomNumber == 3):
                        score[0] += 1


                        print(playerMove)





    imgBG[234:654,795:1195 ] = imgScaled
    if stateResult:
        imgBG = cvzone.overlayPNG(imgBG, imgAI, (149, 310))

    cv2.putText(imgBG, str(score[0]), (410, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 225, 255), 6)
    cv2.putText(imgBG, str(score[1]), (1112, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 225, 255), 6)

    # cv2.imshow("Image",img)
    cv2.imshow("resources/emojis/BG.png",imgBG )
    # cv2.imshow("scaled",imgScaled )
    key=  cv2.waitKey(1)
    if key == ord('s'):
        stateGame = True
        initialTime = time.time()
        stateResult = False



