# seller_bot
Challenge and educational seller bot, with an api



```
Usage: make <target>

app                 Run app with docker like a prod app
install-local       Install and setup project dependencies
lint-fix            Fix the files with linter
dev                 Run app in dev mode
```

If you wanna run like dev you need run

```bash
make dev
```


## How to run

Fisrt update on .env file the values to need, in this case, this is not a production app (I know, the app mode, but is not ready)

```sh
ENV=dev
COMPANY_NAME="by confidentiality y put this value in a Enviroment constant"
OPENAI_API_KEY=mock
```

## Example of the healthcheck


A healcheck if a api is running
```sh
curl --location 'http://localhost:8000/healthcheck'
```

```javascript
{
    "status": "ok",
}
```


I put a healthcheck with openAI, if the conection is sucessful, returned a message
```sh
curl --location 'http://localhost:8000/healthcheck/openai'
```

```javascript
{
    "status": "ok",
    "model_count": 6
}
```


Use 



## Example of a send message of the chat

```sh
curl --location 'http://localhost:8000/chat' \
--header 'Content-Type: application/json' \
--data '{
    "message": "hola"
}'

```


and received a message like this


```javascript
{
    "reply": "Hola",
}
```

If you wanna answer by a specific auto



```sh

curl --location 'http://localhost:8000/chat' \
--header 'Content-Type: application/json' \
--data '{
    "message": "muestrame los nissan ?"
}'


```


```javascript
{
    "reply": "Aquí tienes algunas opciones de autos Nissan que tenemos actualmente en esta empresa tenemos:\n\n1. **2020 Nissan Kicks 1.6 ADVANCE LTS XTRONIC** - $338,999.\n2. **2019 Nissan Sentra 1.8 ADVANCE AUTO** - $268,999.\n3. **2022 Nissan Frontier 2.5 PRO-4X AUTO 4WD** - $637,999.\n4. **2018 Nissan Sentra 1.8 SENSE AUTO** - $199,999.\n5. **2019 Nissan Murano 3.5 EXCLUSIVE AUTO 4WD** - $385,999.\n6. **2018 Nissan March 1.6 ADVANCE AUTO** - $184,999.\n7. **2015 Nissan Pathfinder 3.5 EXCLUSIVE AT** - $218,999.\n8. **2020 Nissan Versa 1.6 ADVANCE CVT** - $265,999.\n9. **2015 Nissan Sentra 1.8 EXCLUSIVE NAVI CVT** - $183,999.\n10. **2018 Nissan Versa 1.6 EXCLUSIVE AUTO** - $220,999.\n11. **2021 Nissan X-Trail 2.5 SENSE 2 ROW CVT** - $407,999.\n12. **2018 Nissan Altima 2.5 SENSE AUTO** - $252,999.\n\nSi alguno de estos modelos te interesa, puedo proporcionarte más detalles sobre él o ayudarte a programar una visita para que lo veas en persona. Además, te ofrecemos financiamiento y garantía para que tu compra sea segura y confiable. No dudes en preguntar cualquier cosa adicional que necesites saber."
}
```