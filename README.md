# [15-112 Fundamentals of Programming](http://www.kosbie.net/cmu/spring-16/15-112/)

## LED Controller

My term project uses pySerial so my python code can communicate with the arduino. The LED lights are hooked up to the arduino, which runs on C++ code. By using serial, I can write to the arduino port, and C++ code uploaded to the arduino will read the values written to its port.

I'm using an Arduino Uno. The port the serial code is writing to will have to be adjusted depending on the specific arduino used. If an arduino is not hooked up to the computer, the program will crash when it tries to write to the serial port. Thus the serial elements will have to be commented out to run the code.