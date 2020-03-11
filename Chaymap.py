import pyautogui
import os
import time
def chaymap():
	path = os.getcwd() + "\\Data\\NgoaLong\\Map"
	Thu_gon=list()
	Thu_gon.append(path+"\\ThuGon.png")
	Thu_gon.append(path+"\\ThuGon1.png")
	Thu_gon.append(path+"\\ThuGon2.png")
	Map=path+"\\MuiTen.png"
	temp=0
	TanCong=path+"\\TanCong.png"
	Ketqua=path+"\\Ketqua.png"
	QuaMap=path+"\\QuaMap.png"
	for i in Thu_gon:
		Xoa=pyautogui.locateCenterOnScreen(i,confidence=0.85)	
		pyautogui.click(Xoa)
		time.sleep(0.2)
	while temp!=5:
		temp+=1
		Next=pyautogui.locateCenterOnScreen(QuaMap,confidence=0.75)
		while Next!=None:
			pyautogui.click(Next)
			time.sleep(0.5)
			Next=pyautogui.locateCenterOnScreen(QuaMap,confidence=0.75)
		temp1=0
		while temp1!=5:
			temp1+=1
			locate_map=pyautogui.locateCenterOnScreen(Map,confidence=0.6)
		if (locate_map==None):
			break
		x,y=locate_map
		y=y+100
		pyautogui.click(x,y)
		time.sleep(0.2)

		auto_tancong=(1060,460)
		pyautogui.click(auto_tancong)
		time.sleep(0.2)

		locate_Ketqua=None
		while locate_Ketqua==None :
			locate_Ketqua=pyautogui.locateCenterOnScreen(Ketqua,confidence=0.8)
		pyautogui.click(locate_Ketqua)
		time.sleep(0.2)
		pyautogui.press("esc")
		time.sleep(0.2)
chaymap()