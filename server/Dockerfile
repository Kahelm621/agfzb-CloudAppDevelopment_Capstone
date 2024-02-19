FROM python:3.12.0-slim-bookworm

# Set environment variables
ENV PYTHONBUFFERED 1
ENV PYTHONWRITEBYTECODE 1
ENV APP /app

# Change the workdir.
WORKDIR $APP

# Install the requirements
COPY requirements.txt $APP
RUN pip install -r requirements.txt

# Copy the rest of the files
COPY . $APP

EXPOSE 8000

# Set entrypoint script permissions
RUN chmod +x $APP/entrypoint.sh

# Define entrypoint and default command
ENTRYPOINT ["$APP/entrypoint.sh"]
CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "djangobackend.wsgi"]
