import threading
import pickle

class BackgroundThread(threading.Thread):
    def __init__(self,marklist):
        threading.Thread.__init__(self)
        self.__marks=marklist

    def run(self):
        with open("marks.pkl","wb") as file:
            pickle.dump(self.__marks,file)