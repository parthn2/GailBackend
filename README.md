# GailBackend

This application is being used by a web application and android application for a Gail Project which is currently in progress in IIT Kharagpur. This application is hosted over local network of IIT Kgp using gunicorn & nginx and can be accesed from 10.29.8.37

###Documentation

###API: 

###    http://10.29.8.37/admin/
/admin/ endpoint is for managing the data stored in database

###    http://10.29.8.37/motors/
/motors/ endpoint is viewing all the motors with the current and voltage values stored in it

###    http://10.29.8.37/motors/<int:motor_id>/
/motors/<int:motor_id>/ endpoint is for viewing the current and voltage values for the motor id : <int:motor_id>

###    Database Diagram
<img width="340" alt="Screenshot 2023-04-15 at 9 33 59 AM" src="https://user-images.githubusercontent.com/74675085/232182022-43e9cffe-b628-4c7e-9270-44e0c05419fd.png">
