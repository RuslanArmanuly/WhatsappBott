# WhatsApp GPT Bot for Home Credit

## Description
This bot connects Twilio WhatsApp messages to OpenAI GPT via Flask.

## Deployment (Render)
1. Push this folder to GitHub
2. Go to https://render.com and create a new Web Service
3. Use the repo you created
4. Set `start command` to: `python app.py`
5. Add build command: `pip install -r requirements.txt`

## Route
Endpoint: `/whatsapp`

## Note
Make sure to connect your Render app's public URL to your Twilio WhatsApp sandbox webhook.
