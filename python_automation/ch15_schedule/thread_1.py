import threading

thread1 = threading.Thread(target=print, args = ["Hello world !", "What is your name? ", "Do you play basketball?"], kwargs = {"sep":" & "})

thread1.start()
