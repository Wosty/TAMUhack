import cognitive_face as CF
import FaceQuickstart

# Stores data in class
class student:
    def __init__(self, faceScan, Name = "John Doe", Id = 42):
        self.name  = Name
        self.id    = Id
        self.faceData = faceScan

# Container for face data for student
#class faceData:
#    pass
    # Data for face to go here when
    # we know what to use