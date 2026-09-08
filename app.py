import streamlit as st
import requests
import urllib.parse
import time

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

# Функция для генерации уникального текста через бесплатный ИИ
def ask_ai(system_prompt, user_question):
    try:
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_question}
        ]
        response = requests.post(
            "https://pollinations.ai",
            json={"messages": messages, "model": "openai-large"},
            timeout=15
        )
        if response.status_code == 200:
            return response.text
        else:
            return "Мяу... Мой кошачий мозг устал. Попробуй еще раз через минуту!"
    except:
        return "Ошибка связи с кошачьим разумом. Проверь интернет!"

# Шапка сайта
st.title("VasyaOS — Интеллектуальная Система Кота Василия")
st.write("Добро пожаловать в мультимодельную систему, посвященную коту Василию.")

# Боковая панель для выбора моделей
st.sidebar.header("Доступные модели")
model_choice = st.sidebar.selectbox(
    "Выберите модель для работы:",
    ["VasyaTheCat (Болталка)", "VasyaExpert (Вопросы)", "VasyaAI (Энциклопедия)", "VasyaLyrics (Поэт)", "CanvasVasya (Арт)"]
)

# Логика для каждой модели
if model_choice == "VasyaTheCat (Болталка)":
    st.subheader("Модель: VasyaTheCat")
    st.info("Василий общается лично с вами. Он ленив, слегка высокомерен, отвечает как кошачий король, обожает пельмени и сон.")
    system_prompt = f"Ты — сам кот Василий. Твоя биография: {VASYA_BIO}. Отвечай лениво, по-королевски, слегка высокомерно, используй кошачьи повадки, иногда вставляй 'мяу' и требуй пельмени или пожаловаться на жизнь на кресле. Пиши строго на русском языке."

elif model_choice == "VasyaExpert (Вопросы)":
    st.subheader("Модель: VasyaExpert")
    st.info("Технический эксперт по Василию. Ответит на любые вопросы о его рационе, привычках и здоровье.")
    system_prompt = f"Ты — эксперт-аналитик по коту Василию. Твоя задача — четко, грамотно и подробно отвечать на вопросы пользователей, используя только реальные факты из этой официальной базы данных: {VASYA_BIO}. Пиши строго на русском языке."

elif model_choice == "VasyaAI (Энциклопедия)":
    st.subheader("Модель: VasyaAI")
    st.info("Официальная вежливая модель. Рассказывает гостям сайта биографию и историю Василия.")
    system_prompt = f"Ты — вежливый искусственный интеллект-энциклопедия 'VasyaAI'. Твоя цель — уважительно и интересно рассказывать гостям сайта про кота Василия на основе фактов: {VASYA_BIO}. Пиши строго на русском языке."

elif model_choice == "VasyaLyrics (Поэт)":
    st.subheader("Модель: VasyaLyrics")
    st.info("Поэт-песенник. Напишите ему тему или слово, и он сочинит смешной стих или рэп про Васю.")
    system_prompt = f"Ты — поэт-песенник. Сочиняй смешные, забавные стихи, четверостишия или рэп-куплеты про кота Василия на основе его привычек (пельмени, костер, кресло, усы): {VASYA_BIO}. Обязательно рифмуй строки. Пиши строго на русском языке."

elif model_choice == "CanvasVasya (Арт)":
    st.subheader("Модель: CanvasVasya")
    st.info("Генератор картинок. Здесь вы можете сгенерировать любое изображение с Васей.")
    
    user_prompt = st.text_input("Напишите сюжет для картинки (например: Кот сидит у костра):", "Кот Василий ест пельмени")
    
    if st.button("Сгенерировать арт"):
        if user_prompt:
            with st.spinner("Василий берет в лапы кисть... Подождите немного..."):
                # Кодируем текст и добавляем случайный seed (время), чтобы картинки всегда были разными
                current_time = int(time.time())
                encoded_prompt = urllib.parse.quote(f"fluffy brown tabby cat, green eyes, white whiskers, {user_prompt}, digital art, highly detailed")
                image_url = f"https://pollinations.ai{encoded_prompt}?width=1024&height=1024&nologo=true&seed={current_time}"
                
                # Отображаем картинку
                st.image(image_url, caption=f"Арт: {user_prompt}")


# Работа чата для текстовых моделей
if model_choice != "CanvasVasya (Арт)":
    user_input = st.text_input("Напишите ваше сообщение для ИИ:")
    
    if st.button("Отправить"):
        if user_input:
            with st.spinner("Василий думает..."):
                # Получаем настоящий живой ответ от ИИ
                ai_response = ask_ai(system_prompt, user_input)
                
                st.write("---")
                st.write(f"**Вы:** {user_input}")
                st.write("**VasyaOS:**")
                st.success(ai_response)


