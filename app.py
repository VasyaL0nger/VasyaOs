import streamlit as st
import urllib.parse
import time
import random

# Настройка страницы сайта
st.set_page_config(page_title="VasyaIQ", page_icon="cat", layout="centered")

# Данные о Василии (внутренний мозг системы)
VASYA_BIO = {
    "имя": "Василий (Вася), полное имя — Василий Королевский.",
    "возраст": "5 лет (зрелый, солидный кошачий возраст).",
    "порода": "Благородная, преданная и очень умная дворняжка.",
    "внешность": "Пушистый красавец, коричнево-серый окрас с темными тигровыми полосками, зеленые гипнотизирующие глаза, розовый носик с темным контуром и роскошные белые усы.",
    "еда": "Основной рацион — сухой корм, но за сочные ПЕЛЬМЕНИ и краковскую колбасу готов продать душу.",
    "привычки": "Спит исключительно на мягком кресле или по центру хозяйской кровати. Обожает греться у костра. Мастерски гипнотизирует взглядом ради еды."
}

# Внутренний лингвистический процессор кошачьего разума
def generate_smart_response(model_type, user_text):
    text_lower = user_text.lower()
    
    # Списки фраз по темам запроса
    greetings = ["Мяу! Ну привет, человек.", "Лениво приоткрываю один зеленый глаз... Привет.", "Мяу. Ты потревожил кошачьего короля. Чего тебе?"]
    food_thoughts = [
        f"Ты говоришь '{user_text}', а в моем пушистом животе заурчало. Напоминаю: моя любимая еда — {VASYA_BIO['еда']}. Живо беги на кухню!",
        "Мои белые усы дрожат, когда заходит речь о еде! Особенно про ПЕЛЬМЕНИ. Включаю гипноз, открывай холодильник!",
        "Мяу! За сочную пельмешку я готов выслушать любые твои истории. Неси скорее, сухой корм мне надоел."
    ]
    sleep_thoughts = [
        f"Мои королевские привычки просты: {VASYA_BIO['привычки']} Сейчас я как раз занимаю лучшее место!",
        "Где я сплю? На кресле или прямо по центру твоей кровати, чтобы тебе негде было лечь. Это кошачий закон. Мяу.",
        "Мяу... Лежать на мягком кресле — мое главное государственное дело. Не отвлекай от созерцания снов."
    ]
    warm_thoughts = [
        "Обожаю тепло! Сидеть у жаркого костра, греть полосатые бока и смотреть на искры — это высший кайф. Подбрось дров! Мяу.",
        "Теплица, батарея, костер — если там тепло, значит там я. Я пушистый коричневый кот и знаю толк в уюте.",
        "Мяу. Мой характер мудрый и спокойный, пока я греюсь в теплом местечке у огня. Не создавай сквозняков!"
    ]
    bio_thoughts = [
        f"Слушай и запоминай: мое имя Василий, мне {VASYA_BIO['возраст']} По породе я {VASYA_BIO['порода']}",
        f"Моя внешность безупречна: {VASYA_BIO['внешность']} Настоящий тигр, только маленький и домашний. Мяу!"
    ]
    philosophy = [
        f"Твой запрос '{user_text}' заставил мои белые усы шевелиться. С высоты моих 5 лет скажу: всё это суета. Лучше дай пельмень.",
        "Мяу... Человеческие проблемы такие странные. Вот у котов всё просто: поспал на кресле, погрелся у костра, поел. Бери с меня пример!",
        f"Я лениво машу хвостом на твое '{user_text}'. Как мудрая дворняжка, я выше этого. Но если принесешь колбасы, мы договоримся."
    ]

    # Логика анализа текста (Определяем тему по ключевым словам)
    chosen_pool = philosophy  # По умолчанию кот просто философствует
    
    if any(word in text_lower for word in ["привет", "здравствуй", "хай", "ку", "здорово"]):
        chosen_pool = greetings
    elif any(word in text_lower for word in ["пельмен", "еда", "кушать", "корм", "колбас", "голод"]):
        chosen_pool = food_thoughts
    elif any(word in text_lower for word in ["спать", "кресло", "кровать", "лежать", "сон"]):
        chosen_pool = sleep_thoughts
    elif any(word in text_lower for word in ["костер", "тепло", "батарея", "огонь", "уют", "теплиц"]):
        chosen_pool = warm_thoughts
    elif any(word in text_lower for word in ["кто", "порода", "возраст", "лет", "внешность", "усы", "глаза", "имя", "как выглядит"]):
        chosen_pool = bio_thoughts

    # Формируем ответ строго под стиль выбранной модели
    raw_answer = random.choice(chosen_pool)
    
    if model_type == "VasyaTheCat (Болталка)":
        return f"{raw_answer} Мяу!"
        
    elif model_type == "VasyaExpert (Вопросы)":
        clean_fact = raw_answer.replace("Мяу!", "").replace("Мяу...", "").strip()
        return f"📋 [VasyaIQ Expert]: Логи системы обработаны. Экспертная выписка по запросу: {clean_fact}"
        
    elif model_type == "VasyaAI (Энциклопедия)":
        clean_fact = raw_answer.replace("Мяу!", "").strip()
        return f"ℹ️ [VasyaIQ Энциклопедия]: Официально подтвержденные хроники кота Василия. {clean_fact}"
        
    elif model_type == "VasyaLyrics (Поэт)":
        # Генерируем уникальное стихотворение на ходу
        rhymes = [
            f"Ты написал мне: '{user_text}',\nА я лежу, засунув нос в буфет.\nХочу пельмешек у костра поесть,\nВедь для кота дороже счастья нет! Мяу!",
            f"На кресле Вася сладко спит,\nТвое '{user_text}' в усах звенит.\nНо если принесешь еду —\nЯ вмиг к пельменям прибегу!",
            f"Зеленые глаза глядят в упор,\nВедем мы про '{user_text}' разговор.\nМне пять летков, усы горят,\nПельмени — радость для котят!"
        ]
        return f"🎵 [VasyaIQ Поэт]:\n\n{random.choice(rhymes)}"

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
                response = generate_smart_response(model_choice, user_input)
                st.write("---")
                st.write(f"**Вы:** {user_input}")
                st.write(f"**VasyaIQ:**")
                st.success(response)

else:
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

