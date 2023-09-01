FROM ubuntu:20.04
RUN apt-get update && apt-get install python3-pip -y && pip3 install pytest==7.3.1 && pip3 install requests==2.31.0
ADD test_content.py /test_content/test_content.py 
ADD content.py /test_content/content.py
WORKDIR /test_content/
EXPOSE 8000
ENV LOG=1
CMD python3 -m pytest test_content.py
