# Tasks given by the mentors of Ganga.
 1. T1 is a basic hello world in Ganga.
2. T2 and T2argsplitter are implementations of Splitter classes of Ganga for a GenericSplitter and an ArgSplitter respectively.
 3. T3 is implementation of CustomMerger class to calculate total number of occurences of 'the'
 4. T4 is used to run any docker image from ganga itself. To run this job make sure you are root user.
* To get root access type the below command on your terminal
```sudo -s```
* Run the job using  ```ganga T4.py [container name]```

Please change the path in splitterjob.py to your respective home path where you clone this repo

### You can also pull in a docker image to run these jobs.
1. To install docker. See this documentation. [Docker Install](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
2. Run this command as root user to run the docker image ```docker run sanchitahuja/test:ganga```
3. Get the container id of the latest instance of the docker by typing ```docker container ls -a```
4. To copy the job data to your local directory run this docker command ```docker cp [container id]:/root/gangadir/workspace/root/LocalXML .```

