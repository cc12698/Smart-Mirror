import weatherPortion
import analogClock

if __name__ == '__main__':
    root = analogClock.main()
    clockRoot= weatherPortion.main()

while True:
    root.update()
    root.update_idletasks()
    root.updateClass()

        


