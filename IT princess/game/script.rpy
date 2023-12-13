﻿# Инициализация персонажей
define teacher = Character('Учитель', color = '#FF0000')
define Henry = Character('Генри', color = '#1F618D')
define Maks = Character('Макс', color = '#797D7F')
define Izabella = Character('Изабелла')
define dragon = Character('Спайнкндс', color = '#2471A3')
define troll = Character('Тролль', color = '#1E8449')
define gnoms = Character('Гаети', color = '#117A65')
define mag = Character('Алистер', color ='#F39C12')
define koldun = Character('Азазелло', color = '#922B21')
define autor = Character('Автор')
define general = Character('Главнокомандующий', color = '#2C3E50')
define computer = Character('Компьютер', color = '#1A5276')
define hagen = Character('Хаген', color = '#5DADE2')
define hinki = Character('Хинки', color = '#28B463')
define riobs = Character('Риобс', color = '#1E8449')
define non = Character('???', color = '#E74C3C')
define n = Character(None, kind = nvl)

# TODO
# 210 строчка, Генри лупит пауков
# использовать координаты для изображений
# испольовать для перехода сцен ComposeTransition(dissolve, before=moveoutleft, after = moveinright)
# вместо hide использовать выход за пределы экрана
# переход сцены 8 на 9 с заглушкой
# выбор молота и меча для сражения с пауками
# сделать выбор без реплики
# использовать window hide
# with config.exit_transition
# MoveTransition(2.0, leave = moveinright)
# pos(00,00)

# Объявление переменных

# Растягивание персонажа
transform leap(z=1.05, t=.5):
    easeout t/2 yzoom z
    easein t/2 yzoom 1

# Подпрыгивание персонажа
transform jump_tr(dist=15, t=0.5):
    linear t/2 yoffset - dist
    linear t/2 yoffset 0

#Бег
transform migga_running:
    anchor(0,0) pos(0,0)
    linear 0.1 pos(-9, -7)
    linear 0.1 pos(0,0)
    linear 0.1 pos(9, -7)
    linear 0.1 pos(0,0)
    repeat

#1080*1920
#Вы указали: 500x1000 (c соблюдением пропорций)
#Получилось: 284x1000, 172.39 Кб
# shift+D режим разработчика
# прозрачность 15 textbox

# Начало игры
label start:
    # call scene1_school from _call_scene1_school # Диалог в школе (сцена 1)
    # call scene2_class from _call_scene2_class # Сцена с учителем и засыпание Генри
    # call scene3_sleep from _call_scene3_sleep # Генри летит спать
    # call scene4_new_country from _call_scene4_new_country # Генри впервые в новом мире
    # call scene5_forest from _call_scene5_forest # Встреча с дракончиком
    # call scene6_wizard_forest from _call_scene6_wizard_forest # Разговор с дракончиком об оружии
    # call scene7_cave from _call_scene7_cave # Генри находит мечи и молот
    # call scene8_fairy_forest from _call_scene8_fairy_forest # Встреча с троллем
    # call scene9_gnoms from _call_scene9_gnoms # Встреча с гномами
    call scene10_megastore from _call_scene10_megastore # Разговор с магом
    call scene11_coldun from _call_scene11_coldun # Встреча с колдуном
    # call scene12_hagen from _call_scene12_hagen # Встреча с Хагеном
    # if not the_end:
    #     call scene13_end from _call_scene13_end # Разговор обо сне с другом
    return

label scene1_school:
    play music peremena fadein 1.0
    scene scene1 with dissolve
    show henry at left with moveinbottom
    show maks at right with moveinbottom
    play sound hmmm1
    show maks at leap
    Maks 'Слушай, а чем бы ты хотел заниматься всю жизнь?'
    play sound hmmm3
    show henry at leap
    Henry 'Если честно, я еще не решил, чем хочу заниматься'
    show maks at leap
    Maks 'Я бы хотел связать свою жизнь с информационными технологиями'
    play sound surprise1
    show henry at leap
    Henry 'А это интересно, но в этой сфере столько направлений и специальностей...'
    stop music
    play sound bell
    show maks at leap
    Maks 'Ладно, что-то мы заболтались, пошли на урок'
    stop sound fadeout 1.0
    stop music fadeout 1.0
    return

label scene2_class:
    scene scene2 with dissolve
    show teacher at center with moveinbottom
    show teacher at leap
    play sound hmmm9
    teacher '"Отец мой Андрей Петрович Гринёв в молодости своей..." - монотонно начал читать учитель'
    play sound yawn1
    scene bg black with Fade(2,0,0)
    scene scene2_blur with Dissolve(1) # блюр 10
    play sound yawn1
    scene bg black with Fade(2,0,0)
    scene scene2_blur with Dissolve(1)
    'Генри, не выспавшись, уже начал засыпать на задней парте'
    stop sound fadeout 1.0
    return

label scene3_sleep:
    play sound krik1
    scene scene3 with dissolve
    window hide
    show henry at right with moveinleft
    show henry:
        xalign 2.5
    with moveinright
    Henry 'ААААААААААААААААА'
    stop sound fadeout 1.0
    return

label scene4_new_country:
    play music birds_sing fadein 1.0
    scene scene4 with dissolve
    show henry at center with moveinbottom
    play sound hmmm6
    show henry at leap
    Henry 'Куда я попал? Где я очутился?'
    Henry 'Что мне делать?'
    stop sound fadeout 1.0
    return

label scene5_forest:
    scene scene5 with dissolve
    show henry at center with moveinbottom
    play sound hmmm11
    show henry at leap
    Henry 'Хммммм...'
    Henry 'Что это за синий свет в лесу?'
    Henry 'Нужно пойти поверить'
    show henry at left with easeinleft
    show dragon_in_chains at topright with moveinbottom
    play sound hmmm4
    show henry at leap
    Henry 'Это же дракон, он попал в ловушку, нужно ему помочь'
    show henry at center with easeinright
    play sound chain1
    show henry at left with easeinleft
    hide dragon_in_chains with easeinbottom
    show dragon at right with moveinbottom
    show henry at leap
    Henry 'Кто ты такой?'
    play sound hmmm2
    show dragon at leap
    non 'Спасибо за помощь. Меня зовут Спайндикс'
    dragon 'Я помогу тебе разобраться в этом мире'
    return

label scene6_wizard_forest:
    scene scene6 with dissolve
    show henry at left with moveinbottom
    show dragon at right with moveinbottom
    play sound hmmm5
    show dragon at leap
    dragon 'Чтобы выжить в этой стране, необходимо найти оружие'
    stop sound fadeout 1.0
    play sound hmmm9
    show henry at leap
    Henry 'Ты знаешь, где его можно достать?'
    play sound hmmm2
    show dragon at leap
    dragon 'К счастью, здесь недалеко есть пещера, в которой может быть что-нибудь полезное'
    stop sound fadeout 1.0
    stop music fadeout 1.0
    return

label scene7_cave:
    play music water_down fadein 1.0 volume 0.8
    scene scene7 with dissolve
    show chest_close at top with moveinbottom
    show henry at left with moveinbottom
    show dragon at right with moveinbottom
    play sound hmmm10 volume 0.6
    show henry at leap
    Henry 'Смотри!'
    Henry 'Это же сундук'
    Henry 'Давай откроем его'
    play sound chest
    show henry at center with easeinright
    show henry at left with easeinleft
    hide chest_close
    show chest_open at top with dissolve
    show sword at topleft with zoomin
    show hammer at topright with zoomin
    show henry at leap
    Henry 'Что это за буквы на мече и молоте?'
    stop sound fadeout 1.0
    show dragon at leap
    dragon 'Я не владею этими знаниями'
    play sound surprise1
    show henry at leap
    Henry 'Кажется, я понимаю, что здесь написано'
    Henry 'Из этого я точно знаю Python, C#'
    stop sound fadeout 1.0
    play sound hmmm11
    show dragon at leap
    dragon 'Это что-то из твоего мира?'
    show henry at leap
    Henry 'Да, это языки программирования'
    hide sword
    hide hammer
    hide chest_open
    return

label scene8_fairy_forest:
    play sound hmmm1
    show henry at leap
    Henry 'Куда мы идём дальше?'
    show dragon at leap
    dragon 'Давай пойдём к магу Алистеру, он поможет нам'
    stop music fadeout 1.0
    play music river fadein 1.0 volume 0.35
    scene scene8 with dissolve
    show henry at left with moveinbottom
    show dragon at right with moveinbottom
    play sound hmmm7
    show henry at leap
    Henry 'Что это за чудесный лес?'
    show dragon at leap
    dragon 'Это лес Мальдонии, место, где живут феи'
    show henry at leap
    Henry 'Как выглядят феи? И где же они все?'
    play sound hmmm1
    show dragon at leap
    dragon 'Фея в переводе с Дотракийского языка переводится как мечта'
    dragon 'К сожалению, их здесь осталось мало, так как их всех похищают тролли'
    dragon 'Я предлагаю поторопиться, тролли очень опасны'
    play sound thunder volume 2.0
    show troll_mini at truecenter
    show henry at leap
    Henry 'Что это такое?'
    show dragon at leap
    dragon 'Похоже на звук приближения тролля'
    hide troll_mini
    show troll at truecenter with zoomin
    show troll at leap
    play sound hmmm9 volume 1.5
    troll 'Кто вы такие ? Что вы забыли здесь?'
    play sound hmmm4
    show henry at leap
    Henry 'Здравствуйте, извините нас пожалуйста, мы уже уходим'
    show troll at leap
    troll 'Какие мы вежливые. Этот подарок тебе'
    hide dragon with easeinbottom
    hide troll
    show troll_average at right with moveinbottom
    show present_close at top with moveinbottom
    show henry at leap
    Henry 'Что это за коробочка? Что внутри?'
    show troll_average at leap
    troll 'Этот подарок даст тебе постоянные слезы и истерики, а также ты будешь плохо управлять своими эмоциями'
    menu:
        'Как поступить Генри?'
        'Принять подарок от тролля':
            play sound hmmm3
            show henry at leap
            Henry 'Спасибо за подарок'
            play sound present volume 1.3
            hide present_close
            show present_open at top with dissolve
            play sound spider_legs volume 1.45
            show spiders at top with dissolve
            show spiders at topright with easeinright
            show spiders2 at top with dissolve
            show spiders2 at topleft with easeinleft
            show spiders3 at top with dissolve
            show spiders2 at left with easeinbottom
            stop sound fadeout 1.0
            play sound krik2
            show henry at leap
            Henry 'ААААААААААА'
            stop sound fadeout 1.0
            Henry 'Пауки!'
            play sound hmmm8 volume 1.3
            show troll_average at leap
            troll 'Ах ты...'
            troll 'Не трожь моих пауков! А не то...'
            hide present_open
            show troll_average at center with easeinleft
            play sound krik2
            show henry at leap
            Henry 'АААААААААА'
            stop sound fadeout 1.0
            show dragon at right with moveinbottom
            show dragon at leap
            dragon 'Бежим!!!'
        'Проигнорировать предложение':
            hide present_close
            play sound hmmm2
            show henry at leap
            Henry 'Извините, но я откажусь, нам нужно идти'
            show troll_average at center with easeinleft
            play sound hmmm9 volume 1.5
            show troll_average at leap
            troll 'Нет! Ты не уйдёшь!'
            play sound krik2
            show henry at leap
            Henry 'АААААААААА'
            stop sound fadeout 1.0
            show dragon at right with moveinbottom
            dragon 'Бежим!!!'
    stop music fadeout 1.0
    return

label scene9_gnoms:
    play music birds_sing fadein 1.0
    scene scene9 with dissolve
    show henry at left with moveinbottom
    show dragon at right with moveinbottom
    show dragon at leap
    dragon 'Вроде бы убежали'
    play sound gasp
    show henry at leap
    Henry 'Да, это было опасно'
    Henry 'Слушай, я понял, нельзя сдаваться и думать о провале перед своими экзаменами'
    play sound hmmm2
    show dragon at leap
    dragon 'Это ты о чём?'
    play sound hmmm7
    show henry at leap
    Henry 'Да так...'
    Henry 'Где мы сейчас находимся?'
    show dragon at leap
    dragon 'Мы попали в долину, которая называется Энчастия'
    play sound gaeti_run volume 1.5
    show henry at leap
    Henry 'А что это за существа бегут к нам?'
    stop sound fadeout 1.0
    show dragon at leap
    dragon 'Гаети. Это маленькие существа, которые здесь обитают'
    show gnom1_mini:
        xalign 0.5
        yalign 0.64
    with zoomin
    show gnom2_mini:
        xalign 0.4
        yalign 0.6
    with zoomin
    show gnom3_mini:
        xalign 0.3
        yalign 0.5
    with zoomin
    show gnom4 at left with moveinbottom
    show gnom5:
        xalign 0.18
        yalign 0.47
    with moveinbottom
    show gnom6:
        xalign 0.714
        yalign 0.616
    with moveinbottom
    play sound hmmm12
    show henry at leap
    Henry 'Здравствуйте, дорогие жители'
    play sound hmmm9
    show gnom5 at leap
    gnoms 'Кто ты такой?'
    play sound hmmm9
    show gnom6 at leap
    gnoms 'Ты не похож на здешних жителей'
    play sound hmmm9
    show gnom4 at leap
    gnoms 'Что ты здесь забыл?'
    hide gnom5
    show gnom3:
        xalign 0.18
        yalign 0.47
    with moveinbottom
    hide gnom3_mini
    show gnom5_mini:
        xalign 0.3
        yalign 0.5
    with zoomin
    hide gnom6
    show gnom1:
        xalign 0.714
        yalign 0.616
    with moveinbottom
    hide gnom1_mini
    show gnom6_mini:
        xalign 0.5
        yalign 0.64
    with zoomin
    play sound hmmm9
    show gnom3 at leap
    gnoms 'Ты хочешь пойти с нами?'
    play sound hmmm9
    show gnom1 at leap
    gnoms 'Ты должен пойти с нами'
    play sound hmmm7
    show henry at leap
    Henry 'Что же делать?'
    menu:
        Henry 'Что мне выбрать?'
        'Попробовать ответить на все вопросы Гаети':
            play sound hmmm1
            show henry at leap
            Henry 'Меня зовут Генри, я не из вашего мира'
            Henry 'Я иду на поиски мага Алистера, чтобы он помог мне вернутся домой'
            play sound hmmm9
            show gnom1 at leap
            gnoms 'Пошли с нами'
            play sound hmmm9
            show gnom3 at leap
            gnoms 'Тебе точно нужно идти с нами'
            play sound hmmm9
            show gnom4 at leap
            gnoms 'Ты идёшь с нами'
            play sound hmmm4
            show henry at leap
            Henry 'Извините, мне нужно идти'
            show henry:
                xalign 1.25
                yalign 1.25
            with moveinright
            show dragon:
                xalign 1.45
                yalign 1.45
            with moveinright
        'Взять себя в руки и бежать':
            show henry:
                xalign 1.25
                yalign 1.25
            with moveinright
            show dragon:
                xalign 1.45
                yalign 1.45
            with moveinright
    scene scene9d with slideawayleft
    show henry at left with moveinleft
    show dragon at right with moveinleft
    play sound hmmm2
    show henry at leap
    Henry 'Знаешь, в моем мире все устроено немного не так...'
    Henry 'И Гаети мне кое-кого напомнили'
    show dragon at leap
    dragon 'Кого напомнили?'
    play sound hmmm1
    show henry at leap
    Henry 'Они напоминают мне моих родителей и учителей'
    Henry 'Мне также все твердят : «Выбрал вуз?», «сдай ЕГЭ», «поступи на бюджет»'
    show dragon at leap
    dragon 'Да, действительно, сходство с Гаети есть'
    play sound surprise1
    show henry at leap
    Henry 'Из этой ситуации я сделал вывод, что родители иногда правы, они желают нам добра, поэтому к ним нужно прислушиваться'
    Henry 'Они всегда заботятся о нас. Требуют, чтобы мы отдыхали, не перетруждались'
    show dragon at leap
    dragon 'То есть учиться в вашем мире не нужно?'
    show henry at leap
    Henry 'Конечно нужно, но нужно знать меру во всём'
    stop music fadeout 1.0
    return

label scene10_megastore:
    play music bazar fadein 1.0
    scene scene10 with dissolve
    show dragon at right with moveinbottom
    show henry at left with moveinbottom
    play sound hmmm4
    show dragon at leap
    dragon 'Вот мы и пришли'
    dragon 'Вот там лавка Алистера'
    show henry at leap
    Henry 'Давай зайдём'
    stop music fadeout 1.0
    play sound door_bell
    scene scene10_1 with dissolve
    show henry at left with moveinbottom
    show dragon at right with moveinbottom
    show mag at center with moveinbottom
    play sound hmmm9
    show mag at leap
    mag 'Приветствую вас, что вы хотели в моей лавке?'
    play sound hmmm4
    show henry at leap
    Henry 'Здравствуйте, мне нужно попасть в мой мир'
    show dragon:
        xalign 1.5
    with moveinright
    show mag at right with moveinright
    play sound hmmm8
    show mag at leap
    mag 'Ой, с этим я тебе помочь не могу'
    show henry at leap
    Henry 'Что же мне тогда делать? Как здесь выжить?'
    show mag at leap
    mag 'Ты бы мог пригодиться в этом мире'
    play sound hmmm12
    show henry at leap
    Henry 'Что же ты можешь мне предложить?'
    show mag at leap
    mag 'Есть несколько вариантов'
    $ first_choose = False
    $ second_choose = False
    $ third_choose = False
    window hide
    call choose_scene10 from _call_choose_scene10 # Сцена выбора цикличная
    scene scene10_1 with dissolve
    show henry at left with moveinbottom
    show dragon at right with moveinbottom
    play sound hmmm6
    show henry at leap
    Henry 'Да, трудно в этом мире, что же мне делать?'
    stop sound fadeout 1.0
    play sound hmmm2
    show dragon at leap
    dragon 'У меня есть ещё одно предложение'
    dragon 'Мы можем отправиться на гору Нан Курнир, там живёт один колдун. Но сразу скажу, он немного сумасшедший'
    return

menu choose_scene10:
    'Ты можешь пасти единорогов':
        if first_choose:
            play sound hmmm9
            show mag at leap
            mag 'Ты уже спрашивал меня про это'
            call choose_scene10 from _call_choose_scene10_1
            return
        play music birds_sing fadein 1.0
        scene scene10_2 with dissolve
        show henry at left with moveinbottom
        show mag at right with moveinbottom
        show unicorn_mini_zerkalo:
            xalign 0.3
            yalign 0.5889
        with zoomin
        show unicorn:
            xalign 0.423
            yalign 0.43
        with zoomin
        play sound hmmm10
        show henry at leap
        Henry 'И как же мне к ним подойти?'
        show mag at leap
        mag 'Ты должен показать единорогу силу'
        window hide
        show henry:
            xalign 1.5
        with moveinright
        show henry_mini:
            xalign 0.55
            yalign 0.43
        with moveinright
        play sound horse
        show unicorn:
            xalign 0.3
        with easeinleft
        show henry_mini:
            xalign 0.4
        with moveinleft
        hide unicorn
        show unicorn_zerkalo:
            xalign 0.3
            yalign 0.43
        with dissolve
        show unicorn_zerkalo:
            xalign 1.5
        with moveinright
        stop sound fadeout 1.0
        show unicorn_mini_zerkalo:
            xalign 1.5
        with moveinright
        show henry_mini:
            xalign 1.5
        with moveinright
        show henry at left with moveinleft
        play sound gasp
        show henry at leap
        Henry 'Да, к ЕГЭ мне было готовиться легче'
        stop music fadeout 1.0
        $ first_choose = True
        if first_choose & second_choose & third_choose == True:
            return
        else:
            scene scene10_1 with dissolve
            show henry at left with moveinbottom
            show mag at right with moveinbottom
            call choose_scene10 from _call_choose_scene10_2
            return
    'Ты можешь состоять в армии короля':
        if second_choose:
            play sound hmmm9
            show mag at leap
            mag 'Ты уже спрашивал меня про это'
            call choose_scene10 from _call_choose_scene10_3
            return
        play music hero fadein 1.0
        scene scene10_3 with dissolve
        show henry at left with moveinbottom
        show mag at right with moveinbottom
        show general at center with moveinbottom
        play sound hmmm9
        show mag at leap
        mag 'Ты можешь состоять в армии короля'
        play sound krik3
        show general at leap
        general 'Бойцы, вы должны быть готовы ко всему'
        general 'Недавно нам объявили войну Марийцы'
        show mag:
            xalign 1.8
        with moveinright
        show general at right with moveinright
        play sound hmmm9
        show general at leap
        general 'С этого момента вы будете жить в замке'
        general 'Итак, ваше первое задание на сегодня...'
        general 'Нужно подняться на гору Нан Куринир, добежать до края острова и принести мне волос единорога'
        play sound hmmm4
        show henry at leap
        Henry 'Нее...'
        Henry 'Это не для меня'
        play sound hmmm8
        show henry at leap
        Henry 'А вот если бы я пошёл в IT, то мог бы работать удалённо и жить в Дубае'
        stop sound fadeout 1.0
        play sound hmmm9
        show general at leap
        general 'Что это ты бормочешь?'
        show henry at leap
        Henry 'Да так... Мысли вслух'
        stop music fadeout 1.0
        $ second_choose = True
        if first_choose & second_choose & third_choose == True:
            return
        else:
            scene scene10_1 with dissolve
            show henry at left with moveinbottom
            show mag at right with moveinbottom
            call choose_scene10 from _call_choose_scene10_4
            return
    'Ты можешь стать моим учеником':
        if third_choose:
            show mag at leap
            play sound hmmm9
            mag 'Ты уже спрашивал меня про это'
            call choose_scene10 from _call_choose_scene10_5
            return
        play sound hmmm8
        show mag at leap
        mag 'Тебе нужно будет днём и ночью выполнять мои поручения'
        mag 'Также нужно будет рисковать своей жизнью, чтобы доставать необходимые ингредиенты для зелий'
        play sound hmmm7
        show henry at leap
        Henry 'Извини, но такое мне тоже не подходит'
        Henry 'В IT у меня был бы удобный график работы'
        $ third_choose = True
        if first_choose & second_choose & third_choose == True:
            return
        else:
            scene scene10_1 with dissolve
            show henry at left with moveinbottom
            show mag at right with moveinbottom
            call choose_scene10 from _call_choose_scene10_6
            return

label scene11_coldun:
    scene scene11 with dissolve
    play music water_down fadein 1.0
    show henry at left with moveinbottom
    show dragon at right with moveinbottom
    show koldun at center with moveinbottom
    show koldun at leap
    koldun 'Давно у меня не было гостей, зачем пожаловали?'
    show henry at leap
    Henry 'Мне нужно попасть в свой мир'
    show koldun at leap
    koldun 'Я давно подозревал, что есть другие миры'
    koldun 'Однако я не могу тебя туда отправить, но могу показать кое-что другое'
    show dragon:
        xalign 1.5
    with moveinright
    show koldun at right with moveinright
    show zerkalo1:
        xalign 0.2
        yalign 0.51
    with moveinbottom
    show zerkalo2:
        xalign 0.41
        yalign 0.51
    with moveinbottom
    show zerkalo3:
        xalign 0.62
        yalign 0.51
    with moveinbottom
    koldun 'Перед тобой три зеркала, выбирай понравившееся'
    window hide
    $ first_zerkalo = False
    $ second_zerkalo = False
    stop music fadeout 1.0
    call choose_scene11 from _call_choose_scene11
    return

menu choose_scene11:
    'Зеркало 1':
        if first_zerkalo:
            show koldun at leap
            play sound hmmm9
            koldun 'Ты уже смотрел, что там'
            call choose_scene11 from _call_choose_scene11_1
            return
        $ first_zerkalo = True
        scene scene11_1 with dissolve
        show henry at left with moveinbottom
        show syringe1left:
            xalign 0.78385
            yalign 0.14259
        with zoomin
        show syringe2left:
            xalign 0.6392
            yalign 0.38
        with zoomin
        show syringe3left:
            xalign 0.82
            yalign 0.514
        with zoomin
        show syringe1left:
            xalign 0.2
        with moveinleft
        show syringe2left:
            xalign 0.2
        with moveinleft
        show syringe3left:
            xalign 0.2
        with moveinleft
        show henry at leap
        play sound krik2
        Henry 'ААААА'
        stop sound fadeout 1.0
        Henry 'Они летают'
        window hide
        show henry:
            xalign 1.5
        with moveinright
        hide syringe1left
        hide syringe2left
        hide syringe3left
        show syringe1right:
            xalign 0.2
            yalign 0.14259
        with zoomin
        show syringe2right:
            xalign 0.2
            yalign 0.38
        with zoomin
        show syringe3right:
            xalign 0.2
            yalign 0.514
        with zoomin
        show syringe1right:
            xalign 1.5
        with moveinright
        show syringe2right:
            xalign 1.5
        with moveinright
        show syringe3right:
            xalign 1.5
        with moveinright
        scene scene11 with dissolve
        show zerkalo1:
            xalign 0.2
            yalign 0.51
        with moveinbottom
        show zerkalo2:
            xalign 0.41
            yalign 0.51
        with moveinbottom
        show zerkalo3:
            xalign 0.62
            yalign 0.51
        show henry at left with moveinbottom
        show koldun at right with moveinbottom
        call choose_scene11 from _call_choose_scene11_2
        return
    'Зеркало 2':
        if second_zerkalo:
            show koldun at leap
            play sound hmmm9
            koldun 'Ты уже смотрел, что здесь'
            call choose_scene11 from _call_choose_scene11_3
            return
        $ second_zerkalo = True
        scene scene11_2 with dissolve
        show henry at left with moveinbottom
        show henry at leap
        Henry 'Сколько же тут книг?'
        window hide
        show book1:
            xalign 0.64696
            yalign 0,174
        with zoomin
        show book2:
            xalign 0.74
            yalign 0.497
        with zoomin
        show book1:
            xalign 0.2
        with moveinleft
        show book2:
            xalign 0.2
        with moveinleft
        show henry at right with moveinright
        show book1:
            xalign 0.8
        with moveinright
        show book2:
            xalign 0.8
        with moveinright
        show henry at left with moveinleft
        show henry at leap
        play sound hmmm12
        Henry 'Они кружат мне голову'
        window hide
        show book1:
            xalign 0.2
        with moveinleft
        show book2:
            xalign 0.2
        with moveinleft
        show henry:
            xalign 1.5
        with moveinright
        show book1:
            xalign 1.5
        with moveinright
        show book2:
            xalign 1.5
        with moveinright
        scene scene11 with dissolve
        show zerkalo1:
            xalign 0.2
            yalign 0.51
        with moveinbottom
        show zerkalo2:
            xalign 0.41
            yalign 0.51
        with moveinbottom
        show zerkalo3:
            xalign 0.62
            yalign 0.51
        show henry at left with moveinbottom
        show koldun at right with moveinbottom
        call choose_scene11 from _call_choose_scene11_4
        return
    'Зеркало 3':
        scene scene11_3 with dissolve
        play music computer_work fadein 1.0
        show henry at left with moveinbottom
        show henry at leap
        play sound hmmm1
        Henry 'Может я смогу написать какую-нибудь программу на компьютере?'
        Henry 'backend-разработчик, кто это такой?'
        show macbook:
            xalign 0.9
            yalign 0.51296
        with moveinbottom
        show macbook at leap
        computer 'Специалист, который занимается серверной частью сайтов, мобильных и десктопных приложений и игр'
        show henry at leap
        Henry 'А чем же он занимается?'
        show macbook at leap
        computer 'Он создает базы данных и управляет ими, проводит интеграции с внешними сервисами и занимается всем, что находится «под капотом» сайта'
        show henry at leap
        Henry 'Как же интересно, но какие плюсы у этой профессии?'
        show macbook at leap
        computer 'Востребованность профессии, работа из любой точки планеты, возможность выбирать направление, перспективы, высокая зарплата'
        show henry at leap
        Henry 'А где же этому можно научиться ?'
        show macbook at leap
        computer 'Программная инженерия — это направление подготовки программистов, готовых к индустриальному производству программного обеспечения для информационно-вычислительных систем различного назначения'
        return

label scene12_hagen:
    show henry at leap
    Henry 'Кто-то идёт, чьи это шаги?'
    show macbook:
        xalign 2.0
    with moveinright
    show hagen at right with moveinbottom
    show hagen at leap
    hagen 'Что ты здесь забыл?'
    show henry at leap
    Henry 'Извините, я просто изучаю профессию, используя ваш компьютер'
    show hagen at leap
    hagen 'Это мое измерение и моя ветка времени, здесь всё решаю я'
    show henry at leap
    Henry 'А вы не могли бы отправить меня домой?'
    show hagen at leap
    hagen 'Пока ты в моем мире, ты будешь работать на меня'
    hagen 'Познакомся с коллегами они введу тебя в курс дела'
    show henry at leap
    Henry 'Хорошо , а куда мне идти?'
    show hagen at leap
    hagen 'Прямо по коридору и направо'
    stop music fadeout 1.0
    scene scene12 with dissolve
    play music koridor fadein 1.0
    show henry at left with moveinleft
    Henry 'Интересно получится ли у меня работать здесь?'
    show henry:
        xalign 1.5
    with MoveTransition(2.0, leave = moveinright)
    stop music fadeout 1.0
    scene scene12_1 with dissolve
    show henry at left with moveinleft
    show hinki at right with moveinbottom
    show hinki at leap
    hinki 'Ой, а кто это у нас тут ? Что ты здесь забыл?'
    show riobs at center with moveinbottom
    show riobs at leap
    riobs ' Хинки, будь помягче с новеньким'
    show riobs at leap
    riobs 'Приветствую тебя, как тебя зовут?'
    show henry at leap
    Henry 'Привет, меня зовут Генри'
    show riobs at leap
    riobs 'Мы сейчас работаем над одним проектом'
    show hinki at leap
    hinki 'Я не думаю, что ты можешь нам чем-нибудь помочь'
    show henry at leap
    Henry 'Я бы мог попробовать себя в роли Backend — разработчика'
    show hinki at leap
    hinki 'Ха-ха-ха, ты хоть знаешь, что такое веб-сервер?'
    show henry at leap
    Henry 'Сервер, принимающий HTTP-запросы от клиентов, обычно веб-браузеров, и выдающий им HTTP-ответы, как правило, вместе с HTML-страницей, изображением, файлом, медиа-потоком или другими данными'
    show hinki at leap
    hinki 'У нас даже уборщик знает, что это такое. Знаешь ли ты что такое HTTP?'
    show henry at leap
    Henry 'Это протокол, который использует для передачи содержимого TCP, поэтому HTTP считается надежным протоколом для обмена содержимым. Также HTTP — самый популярный протокол'
    show henry at leap
    Henry 'Сам не знаю, как мне удалось это запомнить'
    show hinki at leap
    hinki 'Ладно, может ты что-то знаешь. У меня есть последний вопрос'
    hinki 'Как веб-страницы взаимодействуют с серверами?'
    show henry at leap
    Henry 'Веб-браузеры взаимодействуют с веб-серверами при помощи протокола передачи гипертекста (HTTP). При взаимодействии, браузер отправляет на сервер HTTP-запрос'
    show henry at leap
    Henry 'А также, необходимо знать, что путь (URL), который определяет целевой сервер и ресурс (например, HTML-файл, конкретная точка данных на сервере или запускаемый инструмент)'
    show riobs at leap
    riobs 'Хинки, ну отцепись от парнишки. Я думаю, он уже доказал, что может писать проект с нами'
    show hinki at leap
    hinki 'Хм... Ладно, пусть попробует'
    show riobs at leap
    riobs 'Итак, мы работаем над проектом “Gold Ball”. Заказчик проводил городские оффлайн-турниры по киберфутболу'
    show riobs at leap
    riobs 'Чтобы охватить игроков по всей стране и масштабировать проект на СНГ, клиент заказал разработку веб-сервиса для автоматизации проведения соревнований'
    show hinki at leap
    hinki 'Проведя анализ, мы спроектировали механику турниров, логику распределения игроков по турнирной сетке, статистику и систему рейтинга'
    show hinki at leap
    hinki 'Оценив полученные данные, приняли решение в пользу фреймворка Ruby on Rails'
    show hinki at leap
    hinki 'Он подходит, чтобы реализовать описанный функционал, а его шаблонизатор хорошо справляется с типовыми страницами турниров и матчей'
    show hinki at leap
    hinki 'Ты что-нибудь понимаешь?'
    show henry at leap
    Henry 'Я примерно понял, что нужно сделать'
    show riobs at leap
    riobs 'Хорошо, можешь переосмыслить эту информацию. Завтра ты должен будешь что-нибудь предложить'
    show riobs at leap
    riobs 'Хинки, ты можешь показать комнату Генри?'
    show hinki at leap
    hinki 'Неохотно, но соглашусь'
    scene scene12 with dissolve
    play sound koridor fadein 1.0
    show henry at left with moveinleft
    show hinki at left with moveinleft
    show hinki at leap
    hinki 'Идём за мной'
    window hide
    show hinki:
        xalign 1.5
    with MoveTransition(2.0, leave = moveinright)
    show henry:
        xalign 1.5
    with MoveTransition(2.0, leave = moveinright)
    stop sound fadeout 1.0
    scene scene12_2 with dissolve
    show henry at left with moveinleft
    show hinki at center with moveinleft
    show hinki at leap
    hinki 'Здесь ты можешь отдохнуть'
    show henry at leap
    Henry 'Спасибо, что проводил'
    show hinki at leap
    hinki 'Не обольщайся, меня просто попросил мой коллега'
    show hinki:
        xalign 1.5
    with moveinright
    $ the_end = False
    menu:
        Henry 'Может мне и вправду поспать или подумать над проектом?'
        'Поспать':
            $ the_end = True
            scene bg black with dissolve
            window hide
            n '''Генри проснулся во время урока,
            не помня свои приключения'''
            nvl clear
            n '''КОНЕЦ!!!'''
        'Подумать над проектом':
            show henry at center with moveinright
            show henry at leap
            Henry 'Меня так заинтересовал проект, может подумать над ним?'
            Henry 'Хотя я сегодян очень сильно устал'
            Henry 'Необходимо набраться сил перед завтрашним днём'
            show henry at leap
            Henry 'Пойду спать'
    return

label scene13_end:
    show scene2_blur with dissolve
    scene bg black with Fade(2,0,0)
    scene scene2_blur with Dissolve(1)
    play sound pshhh
    Maks 'Пшшш... Генри!'
    Maks 'Генри, вставай, если Юлия Владимировна увидит, что ты спишь, то ты будешь спать у директора'
    scene bg black with Fade(2,0,0)
    scene scene2 with Dissolve(1)
    Henry 'Ладно, пошли давай'
    scene scene1 with dissolve
    show henry at left with moveinbottom
    show maks at right with moveinbottom
    show maks at leap
    Maks 'Ты видел, что в УрФУ проходит День открытых дверей, пойдём?'
    show henry at leap
    play sound hmmm1
    Henry 'Разумеется, мне нужно узнать всё о поступлении, ведь я уже определился с  профессией и направлением'
    show henry at leap
    Henry 'Я поступлю на программную инженерию и стану backend-разработчиком'
    scene bg black with dissolve
    window hide
    n '''КОНЕЦ!!!'''
    nvl clear
    return