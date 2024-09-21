from time import sleep
class User:
    """
    Класс User. Аттрибуты: nickname(имя пользователя, строка), password(в хэшированном виде, число), age(возраст,
    число).
    Внимание: password должен иметь тип str, иначе функция hash() не работает!
    """

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return f"Имя пользователя: {self.nickname}, его возраст {self.age}, пароль {self.password}"

    def __repr__(self):
        return f"Пользователь (Nickname={self.nickname}, Age={self.age}, Password={self.password})\n"


class Video:
    """
    Класс Video. Атриубуты: title(заголовок, строка), duration(продолжительность, секунды), time_now(секунда остановки
    (изначально 0)), adult_mode(ограничение по возрасту, bool (False по умолчанию))
    """

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return f"Видео: {self.title}, продолжительность: {self.duration}"

    def __repr__(self):
        return (f"Title={self.title}, Duration={self.duration}, Time_now={self.time_now}, Adult_mode={self.adult_mode}")


class UrTube:
    """
    Класс UrTube. Содержит методы: log_in (вход в аккаунт), register (регистрации на сайте), log_out (выхода из
    аккаунта), add (добавления видео), get (поиск видео по ключевому слову), watch_video (воспроизведение видео).
    """

    #Атриубты: users(список объектов User), videos(список объектов Video), current_user(текущий пользователь, User)
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    # Метод log_in, который принимает на вход аргументы: nickname, password и пытается найти пользователя в users с
    # такими же логином и паролем. Если такой пользователь существует, то current_user меняется на найденного.

    def log_in(self, nickname, password):
        for user_input in self.users:
            if user_input.nickname == nickname and user_input.password == hash(password):
                self.current_user = user_input
                print(f"Вход успешно осуществлен")
                return
        print("Неверный логин или пароль")

    # Метод register, который принимает три аргумента: nickname, password, age, и добавляет пользователя в список, если
    # пользователя не существует (с таким же nickname). Если существует, выводит на экран: "Пользователь {nickname} уже
    # существует". После регистрации, вход выполняется автоматически.

    def register(self, nickname, password, age):
        for user_input in self.users:
             if user_input == nickname:
                print(f"Пользователь {nickname}, уже существует")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        print("Регистрация успешно осуществлена")
        self.current_user = new_user
        print("Вход осуществлен")

    # Метод log_out для сброса текущего пользователя на None.

    def log_out(self):
        self.current_user = None

    # Метод add, который принимает неограниченное кол-во объектов класса Video и все добавляет в videos, если с таким
    # же названием видео ещё не существует. В противном случае ничего не происходит.

    def add(self, *videos):
       for adding_video in videos:
           for element in self.videos:
               if adding_video.title in element.title:
                   print("Видео с таким названием уже существует")
                   return
           self.videos.append(adding_video)
           print(f"{adding_video} добавлено")

    # Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео, содержащих поисковое
    # слово. Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best' (не учитывать регистр).

    def get_videos(self, keyword: str):
        founded_video_list = []
        for element in self.videos:
            if keyword.lower() in element.title.lower():
                founded_video_list.append(element.title)
        if len(founded_video_list) > 0:
            return f"Результаты поиска: {founded_video_list}"
        else:
            return "По данному запросу ничего не найдено"

    # Метод watch_video, который принимает название фильма, если не находит точного совпадения(вплоть до пробела), то
    # ничего не воспроизводится, если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр.
    # После текущее время просмотра данного видео сбрасывается.

    def watch_video(self, title):
        if self.current_user == None:
            return print("Войдите в аккаунт, чтобы смотреть видео")

        for element in self.videos:
            if title == element.title:
                if self.current_user.age < 18 and element.adult_mode == True:
                    return print("Вам нет 18 лет, пожалуйста покиньте страницу")
                else:
                    while element.time_now < element.duration:
                        element.time_now += 1
                        print(element.time_now)
                        sleep(1)
                element.time_now = 0
                print("Конец видео")

if __name__ == "__main__":
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)
    #Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')

