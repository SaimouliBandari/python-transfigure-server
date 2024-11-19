FROM public.ecr.aws/docker/library/python:3.10

COPY ./app ${LAMBDA_TASK_ROOT}

COPY requirements.txt .

RUN pip install -r requirements.txt -t ${LAMBDA_TASK_ROOT} -U - no-cache-dir

CMD ["app.handler"]
