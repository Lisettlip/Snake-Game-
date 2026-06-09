# Impordime pygame mooduli.
import pygame

# Impordime sys mooduli.
import sys

# Impordime random mooduli.
import random

# Impordime os mooduli.
import os

# Käivitame pygame'i.
pygame.init()

# Määrame akna laiuse.
akna_laius = 720

# Määrame akna kõrguse.
akna_korgus = 480

# Määrame ühe ruudu suuruse.
ruut = 20

# Määrame mängu kiiruse.
kiirus = 12

# Loome mänguakna.
aken = pygame.display.set_mode((akna_laius, akna_korgus))

# Paneme aknale pealkirja.
pygame.display.set_caption("Öine ussimäng")

# Loome mängu kella.
kell = pygame.time.Clock()

# Leiame programmi kausta.
baaskaust = os.path.dirname(os.path.abspath(__file__))

# Määrame piltide kausta.
pildikaust = baaskaust

# Kui olemas on pildid kaust, siis kasutame seda.
if os.path.exists(os.path.join(baaskaust, "pildid")):
    # Määrame pildikaustaks pildid kausta.
    pildikaust = os.path.join(baaskaust, "pildid")

# Määrame tumesinise tausta.
taust = pygame.Color(15, 25, 60)

# Määrame paneeli värvi.
paneel = pygame.Color(25, 40, 90)

# Määrame valge värvi.
valge = pygame.Color(255, 255, 255)

# Määrame punase värvi.
punane = pygame.Color(220, 50, 50)

# Määrame rohelise värvi.
roheline = pygame.Color(0, 200, 80)

# Määrame musta värvi.
must = pygame.Color(0, 0, 0)

# Loome väikese fondi.
font_vaike = pygame.font.SysFont("consolas", 24)

# Loome suure fondi.
font_suur = pygame.font.SysFont("arial", 55)


# Loome pildi laadimise funktsiooni.
def lae_pilt(failinimi):
    # Loome pildi täieliku failitee.
    failitee = os.path.join(pildikaust, failinimi)

    # Kontrollime, kas pilt on olemas.
    if not os.path.exists(failitee):
        # Kuvame puuduva pildi nime.
        print("Puudub pilt:", failitee)

        # Sulgeme pygame'i.
        pygame.quit()

        # Sulgeme programmi.
        sys.exit()

    # Laeme pildi.
    pilt = pygame.image.load(failitee).convert_alpha()

    # Muudame pildi suurust.
    pilt = pygame.transform.scale(pilt, (ruut, ruut))

    # Tagastame pildi.
    return pilt


# Laeme õuna pildi.
ouna_pilt = lae_pilt("apple.png")

# Laeme maasika pildi.
maasika_pilt = lae_pilt("strawberry-png-22943.png")

# Laeme kivi pildi.
kivi_pilt = lae_pilt("kivi.jpg")


# Loome teksti kuvamise funktsiooni.
def kuva_tekst(tekst, font, varv, x, y):
    # Loome teksti pildi.
    tekstipilt = font.render(tekst, True, varv)

    # Kuvame teksti aknas.
    aken.blit(tekstipilt, (x, y))


# Loome juhusliku koha leidmise funktsiooni.
def juhuslik_koht(keelatud):
    # Otsime sobivat kohta.
    while True:
        # Loome juhusliku x-koordinaadi.
        x = random.randrange(0, akna_laius, ruut)

        # Loome juhusliku y-koordinaadi.
        y = random.randrange(40, akna_korgus, ruut)

        # Paneme koha listi.
        koht = [x, y]

        # Kontrollime, kas koht on vaba.
        if koht not in keelatud:
            # Tagastame vaba koha.
            return koht


# Loome mängu algandmete funktsiooni.
def alusta_mang():
    # Loome ussi keha.
    uss = [[100, 60], [80, 60], [60, 60]]

    # Loome ussi pea.
    ussi_pea = [100, 60]

    # Määrame algsuuna.
    suund = "PAREM"

    # Määrame soovitud suuna.
    uus_suund = "PAREM"

    # Määrame skoori.
    skoor = 0

    # Loome õuna.
    oun = juhuslik_koht(uss)

    # Alguses maasikat ei ole.
    maasikas = None

    # Loome tühja kivide listi.
    kivid = []

    # Loome viis kivi.
    for i in range(5):
        # Lisame ühe kivi vabale kohale.
        kivid.append(juhuslik_koht(uss + [oun] + kivid))

    # Tagastame mängu algandmed.
    return uss, ussi_pea, suund, uus_suund, skoor, oun, maasikas, kivid


# Loome mängu algandmed.
uss, ussi_pea, suund, uus_suund, skoor, oun, maasikas, kivid = alusta_mang()

# Määrame, et mäng ei ole läbi.
mang_labi = False

# Käivitame mängutsükli.
while True:
    # Loeme kõik sündmused.
    for event in pygame.event.get():
        # Kontrollime akna sulgemist.
        if event.type == pygame.QUIT:
            # Sulgeme pygame'i.
            pygame.quit()

            # Sulgeme programmi.
            sys.exit()

        # Kontrollime klahvivajutusi.
        if event.type == pygame.KEYDOWN:
            # Kontrollime üles liikumist.
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                # Muudame suuna üles.
                uus_suund = "ULES"

            # Kontrollime alla liikumist.
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                # Muudame suuna alla.
                uus_suund = "ALLA"

            # Kontrollime vasakule liikumist.
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                # Muudame suuna vasakule.
                uus_suund = "VASAK"

            # Kontrollime paremale liikumist.
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                # Muudame suuna paremale.
                uus_suund = "PAREM"

            # Kontrollime väljumist.
            if event.key == pygame.K_ESCAPE:
                # Sulgeme pygame'i.
                pygame.quit()

                # Sulgeme programmi.
                sys.exit()

            # Kontrollime uut mängu.
            if mang_labi and event.key == pygame.K_r:
                # Alustame mängu uuesti.
                uss, ussi_pea, suund, uus_suund, skoor, oun, maasikas, kivid = alusta_mang()

                # Määrame, et mäng ei ole läbi.
                mang_labi = False

    # Kui mäng on läbi.
    if mang_labi:
        # Täidame akna taustavärviga.
        aken.fill(taust)

        # Kuvame mängu lõpu teksti.
        kuva_tekst("MÄNG LÄBI", font_suur, punane, 220, 160)

        # Kuvame lõppskoori.
        kuva_tekst("Skoor: " + str(skoor), font_vaike, valge, 300, 240)

        # Kuvame uuesti alustamise juhise.
        kuva_tekst("R - uuesti   ESC - välju", font_vaike, valge, 220, 290)

        # Uuendame ekraani.
        pygame.display.update()

        # Jätame ülejäänud tsükli vahele.
        continue

    # Kontrollime, et uss ei läheks kohe vastassuunda.
    if uus_suund == "ULES" and suund != "ALLA":
        # Muudame suuna üles.
        suund = "ULES"

    # Kontrollime, et uss ei läheks kohe vastassuunda.
    if uus_suund == "ALLA" and suund != "ULES":
        # Muudame suuna alla.
        suund = "ALLA"

    # Kontrollime, et uss ei läheks kohe vastassuunda.
    if uus_suund == "VASAK" and suund != "PAREM":
        # Muudame suuna vasakule.
        suund = "VASAK"

    # Kontrollime, et uss ei läheks kohe vastassuunda.
    if uus_suund == "PAREM" and suund != "VASAK":
        # Muudame suuna paremale.
        suund = "PAREM"

    # Kui suund on üles.
    if suund == "ULES":
        # Liigutame pead üles.
        ussi_pea[1] -= ruut

    # Kui suund on alla.
    if suund == "ALLA":
        # Liigutame pead alla.
        ussi_pea[1] += ruut

    # Kui suund on vasak.
    if suund == "VASAK":
        # Liigutame pead vasakule.
        ussi_pea[0] -= ruut

    # Kui suund on parem.
    if suund == "PAREM":
        # Liigutame pead paremale.
        ussi_pea[0] += ruut

    # Lisame uue pea ussi ette.
    uss.insert(0, list(ussi_pea))

    # Kontrollime, kas uss sõi õuna.
    if ussi_pea == oun:
        # Lisame punkte.
        skoor += 10

        # Loome uue õuna.
        oun = juhuslik_koht(uss + kivid)

        # Kui skoor jagub 30-ga.
        if skoor % 30 == 0:
            # Loome maasika.
            maasikas = juhuslik_koht(uss + kivid + [oun])

    # Kontrollime, kas uss sõi maasika.
    elif maasikas is not None and ussi_pea == maasikas:
        # Lisame rohkem punkte.
        skoor += 30

        # Eemaldame maasika.
        maasikas = None

    # Kui uss ei söönud midagi.
    else:
        # Eemaldame saba.
        uss.pop()

    # Kontrollime vasakut ja paremat seina.
    if ussi_pea[0] < 0 or ussi_pea[0] > akna_laius - ruut:
        # Mäng saab läbi.
        mang_labi = True

    # Kontrollime ülemist ja alumist seina.
    if ussi_pea[1] < 40 or ussi_pea[1] > akna_korgus - ruut:
        # Mäng saab läbi.
        mang_labi = True

    # Käime läbi ussi keha.
    for kehaosa in uss[1:]:
        # Kontrollime, kas pea puudutab keha.
        if ussi_pea == kehaosa:
            # Mäng saab läbi.
            mang_labi = True

    # Käime läbi kõik kivid.
    for kivi in kivid:
        # Kontrollime, kas pea puudutab kivi.
        if ussi_pea == kivi:
            # Mäng saab läbi.
            mang_labi = True

    # Täidame tausta tumesinisega.
    aken.fill(taust)

    # Joonistame ülemise paneeli.
    pygame.draw.rect(aken, paneel, pygame.Rect(0, 0, akna_laius, 40))

    # Kuvame skoori.
    kuva_tekst("Skoor: " + str(skoor), font_vaike, valge, 15, 8)

    # Kuvame juhise.
    kuva_tekst("WASD/nooled | R pärast lõppu | ESC", font_vaike, valge, 260, 8)

    # Joonistame õuna.
    aken.blit(ouna_pilt, (oun[0], oun[1]))

    # Kontrollime, kas maasikas on olemas.
    if maasikas is not None:
        # Joonistame maasika.
        aken.blit(maasika_pilt, (maasikas[0], maasikas[1]))

    # Käime läbi kõik kivid.
    for kivi in kivid:
        # Joonistame kivi.
        aken.blit(kivi_pilt, (kivi[0], kivi[1]))

    # Käime läbi kõik ussi osad.
    for osa in uss:
        # Joonistame ussi lihtsa rohelise ruuduna.
        pygame.draw.rect(aken, roheline, pygame.Rect(osa[0], osa[1], ruut, ruut))

        # Joonistame ussi osale musta ääre.
        pygame.draw.rect(aken, must, pygame.Rect(osa[0], osa[1], ruut, ruut), 1)

    # Uuendame ekraani.
    pygame.display.update()

    # Hoiame mängu kiirust.
    kell.tick(kiirus)