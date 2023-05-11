FROM mcr.microsoft.com/playwright/python:v1.32.0-jammy

# RUN
RUN pip install poetry

# RUN
RUN poetry config virtualenvs.in-project true

# RUN
# RUN apt-get update -y && \
#     apt-get upgrade -y \ 
#     gstreamer1.0-libav \
#     libnss3-tools \
#     libatk-bridge2.0-0 \
#     libcups2-dev \
#     libxkbcommon-x11-0 \
#     libxcomposite-dev \
#     libxrandr2 \
#     libgbm-dev \
#     libgtk-3-0 \
#     libdbus-glib-1-2 

# WORKDIR
WORKDIR /_app

# COPY
ADD / /_app

RUN poetry install --only prod

RUN poetry run playwright install firefox



# RUN playwright install firefox

# RUN uvicorn main:app --host localhost --port 8085 --timeout-keep-alive 30



