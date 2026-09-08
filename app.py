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

# Профессиональная функция для связи с ИИ через официальный бесплатный сервер Hugging Face
def ask_free_ai(system_prompt, user_question):
    try:
        # Формируем четкую структуру для ИИ
        full_prompt = f"<|system|>\n{system_prompt}\n<|user|>\n{user_question}\n<|assistant|>\n"
        
        # Используем стабильный публичный API без ключей
        payload = {
            "inputs": full_prompt,
            "parameters": {"max_new_tokens": 250, "temperature": 0.7}
        }
        response = requests.post(
            "https://huggingface.co",
            json=payload,
            timeout=10
        )
        
        if response.status_code == 200:
            res_json = response.json()
            output = res_json[0]['generated_text']
            # Отрезаем промпт, чтобы показать только чистый ответ ИИ
            clean_answer = output.split("<|assistant|>\n")[-1].strip()
            return clean_answer
        else:
            # Резервный сервер, если основной перегружен
            encoded_text = urllib.parse.quote(f"{system_prompt}. Ответь на вопрос: {user_question}")
            fallback_res = requests.get(f"https://pollinations.ai{encoded_text}?model=mistral", timeout=10)
            if fallback_res.status_code == 200:
                return fallback_res.text
            return "Мяу! Я умываюсь лапкой. Нажми кнопку еще раз, я обязательно отвечу!"
    except:
        return "Мяу! Нажми отправить еще раз, связь с кошачьим космосом восстанавливается!"

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
    system_prompt = f"Ты — сам кот Василий. Твои факты: {VASYA_BIO}. Отвечай лениво, гордо, по-королевски на русском языке. Всегда вставляй 'мяу' и требуй пельмени."

elif model_choice == "VasyaExpert (Вопросы)":
    st.subheader("Модель: VasyaExpert")
    st.info("Технический эксперт по Василию. Ответит на любые вопросы о его рационе, привычках и здоровье.")
    system_prompt = f"Ты — эксперт по коту Василию. Используй только эти реальные факты: {VASYA_BIO}. Отвечай информативно, четко, строго на русском языке."

elif model_choice == "VasyaAI (Энциклопедия)":
    st.subheader("Модель: VasyaAI")
    st.info("Официальная вежливая модель. Рассказывает гостям сайта биографию и историю Василия.")
    system_prompt = f"Ты — вежливый ИИ-гид 'VasyaAI'. Расскажи красиво про кота Василия на основе фактов: {VASYA_BIO}. Отвечай строго на русском языке."

elif model_choice == "VasyaLyrics (Поэт)":
    st.subheader("Модель: VasyaLyrics")
    st.info("Поэт-песенник. Напишите ему слово, и он сочинит смешной стих про Васю.")
    system_prompt = f"Ты — поэт. Сочиняй забавные и смешные стихотворения с хорошей рифмой про кота Василия на русском языке. Используй факты: {VASYA_BIO}."

elif model_choice == "CanvasVasya (Арт)":
    st.subheader("Модель: CanvasVasya")
    st.info("Генератор картинок. Вводите сюжеты на английском языке для идеального результата.")
    
    user_prompt = st.text_input("Напишите сюжет для картинки на английском:", "fluffy cat eating dumplings near campfire")
    
    # Чтобы на экране не было пустого сломанного квадрата, сразу формируем рабочую заставку
    seed = 42
    encoded_prompt = urllib.parse.quote(f"fluffy brown tabby cat, green eyes, {user_prompt}, digital art, cute style, highly detailed")
    image_url = f"https://pollinations.ai{encoded_prompt}?width=512&height=512&seed={seed}&nofeed=true"
    
    if st.button("Сгенерировать арт"):
        with st.spinner("Василий берет в лапы кисть..."):
            seed = int(time.time())
            image_url = f"https://pollinations.ai{encoded_prompt}?width=512&height=512&seed={seed}&nofeed=true"
            
    st.image(image_url, caption=f"Текущий арт: {user_prompt}")

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

