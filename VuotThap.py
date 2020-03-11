import pyautogui
import os
import threading
import time
def Xacdinhvitri():
	locate=os.getcwd()+"\\Data\\NgoaLong\\Thap\\"
	locate_thap=locate+"Thap.png"
	locate_button_thap=locate+"ButtonThap.png"
	locate_tang=locate+"Tang.png"
	locate_button_next=locate+"Next.png"
	locate_button_xacnhan=locate+"XacNhan.png"
	locate_Boss=locate+"Boss.png"
	locate_Out=locate+"Out.png"
	#Vao Thap Thi Luyen
	# Vaothap=None
	# while Vaothap==None:
	# 	Vaothap=pyautogui.locateCenterOnScreen(locate_thap, confidence=0.5)
	# pyautogui.click(Vaothap)
	# time.sleep(1)
	#bam nut
	# Button_vaothap=None
	# while Button_vaothap==None:
	# 	Button_vaothap=pyautogui.locateCenterOnScreen(locate_button_thap,confidence=0.95)
	# pyautogui.click(Button_vaothap)
	# time.sleep(1)

	#Lap lai
	repeat=0
	TimeScale=0.1
	while repeat<=20:
		#Qua Tang
		time.sleep(TimeScale)
		Button_next=pyautogui.locateCenterOnScreen(locate_button_next,confidence=0.8)
		pyautogui.click(Button_next)
		time.sleep(TimeScale)

		#Tim tang thi luyen
		Tang=pyautogui.locateAllOnScreen(locate_tang,confidence=0.9)
		if (Tang!=None):
			maxtang=None
			for i in Tang:
				maxtang=i
		pyautogui.click(maxtang)
		#Bam nut vuot thap
		Button_VuotThap=(799,660)
		pyautogui.click(Button_VuotThap)
		time.sleep(TimeScale)
		#XacNhan

		Button_XacNhan=pyautogui.locateCenterOnScreen(locate_button_xacnhan,confidence=0.75)
		pyautogui.click(Button_XacNhan)
		time.sleep(TimeScale+0.4)

		#click_Boss
		Boss=None
		temp=0
		while Boss==None:
			temp+=1
			Boss=pyautogui.locateCenterOnScreen(locate_Boss,confidence=0.9)
			time.sleep(TimeScale)
			if (temp==10):
				print ('Break')
				break
			
		pyautogui.click(Boss)

		#Cho chay
		Out=None
		while Out==None:
			Out=pyautogui.locateCenterOnScreen(locate_Out,confidence=0.85)
		pyautogui.click(Out)
Xacdinhvitri()