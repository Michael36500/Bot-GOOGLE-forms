import threading
import time
import function

def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))

Start = time.time()




#List of driver threads
driverThreads = []

# inputText = input("What do you want to generate with AI : ")
# inputText = "Space"
# inputText = ["city", "sunset", "sea", "forest", "airship", "port", "robot", "factory", "human", "fly", "waterfall", "tank", "giant robot", "steamtrain", "train"]
# inputText = ["city"]
# for a in inputText:

# inputText = "".join([x.capitalize() for x in inputText.split(" ")])
# iterations = int(input("Number of iterations : "))
iterations = 10 
iteration = 0
# print(iterations)

#Create directory
# if not os.path.exists(inputText):
#     os.mkdir(inputText)

for j in range(iterations):
    #Add thread to the list
    # driverThreads.append(threading.Thread(target=funuction.funukce()))
    driverThreads.append(threading.Thread(target=function.funukce, kwargs={'iteration':iteration}))

#Start all threads
for i in driverThreads:
    try:
        print("Starting Thread {}".format(iteration))
        # iteration = i._kwargs.get("iteration")+1
        iteration += 1
        i.start()
    except:
        pass
    time.sleep(1)

#Wait for the end of all threads
for i in driverThreads:
    i.join()

print(time.time() - Start)