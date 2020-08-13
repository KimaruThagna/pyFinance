FROM python:3.8.3-alpine
ENV MICRO_SERVICE=/home/app/microservice
ENV APP_USER=app_user
# create the app user
RUN addgroup -S $APP_USER && adduser -S $APP_USER -G $APP_USER
# set work directory


RUN mkdir -p $MICRO_SERVICE
RUN mkdir -p $MICRO_SERVICE/static

# where our code lives
WORKDIR $MICRO_SERVICE

EXPOSE 8501

COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD streamlit run app.py