"""
Read this link must
https://www.geeksforgeeks.org/python-difference-between-lock-and-rlock-objects/
"""

# program to illustrate the use of RLocks 
  
# importing the module 
import threading 
  
# initializing the shared resource 
geek = 0
  
# creating an RLock object instead  
# of Lock object  
lock = threading.RLock() 
  
# the below thread is trying to access  
# the shared resource 
lock.acquire() 
geek = geek + 1
  
# the below thread is trying to access  
# the shared resource  
lock.acquire()  
geek = geek + 2
lock.release() 
lock.release() 
  
# displaying the value of shared resource 
print(geek)
