import streamlit as st
import urllib.parse
import time
import random
import re

# Настройка страницы сайта
st.set_page_config(page_title="VasyaIQ", page_icon="cat", layout="centered")

# --- БОЛЬШОЙ МАССИВ ТЕКСТА ДЛЯ ОБУЧЕНИЯ ВНУТРЕННЕГО РАЗУМА ---
TRAINING_TEXT = """
Кот Василий Вася дворняжка 5 лет пушистый коричнево-серый полосатый зеленые глаза розовый носик белые усы.
Вася обожает пельмени сухой корм колбасу греться у костра спать на кресле на кровати.
Мяу хозяин неси скорее пельмени я продам душу за пельмешки сухой корм мне надоел.
Я ленивый кошачий король мои зеленые глаза смотрят на тебя свысока почеши за ушком.
Мои пушистые усы шевелятся когда я чую запах еды на кухне неси колбасу.
Сплю я по-королевски на мягком кресле или по центру твоей кровати чтобы тебе негде было лечь.
Я включаю свой гипнотический взгляд и гипноз заставляет людей открывать холодильник.
Кот Василий у костра греет лапки до утра дайте Васе пять пельменей будет счастлив он всегда мяу.
На подушке на креслу Вася дрыхнет поутру у него усы из стали мяу-мяу мы устали.
Полосатый наш бандит на кровати сладко спит если пельмешек учует вмиг на кухню прилетит.
Официальный ответ системы Кот Василий имеет возраст 5 лет порода дворняжка харизма сто процентов.
Технический анализ объект пушистый полосатый основные точки базирования кресло кровать костер.
Хроники VasyaIQ Василий легендарный ценитель костров уюта тепла батареи в теплице.
За один сочный пельмень я разрешу тебе погладить мой пушистый живот но не долго мяу.
"""

# --- ГЕНЕРАТИВНЫЙ ДВИЖОК VASYA-CORE ---
def train_and_generate_text(seed_word, max_words=20):
    # Очищаем и разбиваем текст на отдельные слова
    words = re.findall(r'\b[а-яА-Яa-zA-Z0-9-]+\b', TRAINING_TEXT.lower())
    
    # Строим карту связей между словами (обучаем модель)
    word_dict = {}
    for i in range(len(words) - 1):
        current_word = words[i]
        next_word = words[i+1]
        if current_word not in word_dict:
            word_dict[current_word] = []
        word_dict[current_word].append(next_word)
    
    # Начинаем строить новое уникальное предложение
    seed = seed_word.lower()
    if seed not in word_dict:
        # Если слова пользователя нет в базе, выбираем случайное кошачье слово
        seed = random.choice(["вася", "пельмени", "мяу", "костер", "кресле", "усы"])
        
    generated_words = [seed.capitalize() if seed != "я" else "Я"]
    current = seed
    
    for _ in range(max_words - 1):
        if current in word_dict and word_dict[current]:
            next_w = random.choice(word_dict[current])
            generated_words.append(next_w)
            current = next_w
            # Естественная остановка предложения на ключевых словах
            if current in ["мяу", "всегда", "утра", "прилетит", "процентов"]:
                break
        else:
            break
            
    return " ".join(generated_words) + "!"

# Распределение ответов по выбранным на сайте моделям
def ask_vasya_iq(model_type, user_text):
    words = re.findall(r'\b[а-яА-Я0-9]+\b', user_text.lower())
    
    # Ищем, за какое ключевое слово зацепиться генератору
    seed_word = "вася"
    for w in words:
        if w in ["пельмени", "костер", "спать", "усы", "кресло", "кровать", "еда", "кто", "порода", "возраст"]:
            seed_word = w
            break

    # Запускаем генерацию уникальной мысли
    generated_story = train_and_generate_text(seed_word, max_words=25)

    if model_type == "VasyaTheCat (Болталка)":
        return f"Мяу... Слушай сюда, человек: {generated_story} Короче, ты понял. А теперь тащи пельмень!"
    elif model_type == "VasyaExpert (Вопросы)":
        return f"📋 [VasyaIQ Expert]: Логи системы обработаны. Выдаю результат: {generated_story}"
    elif model_type == "VasyaAI (Энциклопедия)":
        return f"ℹ️ [VasyaIQ Энциклопедия]: Подтвержденная историческая хроника: {generated_story}"
    elif model_type == "VasyaLyrics (Поэт)":
        # Форматируем сгенерированный текст в красивый стих из двух строчек
        lines = generated_story.replace("!", "").split()
        if len(lines) >= 6:
            return f"🎵 [VasyaIQ Поэт]:\n\n{' '.join(lines[:3])},\n{' '.join(lines[3:6])}.\nМяу!"
        else:
            return f"🎵 [VasyaIQ Поэт]:\n\n{generated_story}\n(Вот такая кошачья рифма!)"

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
            with st.spinner("VasyaIQ генерирует уникальный ответ..."):
                time.sleep(0.3)
                response = ask_vasya_iq(model_choice, user_input)
                st.write("---")
                st.write(f"**Вы:** {user_input}")
                st.write(f"**VasyaIQ:**")
                st.success(response)

else:
    st.subheader("Модель: CanvasVasya")
    st.info("Генератор картинок. Вводите сюжеты строго на английском языке!")
    user_prompt = st.text_input("Напишите сюжет для картинки на английском:", "cat near campfire")
    
    if 'art_seed' not in st.session_state: st.session_state.art_seed = 42
    if 'current_prompt' not in st.session_state: st.session_state.current_prompt = "cat near campfire"

    if st.button("Сгенерировать арт"):
        st.session_state.art_seed = int(time.time())
        st.session_state.current_prompt = user_prompt

    encoded_prompt = urllib.parse.quote(f"fluffy brown tabby cat, green eyes, {st.session_state.current_prompt}, digital art, cute style, highly detailed")
    image_url = f"https://pollinations.ai{encoded_prompt}?width=512&height=512&seed={st.session_state.art_seed}&nofeed=true"
    st.image(image_url, caption=f"Арт по запросу: {st.session_state.current_prompt}")
