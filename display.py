try:
    import Tkinter
except:
    import tkinter as Tkinter

import math
import time
import weatherPortion
import analogClock
#import clothingRecommendation



if __name__ == '__main__':
    root = analogClock.main()
    weatherRoot= weatherPortion.main()
    #clothRoot = clothingRecommendation.main()
    

while True:
    root.update()
    root.update_idletasks()
    root.updateClass()

        




