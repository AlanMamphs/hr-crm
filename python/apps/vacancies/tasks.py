
from djcelery import celery
from apps.utils.rabbitmq import RabbitMQ
from apps.departments.models import Department
import json
from apps.vacancies.models import Vacancy, Publication


@celery.task
def send_message_to_java(queryset, serializer):
	rabbit = RabbitMQ(host="192.168.89.80", user="guest", password="guest")
	content = rabbit.call_java(queryset, serializer, exchange_name='share',
    			q_receiving='shareResponse', q_sending='facebook.publish')
	
	if content:
		content = content.decode('utf-8')
		content = json.loads(content)
		vacancy = Vacancy.objects.get(uuid=content['uuid'])
		print(vacancy.id)

		response = {
			'vacancy': Vacancy.objects.get(uuid=content['uuid']),
			'message': content['message'],
			'url': content['url'],
			'status':content['status'],
			'publication_service':content['publisher_service_type'],
			'created':content['publish_date']	
		}	

		p = Publication.objects.create(**response)
		

	print(content)