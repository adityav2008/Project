FROM centos:centos7.9.2009
MAINTAINER Aditya Verma <aditya.verma@naukri.com>

#ADD jdk-8u321-linux-x64.rpm /tmp
RUN yum install java-1.8.0-openjdk -y
#RUN rm -rf /tmp/jdk-8u321-linux-x64.rpm
CMD ["/usr/bin/java", "-version"]