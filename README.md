# IoT

A small project aimed at simulating the resource extraction of IoT devices on an eNodeB.

The steps identified to solve:
1. Define the user class which distributes the users over a grid
2. Define an eNodeB and hopefully build a worker that handles the users
3. Distribute the link of the users, randomising the radio characteristics of the link
4. If possible build and interworking mechanism where each active user adds to the interference (which is the case in reality)

The major work lies within point 2. Here it is
