import face_recognition
import cv2
import numpy as np
import requests, os, re

# video_capture = cv2.VideoCapture('rtsp://192.168.0.100:8080/h264_ulaw.sdp')
video_capture = cv2.VideoCapture('http://192.168.0.100:8080/video')

known_face_encodings = []
known_face_names = []
known_faces_filenames = []

# foysal_image = face_recognition.load_image_file("pictures/foysal.jpg")
# foysal_face_encoding = face_recognition.face_encodings(foysal_image)[0]


# zillur_image = face_recognition.load_image_file("pictures/zillur.jpg")
# zillur_face_encoding = face_recognition.face_encodings(zillur_image)[0]

# intisar_image = face_recognition.load_image_file("pictures/intisar.jpg")
# intisar_face_encoding = face_recognition.face_encodings(intisar_image)[0]

# known_face_encodings = [
#    foysal_face_encoding,
#    zillur_face_encoding,
#    intisar_face_encoding
# ]
# known_face_names = [
#   "Foysal",
#   "Zillur",
#    "Intisar"
# ]

for (dirpath, dirnames, filenames) in os.walk('pictures/'):
    known_faces_filenames.extend(filenames)
    break

for filename in known_faces_filenames:
    face = face_recognition.load_image_file('pictures/' + filename)
    known_face_names.append(re.sub("[0-9]", '', filename[:-4]))
    known_face_encodings.append(face_recognition.face_encodings(face)[0])

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    ret, frame = video_capture.read()

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]

    if process_this_frame:
        face_locations = face_recognition.face_locations(small_frame)
        face_encodings = face_recognition.face_encodings(small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
                
                json_to_export['name'] = name
                json_to_export['hour'] = f'{time.localtime().tm_hour}:{time.localtime().tm_min}'
                json_to_export['date'] = f'{time.localtime().tm_year}-{time.localtime().tm_mon}-{time.localtime().tm_mday}'
                json_to_export['picture_array'] = frame.tolist()

                # * ---------- SEND data to API --------- *


                r = requests.post(url='http://127.0.0.1:5000/receive_data', json=json_to_export)
                print("Status: ", r.status_code)

            face_names.append(name)

    process_this_frame = not process_this_frame

    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
