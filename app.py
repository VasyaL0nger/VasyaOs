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

# Автономный генератор кошачьих ответов (работает без ключей и внешних серверов)
def generate_local_response(model_type, user_text):
    text_lower = user_text.lower()
    
    # Фразы для Болталки (VasyaTheCat)
    cat_phrases = [
        "Мяу... Чего тебе, человек? Твой вопрос отвлекает меня от сна на теплом кресле. Лучше неси пельмени!",
        "Шшш... Я ленивый кошачий король. Мои зеленые глаза смотрят на тебя свысока. Мяу!",
        "Ты что-то говоришь, но я слышу только 'купи Васе пельмешек'. Мяу, живо на кухню!",
        "Мои пушистые усы шевелятся от твоего сообщения. Но спать на кровати интереснее. Мяу.",
        "Мяу! Запомни: я дворняжка королевской крови, мне 5 лет, и я требую уважения и еды!"
    ]
    
    # Фразы для Эксперта (VasyaExpert)
    expert_phrases = [
        f"Официальный ответ системы: Кот Василий (порода {VASYA_BIO['порода']}) имеет возраст {VASYA_BIO['возраст']}. Главная слабость — {VASYA_BIO['еда']}.",
        f"Анализ привычек: Объект предпочитает спать на кресле или кровати. Обладает навыком гипноза.",
        f"Технические данные: Окрас коричнево-серый с полосками. Любимое место обогрева — у костра.",
        f"Справка по рациону: Сухой корм принимается регулярно, однако за ПЕЛЬМЕНИ кот готов продать душу."
    ]
    
    # Фразы для Энциклопедии (VasyaAI)
    ai_phrases = [
        f"Приветствуем вас! VasyaAI сообщает: Василий — 5-летний пушистый кот с зелеными глазами и белыми усами.",
        "Василий — уникальный представитель дворняжек, сочетающий в себе мудрость и любовь к уюту у костра.",
        "Исторический факт: Василий спит исключительно на мягких поверхностях (кресло, кровать) и мастерски выпрашивает еду.",
        f"Энциклопедия кота: Вася ценит тепло, имеет харизматичный характер и очень любит пельмени."
    ]

    # Интеллектуальный поиск ключевых слов в запросе пользователя
    if "пельмен" in text_lower or "еда" in text_lower or "кушать" in text_lower:
        return "Мяу!!! Пельмени?! Ты сказал ПЕЛЬМЕНИ?! Мой розовый носик уже чует запах! Неси скорее, или я применю гипнотический взгляд!"
    if "спать" in text_lower or "кресл" in text_lower or "кроват" in text_lower:
        return "Мяу... Кресло и кровать — это моя суверенная территория. Я пушистый, мне нужно спать по 20 часов в сутки."
    if "костер" in text_lower or "тепл" in text_lower:
        return "Мяу! Обожаю тепло. Сидеть возле костра или на теплой батарее — лучшее занятие для мудрого полосатого кота."
    if "стих" in text_lower or "поэт" in text_lower or model_type == "VasyaLyrics (Поэт)":
        rhymes = [
            f"Кот Василий у костра\nГреет лапки до утра.\nДайте Васе пять пельменей —\nБудет счастлив он всегда!",
            f"На подушке, на креслУ\nВася дрыхнет поутру.\nУ него усы из стали,\nМяу-мяу, мы устали!",
            f"Полосатый наш бандит\nНа кровати сладко спит.\nЕсли пельмешек учует —\nВмиг на кухню прилетит!"
        ]
        return random.choice(rhymes)

    # Если ключевых слов нет, выдаем случайную фразу по модели
    if model_type == "VasyaTheCat (Болталка)":
        return random.choice(cat_phrases)
    elif model_type == "VasyaExpert (Вопросы)":
        return random.choice(expert_phrases)
    else:
        return random.choice(ai_phrases)


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
    st.info("Генератор картинок. Вводите сюжеты на английском языке!")
    
    user_prompt = st.text_input("Напишите сюжет для картинки на английском (например: cat near fire):", "cat eating dumplings near campfire")
    
    # Кэшируем генерацию артов, чтобы картинки обновлялись только по нажатию кнопки
    if 'art_seed' not in st.session_state:
        st.session_state.art_seed = 42
    if 'current_prompt' not in st.session_state:
        st.session_state.current_prompt = "cat eating dumplings near campfire"

    if st.button("Сгенерировать арт"):
        st.session_state.art_seed = int(time.time())
        st.session_state.current_prompt = user_prompt

    encoded_prompt = urllib.parse.quote(f"fluffy brown tabby cat, green eyes, {st.session_state.current_prompt}, digital art, cute style, highly detailed")
    image_url = f"https://pollinations.ai{encoded_prompt}?width=512&height=512&seed={st.session_state.art_seed}&nofeed=true"
    
    st.image(image_url, caption=f"Арт по запросу: {st.session_state.current_prompt}")

# Работа чата для текстовых моделей
if model_choice != "CanvasVasya (Арт)":
    user_input = st.text_input("Напишите ваше сообщение для ИИ:")
    
    if st.button("Отправить"):
        if user_input:
            with st.spinner("Василий думает..."):
                time.sleep(0.5) # Имитация раздумий кота
                ai_response = generate_local_response(model_choice, user_input)
                st.write("---")
                st.write(f"**Вы:** {user_input}")
                st.write("**VasyaOS:**")
                st.success(ai_response)
