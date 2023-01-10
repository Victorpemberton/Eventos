import redis

CHANNEL ='joerlyn'
usuario=input('Ingrese su Usuario: ')

if __name__=='__main__':
    client=redis.StrictRedis(host='localhost',port=6379,db=0)
    
while True:
    message= input('Ingrese el mensaje: ')
    client.publish(CHANNEL,f'{usuario}: {message}')