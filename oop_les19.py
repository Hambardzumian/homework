import json
import requests
import threading
class Head():
  def __init__(self):
    # Making dictionaries
    dict_jpg = {}
    dict_png = {}

    # Openning json file to read what is inside it and to get photo url s
    with open("oop19.json","r") as file:
      text = json.load(file)
    text = text["items"]

    # Adding jpg files to jpg dictionary, png files to png dictionary
    for i in text:
      if (".jpg" in i['url']) == True:
        dict_jpg[i['name']] = i['url']
      elif (".png" in i['url']) == True:
        dict_png[i['name']] = i['url']

    # Making self arguments
    self.dict_png = dict_png
    self.dict_jpg = dict_jpg
    self.text = text 

  # Method to start download process
  def Download(self):
    

    # Main openning method
    def pngs(name):

      # Downloading png files
      response = requests.get(self.dict_png[name])
      with open("{}.png".format(name),"wb") as file:
        file.write(response.content)
      print("{} is downloaded".format(name))     

    def jpgs(name):

      # Downloading jpg files
      response = requests.get(self.dict_jpg[name])
      with open("{}.jpg".format(name),"wb") as file:
        file.write(response.content)
      print("{} is downloaded".format(name))


    if __name__ == '__main__':
      for i in self.dict_png:
        x = threading.Thread(target=pngs,args=(i,))
        x.start()
      for i in self.dict_jpg:
        x = threading.Thread(target=jpgs,args=(i,))
        x.start()

# calling Main functions
main = Head()
main.Download()
