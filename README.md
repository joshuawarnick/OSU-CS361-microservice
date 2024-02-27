# microservice

**Request Data** 

Data can be requested from the microservice by writing
the word and of these ["Grunt", "Flood", "Hunter", "Jackal", "Elite"]
alien names. In the test.py there is an example use with "Hunter"
being written to the pipe.txt file. The code for  
the interacting program will should follow this format
It should open and write a valid alien name to the
pipe.txt once ready to receive data. For example:

    file = open('pipe.txt', 'w')
    file.write('Hunter')
    file.close()

The code above will write the word 'Hunter' to
pipe.txt

**Receive Data**

Data is received two ways one is via the communication pipe,
once the microservice is signaled byt the presence of a valid
alien name. It will write back a message. In the test example
the message would be "hunter.jpg"
sencondly it opens an image file of the type of alien 
in a new window.
To access the name of the image file.
These commands could be run

    file = open('signal.txt', 'r')
    word = file.readline()
    file.close()


**UML Diagram**

![Microservice UML](https://github.com/joshuawarnick/OSU-CS361-microservice/assets/86386882/d531f581-f8f1-4fe6-bd90-42d9511d181f)


**Execution**

To see the microservice in action, navigate to the directory where the microservice is:
  1. open main.py in a terminal and enter "python main.py"
  2. open test.py in a new terminal and enter "python test.py"
after this executes you will see a "hunter.jpg" written to the pipe.txt
and the image file opened in a new window 
