from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import openai

app = Flask(__name__)

client = openai.OpenAI(
    api_key="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",
    organization="org-EGa2wJvxhFRpBMc9X8JL5ybn",
    project="proj_gbnzJRgeYifNzqBJ1M7LSJka"
)

@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    incoming_msg = request.values.get("Body", "").strip()

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Ты консультант Home Credit Bank. Помогаешь клиентам с заявками, выписками, картой OZEN и ошибками."},
            {"role": "user", "content": incoming_msg}
        ]
    )

    gpt_reply = response.choices[0].message.content.strip()
    twilio_resp = MessagingResponse()
    twilio_resp.message(gpt_reply)
    return str(twilio_resp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)


