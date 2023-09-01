FROM ubuntu:20.04
RUN apt-get update && apt-get install python3-pip -y && pip3 install pytest==7.3.1 && pip3 install requests==2.31.0
ADD test_authorization.py /test_authorization/test_authorization.py 
ADD authorization.py /test_authorization/authorization.py
WORKDIR /test_authorization/
EXPOSE 8000
ENV LOG=1
CMD python3 -m pytest test_authorization.py
