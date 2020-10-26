import requests
import json
reponse = requests.get("https://xkcd.com/353/")
#the atribute of reponse object
print(dir(reponse))



######################################
dict_ = {
	"name":"Scarlett",
	"surename":"Johanson",
	"age":33
}
reponse = requests.post("https://httpbin.org/post", data = dict_)
print(reponse)
print(reponse.text)
######################################
# parameters = {"name":"python", "shool":"basic IT"}
# reponse = requests.get("https://httpbin.org/get?name=python&school=basic+IT")
# r = reponse.json()
# print(type(r))
# print(r["args"])
# print(r["args"]["name"])
# ########################################
# parameters = {"name":"python", "shool":"basic IT"}
# reponse = requests.get("https://httpbin.org/get", params = parameters)
# reponse = requests.get("https://httpbin.org/get?name=python&school=basic+IT")
# print(reponse.url)
# print(reponse.text)
########################################
# reponse = requests.get("https://imgs.xkcd.com/comics/python.png")
# reponse2 = requests.get("http://www.httpbin.org/image/jpeg")
# print(reponse.content)
# print(reponse.text)
# with open("new2_photo.png","wb") as file:
# 	file.write(reponse.content)

# with open("new3_photo.jpeg", "wb") as file:
# 	file.write(reponse2.content)		
#######################################
# print(F"this is a text document{reponse.content}")
#######################################
# print(F"this attribute is {reponse.text}")
########################################
# print(F"thw URL of the requests is {reponse.url}")
########################################
# print(F"the status code of requests is{reponse.status_code}")
#########################################
# print(help(reponse))
#########################################
# a = [reponse]
# print(a)
##########################################
# class requests():
# def __init__(self,status_code):
# 	self.status_code = status_code
# def __repr__(self):
# 	return self.status_code = status_code
##########################################