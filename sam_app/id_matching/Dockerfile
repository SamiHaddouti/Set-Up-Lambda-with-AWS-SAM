FROM public.ecr.aws/lambda/python:3.9

COPY requirements.txt ./

RUN python3.9 -m pip install --upgrade pip
RUN python3.9 -m pip install wheel
RUN yum install -y gccv 
RUN python3.9 -m pip install -r requirements.txt -t .

COPY app.py helper_functions.py ./

# Command can be overwritten by providing a different command in the template directly.
CMD ["app.lambda_handler"]