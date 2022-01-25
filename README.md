# House rent app (Work Inprogress!!! sorry if stuff is left dangling!)
## _Starter app, For ML deployment_
## Features
- Provide API support 
- Serving ML model prod ready 

## Tech
Houseapp uses a number of open source projects to work properly *SPOILER* you need it too!!!:

![python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=darkgreen)
![docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![bash](https://img.shields.io/badge/Shell_Script-121011?style=for-the-badge&logo=gnu-bash&logoColor=white)

## Installation/Setup

HouseApp requires [python](https://www.python.org/) v3+ to run.

Install the dependencies and devDependencies and start the server.

```sh
 cd  house rent app
make up
```
```python
Building api
 => [internal] load build definition from Dockerfile                 
 => [internal] load .dockerignore                                    
 => [internal] load metadata for docker.io/tiangolo/uvicorn-gunicorn-
 => => transferring context: 2.55kB                                  
 => CACHED [1/6] FROM docker.io/tiangolo/uvicorn-gunicorn-fastapi:pyt
 => [2/6] COPY . /api                                                
 => [4/6] RUN pip install --upgrade pip                              
 => [5/6] RUN pip install -r /tmp/requirements.txt                   
 => [6/6] WORKDIR /api                                               
 => => exporting layers                                              
 => => writing image sha256:6ba112882dafff92885596bfaa9e1ca2ce80c79cc
 => => naming to docker.io/library/houserentapp_api    
```
## RunIt!!!

![Capture](https://user-images.githubusercontent.com/30224411/150890135-97952bb8-7fbe-494d-ab62-7403c21f0440.PNG)


## Stop

```sh
 cd  house rent app
make down
```

Verify the deployment by navigating to your server address in
your preferred browser.

```sh
localhost:4040
```

## License

MIT

**Free Software, Hell Yeah!**
