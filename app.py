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


