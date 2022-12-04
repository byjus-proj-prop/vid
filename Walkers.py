import cv2


# Crie nosso classificador de corpos
people_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

# Inicie a captura de vídeo para o arquivo de vídeo
cap = cv2.VideoCapture('walking.avi')

# Faça o loop assim que o vídeo for carregado com sucesso
while True:
    
    # Leia o primeiro quadro
    ret, frame = cap.read()

    gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    people = people_cascade.detectMultiScale(gray, 1.1, 5)
    
    for (x,y,w,h) in people:
       cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    # Exiba o quadro resultante
    cv2.imshow("cam", frame)
    
    # Saia da tela ao pressionar a barra de espaço
    if cv2.waitKey(25) == 32:
        break

cap.release()
cv2.destroyAllWindows()
