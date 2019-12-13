# import libraries
import cv2
import pafy


url = 'https://www.youtube.com/watch?v=rnN7CpPPVVw'

#CHANGE URL


vPafy = pafy.new(url)
play = vPafy.getbest()

def do_video_face_recognition():
    #start the video

    # Get a reference to webcam

    # Initialize variables
    face_locations = []

    cap = cv2.VideoCapture(play.url)

    while True:
        # Grab a single frame of video
        ret, frame = cap.read()

        #ret, frame = video_capture.read()


        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_frame = frame[:, :, ::-1]

        #detect_and_draw_faces(rgb_frame)

        # do face recognition here


        # Display the resulting image
        cv2.imshow('Video', frame)

        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    # Release handle to the webcam
    #video_capture.release()


    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    do_video_face_recognition()