import requests
import random
class Photo_parser():
	def __init__(self):
		list_png = []
		list_jpg = []
		with open("test.txt","r") as file:
			for i in file:
				if (".png" in i) == True:
					i = i.replace("\n","")
					list_png.append(i)
				elif (".jpg" in i) == True:
					i = i.replace("\n","")
					list_jpg.append(i)
		self.list_png = list_png
		self.list_jpg = list_jpg
	def DownloadPng(self):
		for i in self.list_png:
			response = requests.get(i)
			with open("{}.png".format(random.randint(1,100)),"wb") as file:
				file.write(response.content)
	def DownloadJpg(self):
		for i in self.list_jpg:
			response = requests.get(i)
			with open("{}.jpg".format(random.randint(1,100)),"wb") as file:
				file.write(response.content)
start = Photo_parser()
start.DownloadPng()
start.DownloadJpg()
