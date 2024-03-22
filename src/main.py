"""
Приложение для сокращения текста. В качестве модели используется модель d0rj/rut5-base-summ.
Приложение реализовано с помощью библиотеки gradio.
"""

import gradio as gr
from transformers import pipeline

min_leght = 250


def summarize_text(articleInput, minimal_length, maximum_length):
    """
    Функция для сокращения текста. В качестве модели используется модель d0rj/rut5-base-summ.
    :param articleInput: Входной текст, string
    :param min_length_of_article: Минимальное количество слов в сокращенном виде, int
    :param max_length_of_article: Максимальное количество слов в сокращенном виде, int
    :return: Сокращенный текст, string
    """
    if len(articleInput) > min_leght:
        summarizedArticle = summarizer_pipline(articleInput,
                                               min_length=minimal_length,
                                               max_length=maximum_length,
                                               do_sample=False)
        return summarizedArticle[0]['summary_text']
    return f'Минимальное количество символов в статье {min_leght}'


summarizer_pipline = pipeline('summarization', model="d0rj/rut5-base-summ")  # Загрузка модели

ifrace = gr.Interface(fn=summarize_text,
                    title="Суммаризация текста",
                    inputs=[
                        gr.Textbox(lines=20, placeholder="Введите статью ее сокращения", label="Ввод текста",
                                   interactive=True),
                        gr.Slider(50, 200, value=50, step=10, label="Минимальное количество слов в сокращенном виде",
                                  info="Выберите от 50 до 200"),
                        gr.Slider(200, 500, value=200, step=10, label="Максимальное количество слов в сокращенном виде",
                                  info="Выберите от 200 and 500"),
                    ],
                    outputs=gr.Textbox(lines=20, label="Выход", show_copy_button=True),
                    allow_flagging='never')

if __name__ == "__main__":
    ifrace.launch(server_name="0.0.0.0", server_port=7860)
