# Pull python base image
FROM python:3.10

# install the toolbox runner tools
RUN pip install json2args==0.6.1

# install pandas and geopandas
RUN pip install pandas==2.1.4 geopandas==0.14.4

# create the tool input structure
RUN mkdir /in
RUN mkdir /out
RUN mkdir /src
COPY ./src /src

# Run tools
WORKDIR /src
CMD ["python", "run.py"]