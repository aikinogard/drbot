#DrBOT
##About

DrBOT is a personal assistant based on python and celery. It can automatically check the information of your interest and give you updates.

##Email configuration
You need to allow ["less secure apps"](https://www.google.com/settings/security/lesssecureapps) on your Gmail account.
	
Enter the email configuration in `email_configuration.json`

	{
		"sender": "senderXXX@gmail.com",
		"password": "senderpassword",
		"receivers": ["receiver1@gmail.com", "receiver2@gmail.com"]
	}

##Setup
###install redis
	wget http://download.redis.io/redis-stable.tar.gz
	tar xvzf redis-stable.tar.gz
	cd redis-stable
	make
	make test
	sudo make install
	
### install celery
	pip install celery
	pip install -U "celery[redis]"
	
### install python dependency
	pip install -r requirements.txt
	
##Run Celery
start a redis server

	redis-server
	
start celery workers

	celery -A tasks -l INFO worker

start periodic tasks
	
	celery -A tasks -l INFO beat