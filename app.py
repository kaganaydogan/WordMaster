from flask import Flask, render_template, request, redirect
import random
from models.word import Word
from models.quiz import Quiz

app = Flask(__name__)

words = []

correct_count = 0
wrong_count = 0

# words.txt dosyasından kelimeleri yükle
try:
    with open("words.txt", "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if "," in line:
                english, turkish = line.split(",")

                loaded_word = Word(english, turkish)

                words.append({
                    "english": loaded_word.get_english(),
                    "turkish": loaded_word.get_turkish()
                })

except:
    pass


@app.route("/")
def home():
    return render_template(
        "index.html",
        total_words=len(words)
    )


# Kayıtlı Tüm Kelimeleri Listele
@app.route("/words")
def show_words():
    return render_template(
        "words.html",
        words=words
        )

# Seçilen kelimeyi sil
@app.route("/delete/<english>")
def delete_word(english):

    global words

    words = [word for word in words if word["english"] != english]

    with open("words.txt", "w", encoding="utf-8") as file:
        for word in words:
            file.write(f"{word['english']},{word['turkish']}\n")

    return render_template(
        "words.html",
        words=words
    )

# Kelime quiz sistemi
@app.route("/quiz", methods=["GET", "POST"])
def quiz():

    global correct_count, wrong_count

    if len(words) == 0:
        return render_template("empty_words.html")

    quiz_system = Quiz(words)
    random_word = quiz_system.get_random_word()

    total_questions = correct_count + wrong_count
    # Başarı oranını hesapla
    if total_questions > 0:
        success_rate = int((correct_count / total_questions) * 100)
    else:
        success_rate = 0

    if request.method == "POST":

        # Kullanıcının cevabını al
        answer = request.form.get("answer")
        correct_answer = request.form.get("correct_answer")
        
        if answer and answer.lower().strip() == correct_answer.lower().strip():
            correct_count += 1
            result = "✅ Doğru!"
        else:
            wrong_count += 1
            result = f"❌ Yanlış! Doğru cevap: {correct_answer}"

        total_questions = correct_count + wrong_count

        if total_questions > 0:
            success_rate = int((correct_count / total_questions) * 100)
        else:
            success_rate = 0

        return render_template(
            "quiz.html",
            word=random_word,
            result=result,
            correct_count=correct_count,
            wrong_count=wrong_count,
            success_rate=success_rate
        )

    return render_template(
        "quiz.html",
        word=random_word,
        result="",
        correct_count=correct_count,
        wrong_count=wrong_count,
        success_rate=success_rate
    )

@app.route("/reset_stats")
def reset_stats():

    global correct_count, wrong_count

    correct_count = 0
    wrong_count = 0

    return redirect("/quiz")

# Yeni kelime ekleme işlemi
@app.route("/add", methods=["GET", "POST"])
def add_word():

    if request.method == "POST":

        english = request.form.get("english")
        turkish = request.form.get("turkish")

        # Aynı kelimeyi tekrar eklemeyi engelle
        for word in words:
            if word["english"].lower() == english.lower():

                return render_template(
                    "add_word.html",
                    success=False,
                    error="Bu kelime zaten kayıtlı!"
                )

        try:

            new_word = Word(english, turkish)

            words.append({
                "english": new_word.get_english(),
                "turkish": new_word.get_turkish()
            })

            with open("words.txt", "a", encoding="utf-8") as file:
                file.write(f"{english},{turkish}\n")

            return render_template(
                "add_word.html",
                success=True,
                error=""
            )

        except Exception as e:
            return f"Hata oluştu: {e}"

    return render_template(
        "add_word.html",
        success=False,
        error=""
    )


if __name__ == "__main__":
    app.run(debug=True)