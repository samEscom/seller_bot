# seller_bot
Challenge and educational seller bot, with an api



## Example of the healthcheck

```sh
curl --location 'http://localhost:8000'
```



## Example of a send message of the chat

```sh
curl --location 'http://localhost:8000/chat' \
--header 'Content-Type: application/json' \
--data '{
    "message": "hola"
}'

```