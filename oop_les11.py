# import random
# class HouseHealthing:
# 	def __init__(self,goal_temp_cold):
# 		self.goal_temp_cold = goal_temp_cold

# 	def __eq__(self,other):
# 		check = self.goal_temp_cold == other
# 		return check 


# Home1  = HouseHealthing(30)
# # b = Home1
# a = Home1 == 30

# print(a)		 


#######################################################################333






import os
import shutil

# print("this file is runing from",os.getcwd())

# print(os.listdir(F"{os.getcwd()}/.."))


base_dir = os.getcwd()

# os.makedirs(F"{base_dir}/..// nwe_python_folder/ nwe_python_folder/ nwe_python_folder")

# os.makedirs("/Users/USER/homework/new_python_folder")



print("we are now in {}".format(base_dir))
os.chdir("/Users/USER//Desktop/homework/nwe_python_folder")
# print("we are now in {}".format(os.getcwd()))
# print(os.listdir())
# while os.listdir():
# 	file = F"{os.getcwd()}/{os.listdir()[0]}"
# 	os.remove(file)
# print(os.listdir())	


# b = os.getcwd()
# a = os.chdir("..")

# os.rmdir(b)
path = F"{os.getcwd()}/python_directory"
shutil.rmtree(path)