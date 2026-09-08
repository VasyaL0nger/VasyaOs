import streamlit as st
import urllib.parse
import time
import re

# Настройка страницы сайта
st.set_page_config(page_title="VasyaOS", page_icon="cat", layout="centered")

# --- БАЗА ЗНАНИЙ ДЛЯ ОБУЧЕНИЯ МОДЕЛИ (Вы можете её дополнять!) ---
# Сюда мы пишем все факты про Васю. Чем больше фактов, тем умнее ИИ.
VASYA_DATA = {
    "имя": "Кота зовут Василий, сокращенно Вася. Полное имя — Василий Королевский.",
    "возраст": "Василию сейчас 5 лет. По человеческим меркам он зрелый и солидный мужчина.",
    "порода": "Вася — гордая дворняжка. Самая умная, преданная и харизматичная порода в мире.",
    "внешность": "Василий очень пушистый. У него красивый коричнево-серый окрас с темными тигровыми полосками, выразительные зеленые глаза, аккуратный розовый носик с темным контуром и роскошные длинные белые усы.",
    "характер": "Вася ленивый, гордый и очень мудрый. Он настоящий ценитель комфорта и спокойствия.",
    "костер": "Василий безумно любит тепло! Его коронное увлечение — лежать возле костра, греть свои пушистые полосатые бока и смотреть на огонь. Также любит греться у батареи.",
    "пельмени": "Пельмени — это главная страсть Василия! За один сочный пельмень он готов продать душу, забыть про сухой корм и разрешить хозяину почесать свой живот. Он буквально сходит от них ума.",
    "еда": "Основной рацион Васи — это качественный сухой корм. Но его тайная любовь — это пельмени и колбаса, которые он мастерски выпрашивает.",
    "привычки": "У Василия королевские привычки. Спит он исключительно на мягком кресле или по центру хозяйской кровати. Утром может устроить легкий 'тыгыдык', если миска пуста.",
    "гипноз": "Вася владеет навыком гипноза. Когда он хочет есть, он садится напротив человека и начинает смотреть на него гипнотическим, глубоким взглядом, пока ему не дадут еду."
}

# --- ИНТЕЛЛЕКТУАЛЬНЫЙ ДВИЖОК VASYA-CORE ---
def ask_vasya_os(model_type, user_text):
    text_lower = user_text.lower()
    
    # Очищаем текст от знаков препинания
    words = re.findall(r'\b[а-я0-яa-z0-9]+\b', text_lower)
    
    # Ищем совпадения ключевых слов с нашей базой знаний
    found_facts = []
    for key, fact_text in VASYA_DATA.items():
        if key in text_lower or any(word[:4] in key for word in words if len(word) > 4):
            found_facts.append(fact_text)
            
    # Дополнительные синонимы для более точного обучения
    if "кушать" in text_lower or "корм" in text_lower or "колбас" in text_lower:
        found_facts.append(VASYA_DATA["еда"])
    if "выглядит" in text_lower or "глаза" in text_lower or "усы" in text_lower or "нос" in text_lower or "красив" in text_lower:
        found_facts.append(VASYA_DATA["внешность"])
    if "где спит" in text_lower or "кроват" in text_lower or "кресл" in text_lower:
        found_facts.append(VASYA_DATA["привычки"])

    # Убираем дубликаты найденных фактов
    found_facts = list(set(found_facts))

    # Формируем ответ в зависимости от выбранной модели
    if model_type == "VasyaTheCat (Болталка)":
        if found_facts:
            main_info = " ".join(found_facts)
            return f"Мяу! Слышь, человек... Напрягаешь мой кошачий мозг. Но так и быть, скажу: {main_info} Короче, ты понял. А теперь неси пельмени, я пошел спать на кресло! Мяу."
        else:
            return "Мяу... Чего тебе? Твой вопрос слишком сложный для кота. Напиши слова попроще — например, спроси меня про пельмени, костер, мои усы или где я сплю. Мяу!"

    elif model_type == "VasyaExpert (Вопросы)":
        if found_facts:
            return "📋 [VasyaExpert Аналитика]: " + " ".join(found_facts)
        else:
            return "📋 [VasyaExpert]: В базе данных нет точной информации по вашему запросу. Задайте вопрос о рационе, возрасте, породе, внешности или привычках объекта Василий."

    elif model_type == "VasyaAI (Энциклопедия)":
        if found_facts:
            return "ℹ️ [VasyaAI Справка]: Рады сообщить вам следующие подтвержденные факты: " + " ".join(found_facts)
        else:
            return "ℹ️ [VasyaAI]: Добро пожаловать. Я официальная модель VasyaAI. Вы можете спросить меня: 'Кто такой Вася?', 'Какая у него порода?' или 'Сколько ему лет?'"

    elif model_type == "VasyaLyrics (Поэт)":
        # Модель поэта генерирует стихи на основе найденной темы
        if "пельмен" in text_lower or "еда" in text_lower:
            return "🎵 [VasyaLyrics Рифма]:\n\nКот Василий на кровати сладко-сладко спал,\nЗапах жареных пельменей ухом услыхал!\nВмиг включил он свой гипноз, лапы задрожали,\nПринесите ИИ еду, чтобы мы не ждали!"
        elif "костер" in text_lower or "тепл" in text_lower:
            return "🎵 [VasyaLyrics Рифма]:\n\nВозле жаркого костра Вася греет бок,\nОн пушистый и крутой, в уюте знает толк.\nУсы белые горят, зеленые глаза,\nПро такого мудреца позабыть нельзя!"
        else:
            return "🎵 [VasyaLyrics Рифма]:\n\nНаш Василий — кот крутой, у него усы волной,\nСпит на кресле, видит сны, ждет пельмешек и весны!\nНапиши мне про костер или про еду,\nЯ еще один стишок для тебя найду!"


# --- ИНТЕРФЕЙС САЙТА ---
st.title("🐾 VasyaOS — Интеллектуальная Система Кота Василия")
st.write("Добро пожаловать в мультимодельную систему, посвященную коту Василию.")

# Боковая панель для выбора моделей
st.sidebar.header("🤖 Доступные модели")
model_choice = st.sidebar.selectbox(
    "Выберите модель для работы:",
    ["VasyaTheCat (Болталка)", "VasyaExpert (Вопросы)", "VasyaAI (Энциклопедия)", "VasyaLyrics (Поэт)", "CanvasVasya (Арт)"]
)

# Описание моделей на экране
if model_choice != "CanvasVasya (Арт)":
    st.subheader(f"Модель: {model_choice.split(' ')[0]}")
    user_input = st.text_input("Введите ваш вопрос или фразу для ИИ:")
    
    if st.button("Отправить запрос"):
        if user_input:
            with st.spinner("VasyaOS обрабатывает данные..."):
                time.sleep(0.4)  # Имитация работы процессора
                response = ask_vasya_os(model_choice, user_input)
                st.write("---")
                st.write(f"**Вы:** {user_input}")
                st.write(f"**VasyaOS ({model_choice.split(' ')[0]}):**")
                st.success(response)

else:
    st.subheader("Модель: CanvasVasya")
    st.info("Генератор картинок. Вводите сюжеты строго на английском языке.")
    user_prompt = st.text_input("Напишите сюжет для картинки (например: cat near fire):", "cat eating dumplings near campfire")
    
    if 'art_seed' not in st.session_state: st.session_state.art_seed = 42
    if 'current_prompt' not in st.session_state: st.session_state.current_prompt = "cat near campfire"

    if st.button("Сгенерировать арт"):
        st.session_state.art_seed = int(time.time())
        st.session_state.current_prompt = user_prompt

    encoded_prompt = urllib.parse.quote(f"fluffy brown tabby cat, green eyes, {st.session_state.current_prompt}, digital art, cute style, highly detailed")
    image_url = f"https://pollinations.ai{encoded_prompt}?width=512&height=512&seed={st.session_state.art_seed}&nofeed=true"
    st.image(image_url, caption=f"Арт по запросу: {st.session_state.current_prompt}")

