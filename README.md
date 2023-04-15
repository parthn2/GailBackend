# GailBackend

This application is being used by a web application and android application for a Gail Project which is currently in progress in IIT Kharagpur. This application is hosted over local network of IIT Kgp using gunicorn & nginx and can be accesed from 10.29.8.37

#Documentation

##API: 

###    http://10.29.8.37/admin/
/admin/ endpoint is for managing the data stored in database

###    http://10.29.8.37/motors/
/motors/ endpoint is viewing all the motors with the current and voltage values stored in it

###    http://10.29.8.37/motors/<int:motor_id>/
/motors/<int:motor_id>/ endpoint is for viewing the current and voltage values for the motor id : <int:motor_id>
