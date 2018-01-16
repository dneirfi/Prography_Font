from PIL import Image

CONST_W1=65
CONST_H1=92
CONST_W2=65
CONST_H2=92

img1= Image.open("myfontt1.jpg")
img2= Image.open("myfontt2.jpg")

img1=img1.resize((683,960))
img2=img2.resize((683,960))
#img1.show()
#img2.show()
ar=(16,19,670,940) #여백
img1=img1.crop(ar) #여백잘라낸 이미지
img2=img2.crop(ar)
img1.save('myfontt1_final.jpg')
img2.save('myfontt2_final.jpg')


for i in range (0,10):
    for j in range(0,10):
        area=(CONST_W1*j,CONST_H1*i,CONST_W1*j+CONST_W1,CONST_H1*i+CONST_H1) #박스 한칸
        im1=img1.crop(area)
        a=(5,20,60,90) #검정 테두리 없애기 위한 두번째 크롭
        im1=im1.crop(a)
        name='cropped_img'+str(i*10+j)
        im1.save(name+'.jpg')


for i in range (0,10):
    for j in range(0,10):
        area=(CONST_W1*j,CONST_H1*i,CONST_W1*j+CONST_W1,CONST_H1*i+CONST_H1)
        im2=img2.crop(area)
        a=(5,20,60,90)
        im2 = im2.crop(a)
        name='cropped_img'+str(i*10+100+j)
        im2.save(name+'.jpg')


