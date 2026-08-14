import gradio as gr
def chatbot(user):
    user = user.lower()

    if "exit" in user:
        return "Allah Hafiz!"
    elif "school start" in user:
       return("Bot: School starts at 8:00 AM.")

    elif "period 1" in user:
       return("Bot: Period 1 is from 8:00 AM to 8:40 AM.")

    elif "period 2" in user:
       return("Bot: Period 2 is from 8:40 AM to 9:20 AM.")

    elif "period 3" in user:
       return("Bot: Period 3 is from 9:20 AM to 10:00 AM.")

    elif "period 4" in user:
       return("Bot: Period 4 is from 10:00 AM to 10:40 AM.")

    elif "break" in user:
       return("Bot: Break is from 10:40 AM to 11:00 AM.")

    elif "period 5" in user:
       return("Bot: Period 5 is from 11:00 AM to 11:40 AM.")

    elif "period 6" in user:
       return("Bot: Period 6 is from 11:40 AM to 12:20 PM.")

    elif "school off" in user or "school end" in user:
       return("Bot: School ends at 12:30 PM.")

    else:
        return("BOT: Sorry, I don't understand your question.")

demo = gr.Interface(
     fn=chatbot,
     inputs=gr.Textbox(label="Ask about the timetable"),
     outputs=gr.Textbox(label="Chatbot"),
     title="School Timetable Chatbot",
     description="Assalam-o-Alikum! Ask me about school timings and periods."
 )
import os

demo.launch(
    server_name="0.0.0.0",
    server_port=int(os.environ.get("PORT", 7860))
)
