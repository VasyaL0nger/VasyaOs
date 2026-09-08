import streamlit as st
import requests
import urllib.parse
import time
from g4f.client import Client

# Настройка страницы сайта
st.set_page_config(page_title="VasyaOS", page_icon="cat", layout="centered")

# База данных о Василии для ИИ
VASYA_BIO = (
    "Имя кота: Василий (Вася). Возраст: 5 лет. Порода: Дворняжка. "
    "Внешность: Пушистый, коричнево-серый окрас с темными полосками, зеленые глаза, розовый носик, белые усы. "
    "Характер: Любит тепло, сидеть у костра и в теплых местах. Ленивый, харизматичный, мудрый. "
    "Любимая еда: Сухой корм и ПЕЛЬМЕНИ. За пельмени готов продать душу. "
    "Привычки: Спит на кресле или кровати, мастерски выпрашивает еду гипнотическим взглядом."
)

# Сверхнадежная функция текстового ИИ через обходные сервера g4f
def ask_free_ai(system_prompt, user_question):
    try:
        client = Client()
        full_prompt = f"Системная роль: {system_prompt}\n\nПользователь спрашивает: {user_question}\nОтветь коротко, строго на русском языке в соответствии со своей ролью."
        
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": full_prompt}],
        )
        answer = response.choices[0].message.content
        if answer:
            return answer
        return "Мяу... Что-то связь оборвалась. Попробуй нажать кнопку отправки еще раз!"
    except:
        return "Василий ушел за пельменями на кухню. Пожалуйста, нажми на кнопку еще раз!"

# Шапка сайта
st.title("VasyaOS — Интеллектуальная Система Кота Василия")
st.write("Добро пожаловать в мультимодельную систему, посвященную коту Василию.")

# Боковая панель для выбора моделей
st.sidebar.header("🤖 Доступные модели")
model_choice = st.sidebar.selectbox(
    "Выберите модель для работы:",
    ["VasyaTheCat (Болталка)", "VasyaExpert (Вопросы)", "VasyaAI (Энциклопедия)", "VasyaLyrics (Поэт)", "CanvasVasya (Арт)"]
)

# Настройка системных ролей
if model_choice == "VasyaTheCat (Болталка)":
    st.subheader("Модель: VasyaTheCat")
    st.info("Василий общается лично с вами. Он ленив, слегка высокомерен, отвечает как кошачий король, обожает пельмени.")
    system_prompt = "Ты — сам кот Василий. Отвечай лениво, гордо, по-королевски. Используй кошачьи фразочки, пиши коротко, вставляй 'мяу' и требуй пельмени за общение. Отвечай только на русском языке."

elif model_choice == "VasyaExpert (Вопросы)":
    st.subheader("Модель: VasyaExpert")
    st.info("Технический эксперт по Василию. Ответит на любые вопросы о его рационе, привычках и здоровье.")
    system_prompt = f"Ты — эксперт по коту Василию. Используй только эти реальные факты: {VASYA_BIO}. Отвечай информативно, четко и по делу на русском языке."

elif model_choice == "VasyaAI (Энциклопедия)":
    st.subheader("Модель: VasyaAI")
    st.info("Официальная вежливая модель. Рассказывает гостям сайта биографию и историю Василия.")
    system_prompt = f"Ты — вежливый ИИ-гид 'VasyaAI'. Твоя цель — уважительно, развернуто и красиво рассказать про кота Василия на основе фактов: {VASYA_BIO}. Отвечай на русском языке."

elif model_choice == "VasyaLyrics (Поэт)":
    st.subheader("Модель: VasyaLyrics")
    st.info("Поэт-песенник. Напишите ему слово, и он сочинит смешной стих про Васю.")
    system_prompt = f"Ты — поэт. Сочиняй забавные и смешные стихотворения с хорошей рифмой про кота Василия на русском языке, опираясь на его привычки: {VASYA_BIO}."

elif model_choice == "CanvasVasya (Арт)":
    st.subheader("Модель: CanvasVasya")
    st.info("Генератор картинок. Сюжет можно писать на русском языке!")
    
    user_prompt = st.text_input("Напишите сюжет для картинки:", "Кот Василий ест пельмени у костра")
    
    if st.button("Сгенерировать арт"):
        if user_prompt:
            with st.spinner("Василий берет в лапы кисть... Подождите немного..."):
                # Используем g4f для перевода, так как он надежнее
                english_keywords = ask_free_ai("You are a translator. Translate the text into english keywords for image generation.", user_prompt)
                
                if "Василий ушел" in english_keywords or len(english_keywords) > 150:
                    english_keywords = "cat eating dumplings near fire"
                
                seed = int(time.time())
                final_prompt = f"fluffy brown tabby cat, green eyes, {english_keywords.strip()}, digital art, cute style, highly detailed"
                encoded_prompt = urllib.parse.quote(final_prompt)
                
                image_url = f"https://pollinations.ai{encoded_prompt}?width=512&height=512&seed={seed}&nofeed=true"
                st.image(image_url, caption=f"Арт по вашему сюжету: {user_prompt}")

# Работа чата для текстовых моделей
if model_choice != "CanvasVasya (Арт)":
    user_input = st.text_input("Напишите ваше сообщение для ИИ:")
    
    if st.button("Отправить"):
        if user_input:
            with st.spinner("Василий думает..."):
                ai_response = ask_free_ai(system_prompt, user_input)
                st.write("---")
                st.write(f"**Вы:** {user_input}")
                st.write("**VasyaOS:**")
                st.success(ai_response)
