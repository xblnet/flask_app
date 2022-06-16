# flask_app

Description: 
The web application built on the a linux system with Nginx web proxy configued in a docker setup in Yaml file with python program called Flask. 
Programming the web application in Visual Studio Code IDE with Docker Desktop installed in the Windows System.
```
Deployment(Ubuntu):
  1. git clone https://github.com/xblnet/flask_app    #copy the whole python app and yaml doc to the local server(Ubuntu)
  2. sudo apt-get install docker                      #install docker
  3. docker-compose up                                #download docker images from docker hub by yaml doc and show the outcomes, the current folder must in the donloaded github file.
  4. sudo docker ps/stats                             #show the docker enables and usage of system for the services.
  5. sudo docker images ls                            #show docker images
  6. sudo ifconfig                                    #check the local ip
  7. xxx.xxx.xxx.xxx                                  #check the webserver from the another PC in brownser.

Prerequisite for Development(Windows):
  1. Docker Desktop
  2. Visual Studio Code(IDE)
  3. Oracle VM VirtualBox Manager(testing)
  
Development:
  1.docker-compose up
  2.docker tag
  3.docker push

Others:
  1. git pull origin main                             #update github file from github if the code changed.
  2. docker-compose up --detach                       #run the docker images in the background, but the app will not store date in the database.
  3. docker build -t python .                         #build docker with python program in development IDE, currenct directory match contain Dockerfile file.
  4. docker run -t python                             #run docker image with interactive mode.
  5. docker image rm -f e56f5e035c7d                  #remove image with its id
  6. docker stop id-98e8ec51382d                      #stop the container with it's id  
  7. sudo docker exec -it 5b56bdec28c5 /bin/bash      #run docker image with bash mode with its id
  8. sudo docker run -it xblcn/python bash            #run docker image with bash mode with its name
  9. docker run -d -p 80:5000 python                  #run a image with forward port, add "-p 22:22" with extra ports.
  10. docker buildx build --platform linux/arm -t python . --push  	#build a python docker image for amr v7 architecture and push it to the docker hub.
  11. docker tag python xblcn/python    
      docker push xblcn/python                        #push image to docker hub
```

website: [phay.me](http://phay.me)
