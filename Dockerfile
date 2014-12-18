FROM python:2-onbuild

RUN useradd --system flask

EXPOSE 5000

RUN pip install gunicorn

USER flask

CMD [ "python", "/usr/src/app/project/website.py" ]
