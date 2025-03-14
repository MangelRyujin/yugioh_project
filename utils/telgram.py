import asyncio
from telethon import TelegramClient, functions, types,Button

api_id = '28214263'
api_hash = 'e6ad542309069578d8d78b538505d01a'
phone = '+5358101589'
message="Hola, usted ha recibido una solicitud de compra. Por favor procese su solicitud en la https://mangel990202.pythonanywhere.com/administraci%C3%B3n/nuevas-pedidos/"

async def enviar_mensaje():
    client = TelegramClient('session', api_id, api_hash)
    
    try:
        async with client:
            if not client.is_user_authorized():
                code = input("Ingrese el código de verificación: ")
                await client.sign_in(phone, code)
            
            entity = await client.get_entity(phone)
            result = await client.send_message(entity, message)
            
            
    except Exception as e:
        print(f"Error: {str(e)}")

# Ejecutar el código asíncrono
asyncio.run(enviar_mensaje())