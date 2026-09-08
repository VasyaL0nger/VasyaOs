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

# Сверхнадежная функция текстового ИИ, работающая без токенов и ключей
def ask_free_ai(system_prompt, user_question):
    try:
        # Формируем единый понятный промпт для открытой нейросети
        full_text_prompt = f"Ты работаешь в системе кота Василия. Твоя системная роль: {system_prompt}\n\nПользователь написал: {user_question}\nОтветь строго на русском языке в соответствии со своей ролью:"
        encoded_text = urllib.parse.quote(full_text_prompt)
        
        # Запрос к открытому текстовому серверу
        url = f"https://pollinations.ai{encoded_text}?model=search"
        response = requests.get(url, timeout=15)
        
        if response.status_code == 200:
            return response.text
        else:
            return "Мяу... Мой кошачий процессор перегружен. Попробуй нажать кнопку еще раз!"
    except:
        return "Василий отвлекся на пельмени. Пожалуйста, повтори отправку."

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
    system_prompt = "Ты — сам кот Василий. Отвечай лениво, гордо, по-королевски. Используй кошачьи фразочки, пиши коротко, вставляй 'мяу' и требуй пельмени за общение."

elif model_choice == "VasyaExpert (Вопросы)":
    st.subheader("Модель: VasyaExpert")
    st.info("Технический эксперт по Василию. Ответит на любые вопросы о его рационе, привычках и здоровье.")
    system_prompt = f"Ты — эксперт по коту Василию. Используй только эти реальные факты: {VASYA_BIO}. Отвечай информативно, четко и по делу."

elif model_choice == "VasyaAI (Энциклопедия)":
    st.subheader("Модель: VasyaAI")
    st.info("Официальная вежливая модель. Рассказывает гостям сайта биографию и историю Василия.")
    system_prompt = f"Ты — вежливый ИИ-гид 'VasyaAI'. Твоя цель — уважительно, развернуто и красиво рассказать про кота Василия на основе фактов: {VASYA_BIO}."

elif model_choice == "VasyaLyrics (Поэт)":
    st.subheader("Модель: VasyaLyrics")
    st.info("Поэт-песенник. Напишите ему слово, и он сочинит смешной стих про Васю.")
    system_prompt = f"Ты — поэт. Сочиняй забавные и смешные стихотворения с хорошей рифмой про кота Василия на основе его любви к пельменям, сну и кострам: {VASYA_BIO}."

elif model_choice == "CanvasVasya (Арт)":
    st.subheader("Модель: CanvasVasya")
    st.info("Генератор картинок. Здесь вы можете сгенерировать любое изображение с Васей.")
    
    user_prompt = st.text_input("Напишите сюжет для картинки (на английском, например: Cat near campfire):", "Cat eating dumplings near fire")
    
    if st.button("Сгенерировать арт"):
        if user_prompt:
            with st.spinner("Василий рисует..."):
                seed = int(time.time())
                encoded_prompt = urllib.parse.quote(f"fluffy brown tabby cat, green eyes, {user_prompt}, highly detailed, cute digital art")
                image_url = f"https://pollinations.ai{encoded_prompt}?width=512&height=512&seed={seed}&enhance=true"
                st.image(image_url, caption=f"Ваш арт по запросу: {user_prompt}")

# Работа чата через открытый бесплатный ИИ
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
