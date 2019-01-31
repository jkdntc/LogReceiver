from confluent_kafka import Producer


p = Producer({'bootstrap.servers': 'kafka1,kafka2,kafka3,kafka4,kafka5'})

def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

def put2Kafka(data):
    #p.poll(0)
    p.produce('mytopic', data.encode('utf-8'), callback=delivery_report)
    print(data)
    #p.flush()
    p.flush(2)
    print('flush')

some_data_source = ['Method: GET|Path: /async|HTTP version: 1.1|Query string: None|Query: {}|Host: localhost:8080|Connection: keep-alive|Cache-Control: max-age=0|Upgrade-Insecure-Requests: 1|User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36|Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8|Accept-Encoding: gzip, deflate, br|Accept-Language: en,zh-CN;q=0.9,zh;q=0.8','b','c']

for data in some_data_source:
    put2Kafka(data)

# Wait for any outstanding messages to be delivered and delivery report
# callbacks to be triggered.
p.flush()
