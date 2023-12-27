from plyer import notification
import plyer
import time


screenTimeSeconds = 18000 # = 5 hours

if __name__ == '__main__':
    def timer():
        global screenTimeSeconds
        while True:
            if screenTimeSeconds <= 0:
                break
            screenTimeSeconds -= 1
            time.sleep(1)

        while True:
            plyer.notification.notify(title = '    Time for a rest   ',
                                message = 'Rest is vital for your better mental health, increased concentration and memory, a healthier immune system, reduced stress and much more.',
                                timeout = 5)
            time.sleep(10)

    timer()

        
