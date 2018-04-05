# [15-112 Fundamentals of Programming](http://www.kosbie.net/cmu/spring-16/15-112/)
A technical course and introduction to the fundamentals of programming with an emphasis on producing clear, robust, and reasonably efficient code using top-down design, informal analysis, and effective testing and debugging. Starting from first principles, it covers a large subset of the Python programming language, including its standard libraries and programming paradigms. It will also target numerous deployment scenarios, including standalone programs, shell scripts, and web-based applications.

## LED Controller - Final Project

My term project uses pySerial so my python code can communicate with the arduino. The LED lights are hooked up to the arduino, which runs on C++ code. By using serial, I can write to the arduino port, and C++ code uploaded to the arduino will read the values written to its port.

I used an Arduino Uno for this project. The port the serial code is writing to will have to be adjusted depending on the specific arduino used. If an arduino is not hooked up to the computer, the program will crash when it tries to write to the serial port. Thus the serial elements will have to be commented out to run the code.

The finished project can be seen [here](https://www.arianadaly.com/programming-1/2016/12/22/programming-term-project)
