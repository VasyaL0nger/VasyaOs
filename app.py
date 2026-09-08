import streamlit as st
import urllib.parse
import time
import random

# Настройка страницы сайта
st.set_page_config(page_title="VasyaOS", page_icon="cat", layout="centered")

# База данных о Василии
VASYA_BIO = {
    "имя": "Василий (Вася)",
    "возраст": "5 лет",
    "порода": "Дворняжка",
    "еда": "Сухой корм и ПЕЛЬМЕНИ",
    "привычки": "Спит на кресле или кровати, греется у костра, гипнотизирует взглядом ради еды"
}

# Внутренний генератор кошачьих ответов (работает мгновенно и без сбоев)
def generate_local_response(model_type, user_text):
    text_lower = user_text.lower()
    
    # Интеллектуальный поиск ключевых слов в запросе
    if "пельмен" in text_lower or "еда" in text_lower or "кушать" in text_lower or "корм" in text_lower:
        return random.choice([
            "Мяу!!! Пельмени?! Ты сказал ПЕЛЬМЕНИ?! Мой розовый носик уже чует этот божественный запах! Бегу на кухню, включай газ!",
            "Мяу! За один пельмень я готов продать душу, забыть про сухой корм и разрешить тебе погладить мой пушистый живот. Неси скорее!",
            "Мяу... Ты дразнишь кошачьего короля? Если в твоих руках нет сочной пельмешки, мой гипнотический взгляд накажет тебя!"
        ])
        
    if "спать" in text_lower or "кресл" in text_lower or "кроват" in text_lower or "где" in text_lower:
        return random.choice([
            "Мяу... Кресло и кровать — это мои официальные королевские резиденции. Я пушистый, мне положено спать по 20 часов в сутки.",
            "Где я сплю? Исключительно на мягком кресле или по центру твоей кровати, чтобы тебе негде было лечь. Это кошачий закон. Мяу!",
            "Мяу. Сейчас я лениво потягиваюсь на кресле. Не отвлекай меня от этого важного государственного дела."
        ])
        
    if "костер" in text_lower or "тепл" in text_lower or "характер" in text_lower or "почему" in text_lower:
        return random.choice([
            "Мяу! Я обожаю тепло. Сидеть возле жаркого костра, греть свои полосатые бока и усы — это высшая степень кошачьего кайфа.",
            "Мяу... Мой характер мудрый и спокойный. Но только до тех пор, пока где-то рядом тепло или пахнет вкусной едой.",
            "У костра тепло, а я пушистый коричневый кот, который ценит уют. Мяу! Человек, подбрось дров в огонь!"
        ])

    # Если это модель Поэта (VasyaLyrics) или пользователь просит стих
    if model_type == "VasyaLyrics (Поэт)" or "стих" in text_lower or "рифм" in text_lower or "песн" in text_lower:
        rhymes = [
            f"Кот Василий у костра\nГреет лапки до утра.\nДайте Васе пять пельменей —\nБудет счастлив он всегда! Мяу!",
            f"На подушке, на креслУ\nВася дрыхнет поутру.\nУ него усы из стали,\nМяу-мяу, мы устали!",
            f"Полосатый наш бандит\nНа кровати сладко спит.\nЕсли пельмешек учует —\nВмиг на кухню прилетит! Мяу!"
        ]
        return random.choice(rhymes)

    # Стандартные фразы для разных моделей, если ключевых слов нет
    if model_type == "VasyaTheCat (Болталка)":
        return random.choice([
            f"Мяу... Чего тебе, человек? Твой запрос '{user_input}' отвлекает меня от сна. Лучше почеши за ушком.",
            "Шшш... Я ленивый кошачий король. Мои зеленые глаза смотрят на тебя с легким презрением. Купи пельменей!",
            "Мои пушистые усы шевелятся от твоих слов. Но спать на кровати всё равно интереснее. Мяу."
        ])
    elif model_type == "VasyaExpert (Вопросы)":
        return random.choice([
            f"Экспертная справка: Кот Василий (возраст: {VASYA_BIO['возраст']}, дворняжка). Особые навыки: гипноз, выпрашивание пельменей.",
            f"Технический анализ: Объект пушистый, коричнево-полосатый. Главные точки базирования: кресло и кровать."
        ])
    else:
        return random.choice([
            f"Энциклопедия VasyaAI: Василий — 5-летний полосатый кот, легендарный ценитель костров, уюта и пельменей.",
            "Официальные хроники: Вася имеет зеленые глаза, розовый носик, роскошные белые усы и харизматичный характер."
        ])


# Шапка сайта
st.title("VasyaOS — Интеллектуальная Система Кота Василия")
st.write("Добро пожаловать в мультимодельную систему, посвященную коту Василию.")

# Боковая панель для выбора моделей
st.sidebar.header("🤖 Доступные модели")
model_choice = st.sidebar.selectbox(
    "Выберите модель для работы:",
    ["VasyaTheCat (Болталка)", "VasyaExpert (Вопросы)", "VasyaAI (Энциклопедия)", "VasyaLyrics (Поэт)", "CanvasVasya (Арт)"]
)

# Настройка интерфейса под модели
if model_choice == "VasyaTheCat (Болталка)":
    st.subheader("Модель: VasyaTheCat")
    st.info("Василий общается лично с вами. Он ленив, слегка высокомерен, отвечает как кошачий король, обожает пельмени.")

elif model_choice == "VasyaExpert (Вопросы)":
    st.subheader("Модель: VasyaExpert")
    st.info("Технический эксперт по Василию. Ответит на любые вопросы о его рационе, привычках и здоровье.")

elif model_choice == "VasyaAI (Энциклопедия)":
    st.subheader("Модель: VasyaAI")
    st.info("Официальная вежливая модель. Рассказывает гостям сайта биографию и историю Василия.")

elif model_choice == "VasyaLyrics (Поэт)":
    st.subheader("Модель: VasyaLyrics")
    st.info("Поэт-песенник. Напишите ему слово, и он сочинит смешной стих про Васю.")

elif model_choice == "CanvasVasya (Арт)":
    st.subheader("Модель: CanvasVasya")
    st.info("Генератор картинок. Вводите сюжеты строго на английском языке для идеального результата!")
    
    user_prompt = st.text_input("Напишите сюжет для картинки на английском:", "cat near campfire")
    
    # Кэшируем генерацию артов, чтобы они обновлялись только по кнопке
    if 'art_seed' not in st.session_state:
        st.session_state.art_seed = 42
    if 'current_prompt' not in st.session_state:
        st.session_state.current_prompt = "cat near campfire"

    if st.button("Сгенерировать арт"):
        st.session_state.art_seed = int(time.time())
        st.session_state.current_prompt = user_prompt

    encoded_prompt = urllib.parse.quote(f"fluffy brown tabby cat, green eyes, {st.session_state.current_prompt}, digital art, cute style, highly detailed")
    image_url = f"https://image.pollinations.ai/p/{encoded_prompt}?width=512&height=512&seed={st.session_state.art_seed}&nofeed=true"
    
    st.image(image_url, caption=f"Арт по запросу: {st.session_state.current_prompt}")

# Работа чата для текстовых моделей
if model_choice != "CanvasVasya (Арт)":
    user_input = st.text_input("Напишите ваше сообщение для ИИ:")
    
    if st.button("Отправить"):
        if user_input:
            with st.spinner("Василий думает..."):
                time.sleep(0.4) # Быстрая имитация кошачьих мыслей
                ai_response = generate_local_response(model_choice, user_input)
                st.write("---")
                st.write(f"**Вы:** {user_input}")
                st.write("**VasyaOS:**")
                st.success(ai_response)
