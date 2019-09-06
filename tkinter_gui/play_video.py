import cv2
import sys
import os
import signal


currentVideoPath = sys.stdin.readline()
capture = cv2.VideoCapture(currentVideoPath)
# capture = cv2.VideoCapture('/Volumes/data/DeepLabCut/Videos/BW/DLC/Video6.mp4')
fps = 25
frame_count = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
width = int(capture.get(3))
height = int(capture.get(4))
f = open(str(os.path.split(os.path.dirname(os.path.dirname(os.getcwd())))[-2]) + '/labelling_info.txt', 'w')

def printOnFrame(currentFrame):
    currentTime = currentFrame / 25
    cv2.putText(frame, 'F~ ' + str(currentFrame), (10, (height - 20)), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 2)
    cv2.putText(frame, 'T~ ' + str(currentTime), (10, (height - 80)), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 2)

while True:
    ret, frame = capture.read()
    key = cv2.waitKey(1) & 0xff
    if key == ord('p'):
        while True:
            key2 = cv2.waitKey(1) or 0xff
            ### THE VIDEO IS PAUSED
            currDisplayFrameNo = int(capture.get(cv2.CAP_PROP_POS_FRAMES))
            f.seek(0)
            f.write(str(currDisplayFrameNo-1))
            f.truncate()
            f.flush()
            os.fsync(f.fileno())
            ### BACK UP TWO FRAME
            if key2 == ord('t'):
                capture.set(cv2.CAP_PROP_POS_FRAMES, (currDisplayFrameNo - 2))
                ret, frame = capture.read()
                currentFrame = int(capture.get(cv2.CAP_PROP_POS_FRAMES))
                printOnFrame(currentFrame)
                cv2.imshow('Video', frame)
                f.seek(0)
                f.write(str(currentFrame))
                f.truncate()
                f.flush()
                os.fsync(f.fileno())
            ### BACK UP TEN FRAME
            if key2 == ord('s'):
                capture.set(cv2.CAP_PROP_POS_FRAMES, (currDisplayFrameNo - 11))
                ret, frame = capture.read()
                currentFrame = int(capture.get(cv2.CAP_PROP_POS_FRAMES))
                printOnFrame(currentFrame)
                cv2.imshow('Video', frame)
                f.seek(0)
                f.write(str(currentFrame))
                f.truncate()
                f.flush()
                os.fsync(f.fileno())
            ### BACK UP 1s
            if key2 == ord('x'):
                capture.set(cv2.CAP_PROP_POS_FRAMES, (currDisplayFrameNo-fps))
                ret, frame = capture.read()
                currentFrame = int(capture.get(cv2.CAP_PROP_POS_FRAMES))
                printOnFrame(currentFrame)
                cv2.imshow('Video', frame)
                f.seek(0)
                f.write(str(currentFrame))
                f.truncate()
                f.flush()
                os.fsync(f.fileno())
            ### FORWARD 1s
            if key2 == ord('w'):
                capture.set(cv2.CAP_PROP_POS_FRAMES, (currDisplayFrameNo+fps))
                ret, frame = capture.read()
                currentFrame = int(capture.get(cv2.CAP_PROP_POS_FRAMES))
                printOnFrame(currentFrame)
                cv2.imshow('Video', frame)
                f.seek(0)
                f.write(str(currentFrame))
                f.truncate()
                f.flush()
                os.fsync(f.fileno())
            ### FORWARD TWO FRAMES
            if key2 == ord('o'):
                capture.set(cv2.CAP_PROP_POS_FRAMES, (currDisplayFrameNo + 1))
                ret, frame = capture.read()
                currentFrame = int(capture.get(cv2.CAP_PROP_POS_FRAMES))
                printOnFrame(currentFrame)
                cv2.imshow('Video', frame)
                f.seek(0)
                f.write(str(currentFrame))
                f.truncate()
                f.flush()
                os.fsync(f.fileno())
            ### FORWARD TEN FRAMES
            if key2 == ord('e'):
                capture.set(cv2.CAP_PROP_POS_FRAMES, (currDisplayFrameNo + 9))
                ret, frame = capture.read()
                currentFrame = int(capture.get(cv2.CAP_PROP_POS_FRAMES))
                printOnFrame(currentFrame)
                cv2.imshow('Video', frame)
                f.seek(0)
                f.write(str(currentFrame))
                f.truncate()
                f.flush()
                os.fsync(f.fileno())
            if key2 == ord('p'):
                break
            if key2 == ord('q'):
                capture.release()
                cv2.destroyAllWindows()
                path = (str(os.path.split(os.path.dirname(os.path.dirname(os.getcwd())))[-2]) + r"/subprocess.txt")
                txtFile = open(path)
                line = txtFile.readline()
                os.kill(int(line), signal.SIGTERM)
                break
            if cv2.getWindowProperty('Video', 1) == -1:
                capture.release()
                cv2.destroyAllWindows()
                path = (str(os.path.split(os.path.dirname(os.path.dirname(os.getcwd())))[-2]) + r"/subprocess.txt")
                txtFile = open(path)
                line = txtFile.readline()
                os.kill(int(line), signal.SIGTERM)
    currentFrame = int(capture.get(cv2.CAP_PROP_POS_FRAMES))
    printOnFrame(currentFrame)
    cv2.namedWindow('Video', cv2.WINDOW_NORMAL)
    cv2.imshow('Video', frame)
    if key == ord('q'):
        break
    if cv2.getWindowProperty('Video', 1) == -1:
        break
capture.release()
f.close()
cv2.destroyAllWindows()
path = (str(os.path.split(os.path.dirname(os.path.dirname(os.getcwd())))[-2]) + r"/subprocess.txt")
txtFile = open(path)
line = txtFile.readline()
os.kill(int(line), signal.SIGTERM)










