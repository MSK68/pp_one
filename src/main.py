import gradio as gr
from transformers import pipeline
import re


min_leght = 1000



def summ(articleInput, min_length_of_article, max_length_of_article):
    if len(articleInput) > min_leght :
        summarizedArticle = summarizer_pipline(articleInput, 
                                                     min_length=min_length_of_article, 
                                                     max_length=max_length_of_article, 
                                                     do_sample=False)
        return summarizedArticle[0]['summary_text']
    return f'Минимальное количество символов в статье {min_leght}'



summarizer_pipline = pipeline('summarization', model="d0rj/rut5-base-summ")

demo = gr.Interface(fn=summ, 
                     title="Суммаризация текста",
                     inputs=[
                         gr.Textbox(lines=20, placeholder="Введите статью для ее сокращения", label="Ввод текста", interactive=True),
                         gr.Slider(50, 250, value=10, step=10, label="Минимальное колличество слов в сокращенном варианте", info="Выберите от 50 до 250"),
                         gr.Slider(300, 1000, value=120, step=10, label="Максимальное колличество слов в сокращенном варианте", info="Выберите от 300 and 1000"),
                     ],
                     outputs=gr.Textbox(lines=20, label="Выход", show_copy_button=True),
                     allow_flagging='never')


if __name__=="__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)