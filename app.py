import streamlit as st
import urllib.parse

# Настройка страницы сайта
st.set_page_config(page_title="VasyaOS", page_icon="cat", layout="centered")

# Данные о Василии для ИИ
VASYA_BIO = """
Имя кота: Василий (Вася). Возраст: 5 лет. Порода: Дворняжка.
Внешность: Пушистый, коричнево-серый окрас с темными полосками, зеленые глаза, розовый носик, белые усы.
Характер: Любит тепло, сидеть у костра и в теплых местах. Ленивый, харизматичный, мудрый.
Любимая еда: Сухой корм и ПЕЛЬМЕНИ.
Привычки: Спит на кресле или кровати, мастерски выпрашивает еду.
"""

# Шапка сайта
st.title("VasyaOS — Интеллектуальная Система Кота Василия")
st.write("Добро пожаловать в мультимодельную систему, посвященную коту Василию.")

# Боковая панель для выбора моделей
st.sidebar.header("Доступные модели")
model_choice = st.sidebar.selectbox(
    "Выберите модель для работы:",
    ["VasyaTheCat (Болталка)", "VasyaExpert (Вопросы)", "VasyaAI (Энциклопедия)", "VasyaLyrics (Поэт)", "CanvasVasya (Арт)"]
)

# Описание выбранной модели
if model_choice == "VasyaTheCat (Болталка)":
    st.subheader("Модель: VasyaTheCat")
    st.info("Василий общается лично с вами. Он ленив, слегка высокомерен, но любит собеседников (особенно если у них есть пельмени).")

elif model_choice == "VasyaExpert (Вопросы)":
    st.subheader("Модель: VasyaExpert")
    st.info("Технический эксперт по Василию. Ответит на любые вопросы о его рационе, привычках и здоровье.")

elif model_choice == "VasyaAI (Энциклопедия)":
    st.subheader("Модель: VasyaAI")
    st.info("Официальная вежливая модель. Рассказывает гостям сайта биографию и историю Василия.")

elif model_choice == "VasyaLyrics (Поэт)":
    st.subheader("Модель: VasyaLyrics")
    st.info("Поэт-песенник. Напишите ему любое слово, и он сочинит смешной стих или рэп про Васю.")

elif model_choice == "CanvasVasya (Арт)":
    st.subheader("Модель: CanvasVasya")
    st.info("Генератор картинок. Здесь вы можете сгенерировать любое изображение с Васей.")
    
    user_prompt = st.text_input("Напишите, какую картинку с Васей вы хотите сгенерировать:", "Кот Василий ест пельмени")
    
    if st.button("Сгенерировать арт"):
        if user_prompt:
            st.write("---")
            st.write("Генерирую изображение...")
            
            # Кодируем текст для ссылки генератора картинок Pollinations AI
            encoded_prompt = urllib.parse.quote(f"fluffy brown tabby cat named Vasya, green eyes, {user_prompt}, realistic, highly detailed")
            image_url = f"https://pollinations.ai{encoded_prompt}?width=1024&height=1024&nologo=true&seed=42"
            
            # Показываем картинку пользователю
            st.image(image_url, caption=f"Арт по запросу: {user_prompt}")


# Реализация чата (для текстовых моделей)
if model_choice != "CanvasVasya (Арт)":
    user_input = st.text_input("Напишите ваше сообщение для модели:")
    
    if st.button("Отправить"):
        if user_input:
            st.write("---")
            st.write(f"**Вы:** {user_input}")
            st.write("**VasyaOS:**")
            
            # На следующем шаге мы заменим эти строки на реальный вызов бесплатного ChatGPT/Gemini API
            if model_choice == "VasyaTheCat (Болталка)":
                st.success(f"Мяу... Чего тебе, человек? Твое '{user_input}' отвлекает меня от сна на кресле. Лучше принеси пельменей!")
            elif model_choice == "VasyaLyrics (Поэт)":
                st.success(f"Стих на тему '{user_input}':\n\nКот Василий на кровати тихо-тихо спал,\nПро '{user_input}' лениво усом колыхал.\nВдруг почуял запах теплых пельменей —\nИ примчался к кухне тигра побыстрей!")
            elif model_choice == "VasyaExpert (Вопросы)":
                st.success(f"Я зафиксировал ваш вопрос: '{user_input}'. Чтобы ответить на него уникальным текстом из базы данных Василия, нам осталось подключить бесплатный текстовый токен ИИ. Давай сделаем это сейчас!")
            else:
                st.success(f"Привет! Я обрабатываю твой запрос '{user_input}' по коту Василию. Мой мозг сейчас настраивается!")

