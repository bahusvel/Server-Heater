# Server-Heater
Why not use your servers to heat your office/room? You already have them anyway, and they are probably sitting there doing nothing. Turn them into a heater!!! Why? Because you can!

# How to use

You will need an arduino with LM35 temperature sensor hooked up to its analog pin 0, (you dont have to use arduino or LM35, you will just have to adjust the temperature sensor code to match your needs)

Then you find out what the serial port your microcontroller is using, its gonna be in /dev/tty[blablabla] (google how to do that).
Then you specify that port, the temperature you would like the heaters to turn on and turn off, the command to execute to make the servers heat the room, and a command to turn the heaters off (typically kill or killall). Some ideas for heating commands:
* stress ...
* bitcoin mining
* your own idea...

You will also need a list of IPs the controller can ssh into and run the commands on (these will be your servers). Also please ensure that your controller can login to your servers without a password (i.e. public key authentication instead of password, p.s. google that as well if you dont know how)

And thats pretty much it, you got yourself one hell of an expensive heater :) But it should work... atleast in theory...
