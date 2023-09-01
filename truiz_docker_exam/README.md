## Docker Examination

### Design Considerations

* Unit Testing 

Each test will be ran in it's own docker container. The pytest module is used to execute the unit tests

* Networking 

The API will be deployed to a network called "my_exam_network" and listen in on port 8000. The test containers will use the host network to issue requests to the application. 


* Logging 

An environment variable is defined in the Dockerfile. A volume is defined in the docker-compose yaml to store the results of the unit tests and all services will write to that volume. 

### Usage

* Create a virtual environment and install requirements 

```
python3 -m venv ./venv
source venv/bin/activate
pip3 -r requirements.txt
```

* Run application 

```
chmod +X ./setup.sh
./setup.sh

```


* Review Log File

```
sudo cp /var/lib/docker/volumes/truiz_docker_exam_log_vol/_data/api_test.log . 
cat api_test.log
```