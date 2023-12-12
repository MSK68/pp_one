FROM python:3.9

ARG GRADIO_SERVER_PORT=7860
ENV GRADIO_SERVER_PORT=${GRADIO_SERVER_PORT}

WORKDIR /workspace

COPY requirements.txt /workspace/
RUN pip install -r /workspace/requirements.txt

COPY src/main.py /workspace/

ENV HOME=/workspace

CMD ["python", "/workspace/main.py"]