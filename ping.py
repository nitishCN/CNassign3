import subprocess
import time
from threading import Timer


def timeout(end):
    end.kill()
p1 = subprocess.Popen(['ping',"192.168.2.2"], stdout=subprocess.PIPE)   # ping request to 192.168.2.2

my_timer = Timer(60, timeout, [p1])                                        #timer of 60sec

try:
    my_timer.start()
    output = p1.communicate()[0]
    print (output.decode('ascii'))
except:
    print("End")
start=time.time()

