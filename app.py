from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import openai

app = Flask(__name__)

client = openai.OpenAI(
    api_key="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"
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


