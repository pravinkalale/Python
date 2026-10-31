class Grand_parent:                      # grand class 
    def talk(self):
        print("grand parents talk")
        
class parent(Grand_parent):
    def ride(self):
        print("bike riding")
        
class child(parent):
    def drive(self):
        print("car driving")
d = child()
d.ride()
d.talk()
d.drive()