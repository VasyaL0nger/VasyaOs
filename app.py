import streamlit as st
import urllib.parse
import time
import random

# Настройка страницы сайта
st.set_page_config(page_title="VasyaIQ", page_icon="cat", layout="centered")

# База знаний кота Василия
VASYA_INFO = {
    "имя": "Кота зовут Василий, сокращенно Вася. Полное королевское имя — Василий Королевский.",
    "возраст": "Василию ровно 5 лет. По человеческим меркам это самый сок, солидный и зрелый мужчина.",
    "порода": "Вася — гордая, невероятно умная и преданная дворняжка.",
    "внешность": "Он очень пушистый. Окрас коричнево-серый с темными тигровыми полосками, глаза глубокие зеленые, носик розовый с темной каемкой, а усы роскошные, длинные и белые.",
    "пельмени": "Пельмени — главная жизненная страсть Васи! За один пельмень он готов продать душу, забыть про корм и дать почесать живот.",
    "еда": "Обычно Вася ест сухой корм, но его тайная любовь — это сочные пельмени и краковская колбаса, которые он мастерски выпрашивает.",
    "костер": "Василий безумно любит тепло. Его коронная фишка — лежать возле жаркого костра, греть полосатые бока и медитировать на огонь.",
    "тепло": "Кот обожает уют. Помимо костра, его часто можно застать греющимся на теплой батарее или в теплице.",
    "спать": "У Василия королевские привычки. Спит он исключительно на мягком кресле или прямо по центру твоей кровати, чтобы тебе негде было лечь.",
    "гипноз": "Вася владеет искусством кошачьего гипноза. Он садится напротив человека и смотрит на него глубоким взглядом, пока тот в панике не отдаст еду."
}

# Внутренний ИИ-генератор ответов Vasya-Core 2.0
def ask_vasya_core(model_type, user_text):
    text_lower = user_text.lower()
    
    # 1. Поиск точного факта по ключевым словам
    matched_fact = None
    
    if "имя" in text_lower or "как зовут" in text_lower:
        matched_fact = VASYA_INFO["имя"]
    elif "лет" in text_lower or "возраст" in text_lower:
        matched_fact = VASYA_INFO["возраст"]
    elif "пород" in text_lower:
        matched_fact = VASYA_INFO["порода"]
    elif "выглядит" in text_lower or "усы" in text_lower or "глаза" in text_lower or "нос" in text_lower or "шерсть" in text_lower or "цвет" in text_lower:
        matched_fact = VASYA_INFO["внешность"]
    elif "пельмен" in text_lower:
        matched_fact = VASYA_INFO["пельмени"]
    elif "костер" in text_lower or "костра" in text_lower or "огн" in text_lower:
        matched_fact = VASYA_INFO["костер"]
    elif "тепло" in text_lower or "батаре" in text_lower or "теплиц" in text_lower:
        matched_fact = VASYA_INFO["тепло"]
    elif "спать" in text_lower or "спит" in text_lower or "кресл" in text_lower or "кроват" in text_lower:
        matched_fact = VASYA_INFO["спать"]
    elif "гипноз" in text_lower or "взгляд" in text_lower or "выпрашива" in text_lower:
        matched_fact = VASYA_INFO["гипноз"]
    elif "еда" in text_lower or "кушать" in text_lower or "корм" in text_lower or "колбас" in text_lower:
        matched_fact = VASYA_INFO["еда"]

    # Если точный факт не найден, берем случайную философскую фразу кота
    if not matched_fact:
        matched_fact = f"Твой запрос '{user_text}' заставил мои белые усы шевелиться. Но в моей кошачьей базе знаний нет точного ответа на это. Спроси меня лучше про мои 5 лет, пельмени, костер или усы!"

    # 2. Форматирование ответа под выбранную модель
    if model_type == "VasyaTheCat (Болталка)":
        return f"Мяу! Слушай сюда, человек. По поводу твоего вопроса скажу так: {matched_fact} Короче, ты понял. А теперь неси пельмени! Мяу."
        
    elif model_type == "VasyaExpert (Вопросы)":
        return f"📋 [VasyaIQ Expert]: Система обработала запрос. Найдена официальная выписка: \"{matched_fact}\""
        
    elif model_type == "VasyaAI (Энциклопедия)":
        return f"ℹ️ [VasyaIQ Энциклопедия]: Архивные хроники подтверждают информацию. {matched_fact}"
        
    elif model_type == "VasyaLyrics (Поэт)":
        # Умный поэт собирает разные стихи под разные ключевые слова!
        if "пельмен" in text_lower or "еда" in text_lower:
            return "🎵 [VasyaIQ Рэпер/Поэт]:\n\nКот Василий на кровати тихо-тихо спал,\nЗапах жареных пельменей ухом услыхал!\nВмиг включил он свой гипноз, лапы задрожали,\nПринесите Васе жратву, чтобы мы не ждали! Мяу!"
        elif "костер" in text_lower or "тепло" in text_lower:
            return "🎵 [VasyaIQ Рэпер/Поэт]:\n\nВозле жаркого костра Вася греет бок,\nОн пушистый и крутой, в уюте знает толк.\nУсы белые горят, зеленые глаза,\nПро такого мудреца позабыть нельзя! Мяу!"
        elif "спать" in text_lower or "кресло" in text_lower:
            return "🎵 [VasyaIQ Рэпер/Поэт]:\n\nНа подушке, на креслУ Вася дрыхнет поутру,\nСпит по двадцать пять часов, предан он сну.\nУ него усы из стали, лапы — чистый пух,\nПолосатый наш король бодр и духом ух! Мяу!"
        else:
            return f"🎵 [VasyaIQ Рэпер/Поэт]:\n\nНаш Василий — кот крутой, у него усы волной,\nМы читали про '{user_text}', но пельмешки — выбор мой!\nСпит на кресле, видит сны, ждет костра и ждет весны! Мяу!"

# --- ИНТЕРФЕЙС САЙТА ---
st.title("🐾 VasyaIQ — Интеллектуальная Система Кота Василия")
st.write("Добро пожаловать в вашу личную автономную мультимодельную систему!")

# Боковая панель для выбора моделей
st.sidebar.header("🤖 Доступные модели")
model_choice = st.sidebar.selectbox(
    "Выберите модель для работы:",
    ["VasyaTheCat (Болталка)", "VasyaExpert (Вопросы)", "VasyaAI (Энциклопедия)", "VasyaLyrics (Поэт)", "CanvasVasya (Арт)"]
)

# Работа чата для текстовых моделей
if model_choice != "CanvasVasya (Арт)":
    st.subheader(f"Модель: {model_choice}")
    user_input = st.text_input("Введите ваш вопрос или фразу для ИИ:")
    
    if st.button("Отправить запрос"):
        if user_input:
            with st.spinner("VasyaIQ ищет данные..."):
                time.sleep(0.2)
                response = ask_vasya_core(model_choice, user_input)
                st.write("---")
                st.write(f"**Вы:** {user_input}")
                st.write(f"**VasyaIQ:**")
                st.success(response)

else:
    st.subheader("Модель: CanvasVasya")
    st.info("Генератор картинок. Вводите сюжеты строго на английском языке!")
    user_prompt = st.text_input("Напишите сюжет для картинки на английском:", "cat eating dumplings near campfire")
    
    if 'art_seed' not in st.session_state: st.session_state.art_seed = 42
    if 'current_prompt' not in st.session_state: st.session_state.current_prompt = "cat near campfire"

    if st.button("Сгенерировать арт"):
        st.session_state.art_seed = int(time.time())
        st.session_state.current_prompt = user_prompt

    encoded_prompt = urllib.parse.quote(f"fluffy brown tabby cat, green eyes, {st.session_state.current_prompt}, digital art, cute style, highly detailed")
    image_url = f"https://pollinations.ai{encoded_prompt}?width=512&height=512&seed={st.session_state.art_seed}&nofeed=true"
    st.image(image_url, caption=f"Арт по запросу: {st.session_state.current_prompt}")

