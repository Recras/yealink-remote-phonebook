FROM python:3-onbuild

EXPOSE 8000
RUN useradd --system gunicorn
RUN pip install gunicorn

USER gunicorn

CMD [ "gunicorn", "--bind", "0.0.0.0:8000", "--pythonpath", "/usr/src/app/project", "website:app" ]
