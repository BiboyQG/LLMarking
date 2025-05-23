import gradio as gr
import requests
import json

css = """footer {visibility: hidden}
.logo img {height:100px; width:auto; margin:0 auto;}
"""
MAX_HISTORY_LEN = 50


def chat_streaming(query, history):
    # 调用api_server
    response = requests.post(
        "http://localhost:8888/chat",
        json={"query": query, "stream": True, "history": history},
        stream=True,
    )

    # 流式读取http response body, 按\0分割
    for chunk in response.iter_lines(
        chunk_size=8192, decode_unicode=False, delimiter=b"\0"
    ):
        if chunk:
            data = json.loads(chunk.decode("utf-8"))
            text = data["text"].rstrip("\r\n")  # 确保末尾无换行
            yield text


with gr.Blocks(css=css, title="Chat Space") as app:
    with gr.Row():
        logo_img = gr.Image(
            "https://s2.loli.net/2024/06/18/kbRqVAKdnFEhLj8.png",
            elem_classes="logo",
            show_download_button=False,
            show_label=False,
            container=False,
        )
    with gr.Row():
        chatbot = gr.Chatbot(label="LLMs", placeholder="Loading model...")
    with gr.Row():
        query_box = gr.Textbox(label="Chat", autofocus=True, lines=5)
    with gr.Row():
        clear_btn = gr.ClearButton([query_box, chatbot], value="Clear history")
        submit_btn = gr.Button(value="Submit")

    def chat(query, history):
        for response in chat_streaming(query, history):
            yield "", history + [(query, response)]
        history.append((query, response))
        while len(history) > MAX_HISTORY_LEN:
            history.pop(0)

    # 提交query
    submit_btn.click(chat, [query_box, chatbot], [query_box, chatbot])
    # query_box.submit(chat,[query_box,chatbot],[query_box,chatbot])

if __name__ == "__main__":
    app.queue(200)  # 请求队列
    app.launch(server_name="0.0.0.0", max_threads=500)  # 线程池
