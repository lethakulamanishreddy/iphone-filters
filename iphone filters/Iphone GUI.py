import cv2
import numpy as np
import math
from vcam import vcam,meshGen
import sys
from tkinter import *
root=Tk()

root.geometry('500x570')
root.resizable(width=False, height=False)
root.title('iPhone Filters')
root.config(background='light blue')
label = Label(root, text="iPhone Filters",bg='light blue',font=('helvetica 30 bold'))
label.pack(side=TOP)
statusbar=Label(root,width=50,text="A Project by Team SAHARA",font=("arial",13,"bold"),bg="black",fg="white",relief=SUNKEN)
statusbar.place(x=0,y=550)

def destroy():
   root.destroy()

def f1():
        cap = cv2.VideoCapture(0)
        ret, img = cap.read()
        H,W = img.shape[:2]
        fps = 30
        c1 = vcam(H=H,W=W)
        plane = meshGen(H,W)
        plane.Z += 20*np.exp(-0.5*((plane.X*1.0/plane.W)/0.1)**2)/(0.1*np.sqrt(2*np.pi))
        pts3d = plane.getPlane()
        pts2d = c1.project(pts3d)
        map_x,map_y = c1.getMaps(pts2d)
        ret, img = cap.read()
        while True:
                ret, img = cap.read()
                output = cv2.remap(img,map_x,map_y,interpolation=cv2.INTER_LINEAR,borderMode=0)
                output = cv2.flip(output,1)
                out1 = np.hstack((img,output))
                out1 = cv2.resize(out1,(700,350))
                cv2.imshow("Filter 1",out1)
                if cv2.waitKey(30)&0xFF == 27:
                        break
        cap.release()
        cv2.destroyAllWindows()
def f2():
        cap = cv2.VideoCapture(0)
        ret, img = cap.read()
        H,W = img.shape[:2]
        fps = 30
        c1 = vcam(H=H,W=W)
        plane = meshGen(H,W)
        plane.Z += 20*np.exp(-0.5*((plane.Y*1.0/plane.H)/0.1)**2)/(0.1*np.sqrt(2*np.pi))
        pts3d = plane.getPlane()
        pts2d = c1.project(pts3d)
        map_x,map_y = c1.getMaps(pts2d)
        ret, img = cap.read()
        while True:
                ret, img = cap.read()
                output = cv2.remap(img,map_x,map_y,interpolation=cv2.INTER_LINEAR,borderMode=0)
                output = cv2.flip(output,1)
                out1 = np.hstack((img,output))
                out1 = cv2.resize(out1,(700,350))
                cv2.imshow("Filter 2",out1)
                if cv2.waitKey(30)&0xFF == 27:
                        break
        cap.release()
        cv2.destroyAllWindows()
def f3():
        cap = cv2.VideoCapture(0)
        ret, img = cap.read()
        H,W = img.shape[:2]
        fps = 30
        c1 = vcam(H=H,W=W)
        plane = meshGen(H,W)
        plane.Z -= 10*np.exp(-0.5*((plane.X*1.0/plane.W)/0.1)**2)/(0.1*np.sqrt(2*np.pi))
        pts3d = plane.getPlane()
        pts2d = c1.project(pts3d)
        map_x,map_y = c1.getMaps(pts2d)
        ret, img = cap.read()
        while True:
                ret, img = cap.read()
                output = cv2.remap(img,map_x,map_y,interpolation=cv2.INTER_LINEAR,borderMode=0)
                output = cv2.flip(output,1)
                out1 = np.hstack((img,output))
                out1 = cv2.resize(out1,(700,350))
                cv2.imshow("Filter 3",out1)
                if cv2.waitKey(30)&0xFF == 27:
                        break
        cap.release()
        cv2.destroyAllWindows()
def f4():
        cap = cv2.VideoCapture(0)
        ret, img = cap.read()
        H,W = img.shape[:2]
        fps = 30
        c1 = vcam(H=H,W=W)        
        plane = meshGen(H,W)
        plane.Z -= 10*np.exp(-0.5*((plane.Y*1.0/plane.W)/0.1)**2)/(0.1*np.sqrt(2*np.pi))
        pts3d = plane.getPlane()
        pts2d = c1.project(pts3d)
        map_x,map_y = c1.getMaps(pts2d)
        ret, img = cap.read()
        while True:
                ret, img = cap.read()
                output = cv2.remap(img,map_x,map_y,interpolation=cv2.INTER_LINEAR,borderMode=0)
                output = cv2.flip(output,1)
                out1 = np.hstack((img,output))
                out1 = cv2.resize(out1,(700,350))
                cv2.imshow("Filter 4",out1)
                if cv2.waitKey(30)&0xFF == 27:
                        break
        cap.release()
        cv2.destroyAllWindows()
def f5():
        cap = cv2.VideoCapture(0)
        ret, img = cap.read()
        H,W = img.shape[:2]
        fps = 30
        c1 = vcam(H=H,W=W)
        plane = meshGen(H,W)
        plane.Z += 20*np.sin(2*np.pi*((plane.X-plane.W/4.0)/plane.W)) + 20*np.sin(2*np.pi*((plane.Y-plane.H/4.0)/plane.H))
        pts3d = plane.getPlane()
        pts2d = c1.project(pts3d)
        map_x,map_y = c1.getMaps(pts2d)
        ret, img = cap.read()
        while True:
                ret, img = cap.read()
                output = cv2.remap(img,map_x,map_y,interpolation=cv2.INTER_LINEAR,borderMode=0)
                output = cv2.flip(output,1)
                out1 = np.hstack((img,output))
                out1 = cv2.resize(out1,(700,350))
                cv2.imshow("Filter 5",out1)
                if cv2.waitKey(30)&0xFF == 27:
                        break
        cap.release()
        cv2.destroyAllWindows()
def f6():
        cap = cv2.VideoCapture(0)
        ret, img = cap.read()
        H,W = img.shape[:2]
        fps = 30
        c1 = vcam(H=H,W=W)
        plane = meshGen(H,W)
        plane.Z -= 20*np.sin(2*np.pi*((plane.X-plane.W/4.0)/plane.W)) - 20*np.sin(2*np.pi*((plane.Y-plane.H/4.0)/plane.H))
        pts3d = plane.getPlane()
        pts2d = c1.project(pts3d)
        map_x,map_y = c1.getMaps(pts2d)
        ret, img = cap.read()
        while True:
                ret, img = cap.read()
                output = cv2.remap(img,map_x,map_y,interpolation=cv2.INTER_LINEAR,borderMode=0)
                output = cv2.flip(output,1)
                out1 = np.hstack((img,output))
                out1 = cv2.resize(out1,(700,350))
                cv2.imshow("Filter 6",out1)
                if cv2.waitKey(30)&0xFF == 27:
                        break
        cap.release()
        cv2.destroyAllWindows()
def f7():
        cap = cv2.VideoCapture(0)
        ret, img = cap.read()
        H,W = img.shape[:2]
        fps = 30
        c1 = vcam(H=H,W=W)
        plane = meshGen(H,W)
        plane.Z -= 100*np.sqrt((plane.X*1.0/plane.W)**2+(plane.Y*1.0/plane.H)**2)
        pts3d = plane.getPlane()
        pts2d = c1.project(pts3d)
        map_x,map_y = c1.getMaps(pts2d)
        ret, img = cap.read()
        while True:
                ret, img = cap.read()
                output = cv2.remap(img,map_x,map_y,interpolation=cv2.INTER_LINEAR,borderMode=0)
                output = cv2.flip(output,1)
                out1 = np.hstack((img,output))
                out1 = cv2.resize(out1,(700,350))
                cv2.imshow("Filter 7",out1)
                if cv2.waitKey(30)&0xFF == 27:
                        break
        cap.release()
        cv2.destroyAllWindows()


b1=Button(root,padx=5,pady=5,width=12,bg='white',fg='black',relief=GROOVE,command=f1,text='Filter 1',font=('helvetica 15 bold'),activebackground='light green')
b1.pack()

b2=Button(root,padx=5,pady=5,width=12,bg='white',fg='black',relief=GROOVE,command=f2,text='Filter 2',font=('helvetica 15 bold'),activebackground='light green')
b2.pack()

b3=Button(root,padx=5,pady=5,width=12,bg='white',fg='black',relief=GROOVE,command=f3,text='Filter 3',font=('helvetica 15 bold'),activebackground='light green')
b3.pack()

b4=Button(root,padx=5,pady=5,width=12,bg='white',fg='black',relief=GROOVE,command=f4,text='Filter 4',font=('helvetica 15 bold'),activebackground='light green')
b4.pack()

b5=Button(root,padx=5,pady=5,width=12,bg='white',fg='black',relief=GROOVE,command=f5,text='Filter 5',font=('helvetica 15 bold'),activebackground='light green')
b5.pack()

b6=Button(root,padx=5,pady=5,width=12,bg='white',fg='black',relief=GROOVE,command=f6,text='Filter 6',font=('helvetica 15 bold'),activebackground='light green')
b6.pack()

b7=Button(root,padx=5,pady=5,width=12,bg='white',fg='black',relief=GROOVE,command=f7,text='Filter 7',font=('helvetica 15 bold'),activebackground='light green')
b7.pack()

b8=Button(root,padx=5,pady=5,width=12,bg='red',fg='black',relief=GROOVE,text='EXIT',command=destroy,font=('helvetica 15 bold'),activebackground='red')
b8.pack()

        
        


        
        
        
