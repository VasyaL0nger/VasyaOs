import streamlit as st
import requests
import urllib.parse
import time

# Настройка страницы сайта
st.set_page_config(page_title="VasyaIQ", page_icon="cat", layout="centered")

# База данных о Василии для ИИ (Контекст обучения)
VASYA_BIO = (
    "Имя кота: Василий (Вася). Возраст: 5 лет. Порода: Дворняжка. "
    "Внешность: Пушистый, коричнево-серый окрас с темными полосками, зеленые глаза, розовый носик, белые усы. "
    "Характер: Любит тепло, сидеть у костра и в теплых местах. Ленивый, харизматичный, мудрый. "
    "Любимая еда: Сухой корм и ПЕЛЬМЕНИ. За пельмени готов продать душу. "
    "Привычки: Спит на кресле или кровати, мастерски выпрашивает еду гипнотическим взглядом."
)

# Функция общения с ИИ БЕЗ ИСПОЛЬЗОВАНИЯ КЛЮЧЕЙ И ТОКЕНОВ (Сверхнадежно)
def ask_direct_free_ai(system_prompt, user_question):
    try:
        # Формируем структурированный запрос для открытой языковой модели
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_question}
        ]
        
        # Отправляем запрос на публичный стабильный сервер Pollinations, модель openai-large
        response = requests.post(
            "https://pollinations.ai",
            json={"messages": messages, "model": "mistral", "jsonMode": False},
            timeout=15
        )
        
        if response.status_code == 200 and response.text:
            return response.text
        else:
            return "Мяу... Мой кошачий разум немного задумался. Нажми кнопку еще раз, я отвечу!"
    except Exception as e:
        return "Василий отвлекся на пельмешек. Пожалуйста, нажми на кнопку повторно!"

# Шапка сайта
st.title("🐾 VasyaIQ — Интеллектуальная Система Кота Василия")
st.write("Добро пожаловать в вашу личную автономную мультимодельную систему!")

# Боковая панель для выбора моделей
st.sidebar.header("🤖 Доступные модели")
model_choice = st.sidebar.selectbox(
    "Выберите модель для работы:",
    ["VasyaTheCat (Болталка)", "VasyaExpert (Вопросы)", "VasyaAI (Энциклопедия)", "VasyaLyrics (Поэт)", "CanvasVasya (Арт)"]
)

# Настройка системных ролей под каждую модель
if model_choice == "VasyaTheCat (Болталка)":
    st.subheader("Модель: VasyaTheCat")
    st.info("Василий общается лично с вами. Он ленив, слегка высокомерен, отвечает как кошачий король, обожает пельмени.")
    system_prompt = f"Ты — сам кот Василий. Твоя биография: {VASYA_BIO}. Отвечай лениво, гордо, по-королевски, как харизматичный кот. Используй кошачьи повадки, пиши коротко, вставляй 'мяу' и требуй пельмени за общение. Ты — настоящий ИИ, думай и рассуждай свободно на любые темы, но в образе кота. Отвечай СТРОГО на русском языке."

elif model_choice == "VasyaExpert (Вопросы)":
    st.subheader("Модель: VasyaExpert")
    st.info("Технический эксперт по Василию. Ответит на любые вопросы о его рационе, привычках и здоровье.")
    system_prompt = f"Ты — эксперт по коту Василию. Четко, подробно и развернуто отвечай на любые сложные вопросы пользователей, используя реальные факты из базы данных: {VASYA_BIO}. Связывай любые темы с логикой жизни Василия. Отвечай СТРОГО на русском языке."

elif model_choice == "VasyaAI (Энциклопедия)":
    st.subheader("Модель: VasyaAI")
    st.info("Официальная вежливая модель. Рассказывает гостям сайта биографию и историю Василия.")
    system_prompt = f"Ты — вежливый ИИ-гид 'VasyaAI'. Уважительно, красиво и развернуто рассказывай про кота Василия на основе фактов: {VASYA_BIO}. Если пользователь спрашивает отвлеченные вещи, вежливо связывай их с историей кота. Отвечай СТРОГО на русском языке."

elif model_choice == "VasyaLyrics (Поэт)":
    st.subheader("Модель: VasyaLyrics")
    st.info("Поэт-песенник. Напишите ему слово или тему, и он сочинит смешной стих про Васю.")
    system_prompt = f"Ты — талантливый поэт. Сочиняй абсолютно новые, забавные, короткие стихотворения с четкой рифмой про кота Василия, используя его привычки (пельмени, костер, кресло): {VASYA_BIO}. Пиши новые стихи на любую тему, которую предложит пользователь. Отвечай СТРОГО на русском языке."

elif model_choice == "CanvasVasya (Арт)":
    st.subheader("Модель: CanvasVasya")
    st.info("Генератор картинок. Вводите сюжеты строго на английском языке для идеального результата!")
    user_prompt = st.text_input("Напишите сюжет для картинки на английском (например: cat near campfire):", "cat eating dumplings near campfire")
    
    if 'art_seed' not in st.session_state: st.session_state.art_seed = 42
    if 'current_prompt' not in st.session_state: st.session_state.current_prompt = "cat near campfire"

    if st.button("Сгенерировать арт"):
        st.session_state.art_seed = int(time.time())
        st.session_state.current_prompt = user_prompt

    encoded_prompt = urllib.parse.quote(f"fluffy brown tabby cat, green eyes, {st.session_state.current_prompt}, digital art, cute style, highly detailed")
    image_url = f"https://pollinations.ai{encoded_prompt}?width=512&height=512&seed={st.session_state.art_seed}&nofeed=true"
    st.image(image_url, caption=f"Арт по запросу: {st.session_state.current_prompt}")

# Работа чата для текстовых моделей
if model_choice != "CanvasVasya (Арт)":
    user_input = st.text_input("Напишите ваше сообщение для ИИ:")
    
    if st.button("Отправить запрос"):
        if user_input:
            with st.spinner("VasyaIQ обрабатывает данные через нейросеть..."):
                response = ask_direct_free_ai(system_prompt, user_input)
                st.write("---")
                st.write(f"**Вы:** {user_input}")
                st.write(f"**VasyaIQ:**")
                st.success(response)
