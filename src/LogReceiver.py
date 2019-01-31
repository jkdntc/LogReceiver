import asyncio
from japronto import Application

import KafkaProducer

def getRequestText(request):
    text = """Method: {0.method}|Path: {0.path}|HTTP version: {0.version}|Query string: {0.query_string}|Query: {0.query}""".format(request)

    if request.headers:
        for name, value in request.headers.items():
            text += "|{0}: {1}".format(name, value)
    return text

# This is a synchronous handler.
def synchronous(request):
    text=getRequestText(request)
    #KafkaProducer.put2Kafka(text)
    return request.Response(text=text)


# This is an asynchronous handler
async def asynchronous(request):
    def cb(request):
        text=getRequestText(request)
        KafkaProducer.put2Kafka(text)
    request.add_done_callback(cb)
    text=getRequestText(request)
    return request.Response(text=text)


app = Application()

r = app.router
r.add_route('/sync', synchronous)
r.add_route('/async', asynchronous)

app.run()