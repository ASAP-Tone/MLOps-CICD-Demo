FROM ubuntu:20.04
RUN apt-get update && apt-get install python3-pip -y && pip3 install pytest==7.3.1 && pip3 install requests==2.31.0
ADD test_authentication.py /test_authentication/test_authentication.py 
ADD authentication.py /test_authentication/authentication.py
WORKDIR /test_authentication/
EXPOSE 8000
ENV LOG=1
CMD python3 -m pytest test_authentication.py
# CMD python3 authentication.py