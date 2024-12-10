import gradio as gr
from example1 import chain


# def chat(question, history):
#     # if question == "":
#     #     return "Please ask a question"
#     # else:
#     #     return chain.invoke(question)

#     history.append({"role" : "user", "content" : question})
#     if question == "":
#         response = "Please ask a question"
#         history.append({"role" : "assistant", "content" : response})

#     else:
#         history.append({"role" : "assistant", "content" : ""})
#         response = chain.stream(question)

#     for res in response:
#         history[-1]["content"] +=res
#         yield " ",res
        

# gr.ChatInterface(
#     fn = chat,
#     type = "messages"
# ).launch(
#     share=True,
# )

def chat(question, history):
    history.append({"role" : "user", "content" : question})
    if question == "":
        response = "Please ask a question"
        history.append({"role" : "assistant", "content" : response})

    else:
        history.append({"role" : "assistant", "content" : ""})
        response = chain.stream(question)

    for res in response:
        history[-1]["content"] +=res
        yield " ",res
        
    textbox.submit(chat, [textbox, chatbox])
    submit_button.click(chat, [textbox, chatbox])



with gr.Blocks(title = "Chatbot") as demo:
    gr.Markdown("# Chat with GPT-4 Demo")
    with gr.Row():
        gr.Markdown("")
        with gr.Column(scale = 6):
            chatbox = gr.Chatbot(type = "messages")

            with gr.Row():
                textbox = gr.Textbox(scale = 7, container= False, placeholder= "Ask me anything")
                submit_button = gr.Button(
                    value= "Submit",
                    scale = 3,
                    variant= "primary"
                )
        gr.Markdown("")
        



demo.launch(
    server_name = "0.0.0.0",
    server_port = 7860
)