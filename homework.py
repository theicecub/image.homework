import cv2 #open cv библиотека для работы с изображениями 
from PIL import Image

image_path = 'man.jpg'
image = cv2.imread(image_path)

if image is None:
    raise FileNotFoundError("Файл man не найден")

cv2.imshow('Face', image)
cv2.waitKey() #команда, которая ждет пока мы не нажмем на кнопку

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

if face_cascade.empty():
    raise FileNotFoundError("Файл haarcascade_frontalface_alt не найден")

face = face_cascade.detectMultiScale(gray_image)
print("Координаты лица:", face)

for(x, y, w, h) in face:
    cv2.rectangle(image, (x,y), (x+w, y+h), (0, 255, 0), 3)

cv2.imshow("Прямоугольник", image)
cv2.waitKey()


cat = Image.open(image_path)
glasses = Image.open('glasses.png')
cat = cat.convert('RGBA')
glasses = glasses.convert('RGBA')

for(x, y, w, h) in face:
    glasses_recised = glasses.resize((w, int(h/3)))
    cat.paste(glasses_recised, (x, y + int(h/4)), glasses_recised)

ouput_path="man_with_glasses.png"
cat.save(ouput_path)

result = cv2.imread("man_with_glasses.png")
cv2.imshow("Man with glasses", result)
cv2.waitKey()