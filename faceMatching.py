from studentClass import *
from FaceQuickstart import faces

# TODO: Create way to initialize students with custom variables in the front-end 
# Hard-coded student classes
gabi    = student(faces, "Gabi Norsworthy", 11)
landon  = student(faces, "Landon Creel", 12)
wesley  = student(faces, "Wesley Till", 13)
shikhar = student(faces, "Shikhar Baheti", 14)

studentList = [gabi, landon, wesley, shikhar]

print(studentList[0].faceData)