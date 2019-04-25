# Serial-Keys
Program written in python to generate and check validity of the key. The keygen is supposed to be in the hands of the creator of the application and the verifier should be on a server listening for packets and sending back packets once verified (TCP packet listening not included). 

# Keygen
The concept is to have the serial key look like this (Serial key expiration time in seconds)-(Last 20 integers of the expiration time's corresponding y value on graph).

# Verification
It first checks to see if the time is earlier than the expiration time. Next it checks if the expiration time corresponds with the Y value in the serial key. This makes it virtually impossible to crack this serial key if you don't have the encryption graph.

