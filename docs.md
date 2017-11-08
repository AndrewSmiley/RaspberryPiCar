#autonomous raspberry pi car
## Instructions 
1. open ssh connection to raspberry pi car using `ssh pi@192.168.1.1`
2. type `cd RaspberryPiCar/server`
3. Next, type `vim autonomous.py`, this will open the Python file that will drive the car along the course
4. The following variables effect the drive of the car: 
	5. 	`forward_time`: this dictates the amount of time (in seconds) that the car will travel forward before the first turn
	6. `turn_time`: this dictates the amount of time the car will turn in the first turn
	7. `turn_angle`: this is the angle at which the axle will turn the wheels
8. Change these variables to dictate the course the car will take 
9. Once your changes have been made, hit `ESC` followed by `:` and type `wq` followed by enter.
10. Now you will be back into the terminal, type `python autonomous.py` and hit enter. Place your car on the starting point and wait!