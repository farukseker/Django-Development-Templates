FROM python:3.13-slim

WORKDIR /app

COPY /backend/docker_requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN useradd -m appuser
USER appuser

EXPOSE 8000

# RUN python manage.py collectstatic --noinput
# RUN python manage.py migrate --noinput

# CMD ["gunicorn", "--workers=4", "--bind=0.0.0.0:8000", "config.wsgi:application", "&&", 'celery', '-A', 'config', 'worker', '--loglevel=info', "&&", 'celery', '-A', 'config', 'beat', '--loglevel=info']
CMD ["gunicorn", "--workers=4", "--bind=0.0.0.0:8000", "config.wsgi:application"]