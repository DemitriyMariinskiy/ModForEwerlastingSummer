﻿#####Отец--------------Николай Семенов. "Бес"
#####Протагонист-------Юлия Семенова Николаевна
#####Вредный профессор-Отто Штехель
#####
#####
#####
#####
#####
#####
#####
#####
#####


init:

    $ mods["MD_01"]=u"А как всё начиналось..."

    image Bolnichca = "mods/Images/BG/Bolnichca.jpg"
    image IHM = "mods/Images/BG/Int_House_Moscow.jpg"    
    
    
    $ UVAO = Character(u'Юля', color="#c600ff", ctc="ctc_animation", ctc_position="fixed", what_color="ffffff", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ DAD = Character(u'Отец', color="#ff0000", ctc="ctc_animation", ctc_position="fixed", what_color="ffffff", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ SH = Character(u'Профессор Штехель', color="#ff0054", ctc="ctc_animation", ctc_position="fixed", what_color="ffffff", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")







label MD_01:
    $ prolog_time()
    scene anim prolog_1 with dissolve
    "Дневник Юлии Семеновой.  2002 год."
    $ set_mode_nvl()
    scene IHM with dissolve
    "Моя история началась летом 2002 года." 
    "Я верю, что жизнь может дать каждому шанс на нечто большее, чем то, но что он может рассчитывать. {w}Читая художественные книжки, десятками раз пересматривая интересные фильмы, постепенно можно начать думать, что настоящая жизнь на фоне этого скучна, сера и неинтересна. {w}Дейтвительно, возможна ли в реальности хоть половина тех невероятных и фантастических событий, которые мы переживаем вместе с героями любимых произведений?"
    "Раньше я думала, что нет. {w}Судьба не баловала меня. Я закончила школу, поступила в один из лучших в России университетов по направлению генетики. {w}Казалось бы, разве это не здорово? {w}Здорово. {w}Только в этом нет ничего необычного. Это не вносит в мир тех красок, которых мне не хватает."
    "В детстве я лазела по заброшенным домам, по огородам ворчливых бабок: к некоторым за яблоками, а к другим просто чтобы позлить. {w}Хотя хулиганские компании, известные своими проделками на весь город- это в представлении всех мальчишки, я была заводилой в подобной девчачей банде. {w}Разве это не те самые приключения, а Юля?"
    "Да нет, ерунда. {w}Даже это наскучит со временем."
    "Теперь этот университет. {w}У меня в нем появилось несколько подруг, с которыми у нас на столько разные вкусы, что почти нет общих тем."
    nvl clear
    "Нашла любовь...{w}ну, то есть это мне так говорят. {w}На самом деле я ничего особенного не чувствую к этому человеку. {w}А может в любви ничего особенного и не чувсвуют? {w}Хотя нет. Маму я любила совсем по другому. И отца тоже люблю совсем не так."
    "В общем моя жизнь кажется мне довольно серой, хотя многие бы не поняли моих мыслей. И по этому я жду, пока случится нечто интересное."
    $ set_mode_adv()
    "Проблема только в том, что если вот так седеть на диватьчике, и жалеть себя бедную сама не знаю за что, то ничего и не изменится."
    "Из размышлений меня вывел скрип замка. Отец пришел с вокзала."
    "Мой отец - телохранитель, бывший ЧОПовец, вернулся из командировки, и ему тут же предложили работу."
    "Я редко интересуюсь его делами, да и когда спрошу-молчит. Бывает, буркнет что-нибудь себе под нос, а так мол говорить не велено."
    "Но сегодня он начал разговор первым. {w}Я сидела в комнате, читала {i}занимательную биологию{/i}, когда он позвал меня к себе."
    DAD "Дочка моя, как твои экзамены?"
    UVAO "Нормально, пап. Я сдала уже всё, теперь можно рассчитывать на неплохую работу."
    "Он редко интересуется моими успехами. Странно, что он расспрашивает меня об успехах. Однако я всегда старалась ценить подобные минуты разговоров по душам."
    DAD "Я понимаю; у тебя были планы, ты училась с подругами, хотела и работать с ними. Да и девочка ты уже взрослая, решаешь свою судьбу сама."
    "Я напрягла слух. Разговор будет серьезным,это я поняла сразу."
    DAD "Мне предложили работу. Весьма необычную работу. Завтра я уезжаю."
    UVAO "Необычную? Это как? Охранять спутник на орбите?"
    "Забыла сказать, что я очень люблю шутить."
    DAD "Нет. На орбиту я лететь отказался. Вместо этого мне предложили быть охранником на секретном объекте. "
    UVAO "И раз ты мне об этом сказал, значит мне что-то с этого будет?"
    DAD "Я устроился туда благодаря огромному послужному списку, и по знакомству там."
    "Он поднял палец к небу, таким образом показывая знакомство с каким-нибудь министром или генералом."
    DAD "Это своего рода полигон, на котором будут проводить какие-то испытания. Я не интересовался. Работа у меня дочка такая-молчать."
    "Он выдержал драматическую паузу, сглотнул и продолжил."
    DAD "И я могу, так же через этих знакомых, устроить тебя туда. Думаю, это встряхнет твою жизнь. Ты же хотеля чего-то необычного?"
    UVAO "Но как ты все устроишь? И потом, это же секретный объект!"
    DAD "Не волнуйся, устроить я могу. А вот секретный-это дааа."
    "Я насторожилась еще сильнее, кажется даже вспотела."
    DAD "В общем так: правительственная собственность. Платить будут соответственно хорошо. Это очень интересно-гарантирую. А условие..."
    DAD "Ты не должна будешь покидать это место. Минимум три года. Там будет научный городок, и полная автономия."
    UVAO "Это конечно интересно, но я пока ничего не понимаю!"
    DAD "Я пока тоже. Но если ты согласишься, тебе придется на три года забыть весь мир, забыть подруг, знакомых, всё, что тебе было здесь дорого."
    "Подруг? Я прокрутила перед глазами своих подруг. Некоторых я знала еще с детсада. Это было бы непросто-забыть про них. Хотя, это единственное, что меня тут держит."
    "Подумав о долгой разлуке с ними, я не ощутила ничего особенного. И правда, подруги и подруги. Вернусь-будет что рассказать. А там себе еще друзей заведу. А этот болван, который ужасные стишки про любовь пишет?"
    "Разве он мне нужен? Давно хотела ему намекнуть, чтобы он наконец отстал."
    "Вдруг мне на секунду стало страшно за свои мысли. Неужели я ни о чем не пожалею? Неужели смогу уехать отсюда на ТРИ ГОДА без особых сожалений?"
    "Надо прекращать думать об этом. А то сначала ничего не держит в городе, а потом и в жизнь..."
    "Я тряхнула головой, чем немного удивила отца."
    UVAO "Я подумаю, пап."
    DAD "Только не тяни с решением, дорогая. К вечеру ты должна будешь решить. Я уезжаю рано утром, и к этому времени ты должна будешь собрать вещи. И лучше если ты успеешь выспаться. Дорога будет долгой, но на всякий случай лучше не спать в автобусе."
    "..."
    scene Bolnichca with dissolve
    "Стоит ли говорить, согласилась я или нет. Конечно же посидев в комнате, и поразмыслив над ситуацией, я поняла, что нет ни единого аргумента в пользу того, чтобы оставаться в Москве."
    "За окном пролетают дома. Мы едем уже давно, но из города еще не выехали. Бесконечная Москва стелится на километры в обе стороны. До часа пик еще далеко, так что пробки нам не страшны."
    "Еще рано, да к тому же выходной. На дорогах кое-где встречаются автомобили, рейсовые автобусы и велосипедисты, которые, как и мы встали так рано, потому что имеют дела, не терпащие отлагательств."
    "..."
    ".........."
    "Подруги"
    "Учеба"
    "Перед моими заспанными глазами мелькают обрывочные воспоминания, мутные и неточные. {w}Как будто я уже давно уехала, и теперь пытаюсь увидеть сквозь время себя в прошлом, когда-то жившую как все."
    "Но это не забывчивость, а сонное состояние не дает сконцентрировать внимание на чем-либо."
    DAD "Хочешь спать?"
    "Он взял меня за плечо и облокотил на свое."
    UVAO "Немножко."
    DAD "Спи, я разбужу тебя когда мы приедем."
    $ renpy.pause(2)
    DAD "Просыпайся, засоня!"
    "Услышала я сквозь сон. {w}В нос ударил запах резины, вперемешку с папиными сигаретами и чем-то еще."
    "Метрах в трех раздовались удары по железной поверхности, вдалеке слышалась сварка."
    "Я открыла глаза. {w}Отец навис надо мной, и добродушно смотрел мне в глаза."
    DAD "Приехали!"
    "Повторил он. {w}Рука онемела от неудобной позы, и временно перестала функционировать. Ну, хоть не голова! {w}Подумав об этом я ухмыльнулась."
    "Мы вышли из автобуса, и остановились в нерешительности."
    "Перед нами были ворота, которые еще только достраивали. Там и тут виднелись куски арматуры, торчащие, кажется, отовсюду. Слева памятник пионера с горном, справа, видимо, будет еще один."
    "Мой взгляд упал на траву в тени деревьев. Там группа строителей приваривала по буквам какое-то слово к тому, что будет воротами."
    "Со...нек"
    "Со...в..."
    "Совенок!"
    "Только и успела прочесть я. К нам подошел, невесть откуда появившийся человек в халате. {w}Это был мужчина средних лет, ближе к старости."
    SH "Добро пожаловать, вы, должно быть, Семенов Николай?"
    DAD "Да, это я." 
    "Мой отец почтительно пожал протянутую ему руку."
    SH "А вы... Юлия?"
    UVAO "Верно."
    "Он что-то черкнул в своем блокноте и протянул мне руку. Я ответила тем же. {w}Однако, моя рука онемела, и когда ему пришла в голову мысль потрясти ее, получилось очень странное движение."
    "Он отдернул руку, с испугом посмотрев на нее. Через мгновенье его лицо приняло прежнее выражение безразличия, и он продолжил."
    SH "Добро пожаловать!"
    SH "Меня зовут Отто Штехель, я главный..."
    "Он наотмашь протянул руку в сторону территории объекта." 
    SH "...во всей этой богадельне. Сейчас идите прямо, и заходите в первую дверь. Там у вас проверят здоровье, документы, личные вещи, произведут конфискацию запрещенных вещей, вы помоетесь и получите дальнейшее указания."
    "Казалось, это не человек, а робот. Он говорил без эмоций, и чуть не тараторил."
    UVAO "Запрещенные вещи?"
    "Похоже, он был готов к этому вопросу, и выдал ответ моментально, даже не задумавшись."
    SH "Телефоны, ноутбуки, прочая программируемая техника. {w}Возможно наркотики."
    "Его лицо не дало мне понять, пошутил ли он, или нет, или сам не понял, что пошутил."
    SH "Ваше местоположение должно оставаться секретно, и, вы, как понимаете, никакой связи с внешним миром иметь не будите. {w}Понятно?"
    UVAO "Да, понятно. (Шепотом) мы тут, типа, как люди в черном."
    "Последнюю фразу слышал только отец, мы посмеялись и пошли вперед." 









    return    
    
    
    
    
    
