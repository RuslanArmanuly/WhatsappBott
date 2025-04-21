from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import openai

app = Flask(__name__)

client = openai.OpenAI(
    api_key="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",
    organization="org-EGa2wJvxhFRpBMc9X8JL5ybn",
    project="proj_U30YgR005BETRTnmfy4ied7K"
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


