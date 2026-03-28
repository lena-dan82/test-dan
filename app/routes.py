from flask  import render_template, request, redirect, url_for
from app import app

posts = []

@app.route("/", methods=["GET", "POST"])
def index():
#использует метод POST, так как информация будет отправляться. Request method сравнивает данные с HTTP-запросом.
    if request.method == 'POST':
    #функция request.form извлекает значение из соответствующих полей
        title = request.form.get('title')
        sity = request.form.get('sity')
        hobby = request.form.get('hobby')
        age = request.form.get('age')
        #создаёт условие для проверки наличия данных в полях title и content
        if title and sity:
            posts.append({'title': title, 'sity': sity, 'hobby': hobby, 'age': age})
            #использует для обновления страницы и предотвращения повторной отправки формы.
            return redirect(url_for('index'))
    #возвращает отрендеренный шаблон с переданными данными постов
    return render_template('blog.html', posts=posts)

