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

# Новая более надежная функция для общения с ИИ
def ask_ai(system_prompt, user_question):
    try:
        # Используем альтернативный стабильный эндпоинт Pollinations
        prompt = f"System: {system_prompt}\nUser: {user_question}\nAnswer in Russian strictly."
        encoded_prompt = urllib.parse.quote(prompt)
        url = f"https://pollinations.ai{encoded_prompt}?model=openai"
        
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.text
        else:
            return "Мяу... Сервер занят. Принеси мне пельмешек и попробуй нажать кнопку еще раз!"
    except:
        return "Василий ушел спать на кресло. Нажми кнопку отправки еще раз!"

# Шапка сайта
st.title("VasyaOS — Интеллектуальная Система Кота Василия")
st.write("Добро пожаловать в мультимодельную систему, посвященную коту Василию.")

# Боковая панель для выбора моделей
st.sidebar.header("Доступные модели")
model_choice = st.sidebar.selectbox(
    "Выберите модель для работы:",
    ["VasyaTheCat (Болталка)", "VasyaExpert (Вопросы)", "VasyaAI (Энциклопедия)", "VasyaLyrics (Поэт)", "CanvasVasya (Арт)"]
)

# Настройка системных промптов
if model_choice == "VasyaTheCat (Болталка)":
    st.subheader("Модель: VasyaTheCat")
    st.info("Василий общается лично с вами. Он ленив, слегка высокомерен, отвечает как кошачий король, обожает пельмени.")
    system_prompt = f"Ты — сам кот Василий. Твоя биография: {VASYA_BIO}. Отвечай лениво, по-королевски, используй кошачьи повадки, пиши коротко, вставляй 'мяу' и требуй пельмени. Отвечай только по-русски."

elif model_choice == "VasyaExpert (Вопросы)":
    st.subheader("Модель: VasyaExpert")
    st.info("Технический эксперт по Василию. Ответит на любые вопросы о его рационе, привычках и здоровье.")
    system_prompt = f"Ты — эксперт по коту Василию. Четко и подробно отвечай на вопросы, используя факты: {VASYA_BIO}. Отвечай только по-русски."

elif model_choice == "VasyaAI (Энциклопедия)":
    st.subheader("Модель: VasyaAI")
    st.info("Официальная вежливая модель. Рассказывает гостям сайта биографию и историю Василия.")
    system_prompt = f"Ты — вежливый ИИ-гид. Уважительно рассказывай про кота Василия на основе фактов: {VASYA_BIO}. Отвечай только по-русски."

elif model_choice == "VasyaLyrics (Поэт)":
    st.subheader("Модель: VasyaLyrics")
    st.info("Поэт-песенник. Напишите ему слово, и он сочинит смешной стих про Васю.")
    system_prompt = f"Ты — поэт. Сочиняй смешные стихи с хорошей рифмой про кота Василия на основе его привычек: {VASYA_BIO}. Отвечай только по-русски."

elif model_choice == "CanvasVasya (Арт)":
    st.subheader("Модель: CanvasVasya")
    st.info("Генератор картинок. Здесь вы можете сгенерировать любое изображение с Васей.")
    
    user_prompt = st.text_input("Напишите сюжет для картинки (на английском работает лучше всего!):", "Cat eating dumplings near fire")
    
    if st.button("Сгенерировать арт"):
        if user_prompt:
            with st.spinner("Василий рисует..."):
                # Генерируем случайный seed, чтобы картинка обновилась и не ломалась
                seed = int(time.time())
                encoded_prompt = urllib.parse.quote(f"fluffy brown tabby cat, green eyes, {user_prompt}, 3d render, cute, highly detailed")
                # Изменили параметры ссылки на более стабильные
                image_url = f"https://pollinations.ai{encoded_prompt}?width=512&height=512&seed={seed}&nofeed=true"
                
                # Показываем результат
                st.image(image_url, caption=f"Ваш арт по запросу: {user_prompt}")

# Работа чата для текстовых моделей
if model_choice != "CanvasVasya (Арт)":
    user_input = st.text_input("Напишите ваше сообщение для ИИ:")
    
    if st.button("Отправить"):
        if user_input:
            with st.spinner("Василий думает..."):
                ai_response = ask_ai(system_prompt, user_input)
                st.write("---")
                st.write(f"**Вы:** {user_input}")
                st.write("**VasyaOS:**")
                st.success(ai_response)


