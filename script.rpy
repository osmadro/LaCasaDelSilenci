# La Casa del Silenci - Joc de Terror amb Ren'Py
# Definició de personatges
define a = Character("Alex", color="#87CEEB")
define e = Character("Elena", color="#FFB6C1")
define m = Character("Dr. Moreno", color="#8B0000")
define v = Character("???", color="#4B0082")
define desc = Character(None, kind=nvl)

# Variables globals per controlar les decisions
default confianca_elena = 0
default investigacio_completa = 0
default objectes_recollits = 0
default moreno_enfadat = 0
default porta_oberta = False
default clau_trobada = False
default diari_llegit = False
default ritual_complet = False

# Imatges de fons (aquests són els backgrounds)
image bg entrada = "bg_entrada.jpg"
image bg rebedor = "bg_rebedor.jpg"
image bg escales = "bg_escales.jpg"
image bg dormitori = "bg_dormitori.jpg"
image bg sotano = "bg_sotano.jpg"
image bg biblioteca = "bg_biblioteca.jpg"
image bg cuina = "bg_cuina.jpg"
image bg despatx = "bg_despatx.jpg"
image bg ritual = "bg_ritual.jpg"
image bg final_bo = "bg_final_bo.jpg"

# Sprites de personatges (expressions diferents)
image elena normal = "elena_normal.png"
image elena triste = "elena_triste.png"
image elena sinistre = "elena_sinistre.png"
image moreno enfadat = "moreno_enfadat.png"
image moreno amenaçant = "moreno_amenaçant.png"
image ombra = "ombra.png"

# Etiqueta d'inici
label start:
    
    # Música de fons principal
    play music "tension_music.mp3" fadein 2.0
    
    scene bg entrada with fade
    
    a "Aquesta és la Casa Thornwood. Fa tres setmanes que ningú sap res de la Sara."
    
    a "La policia va tancar el cas massa ràpid. Jo sé que aquí hi ha alguna cosa estranya."
    
    # So ambiental
    play sound "porta_cruixent.mp3"
    
    a "La porta està mig oberta... Això no és normal."
    
    # DECISIÓ 1
    menu:
        "Entrar immediatament":
            jump entrar_directe
        
        "Trucar primer i esperar resposta":
            jump trucar_porta
            
label entrar_directe:
    $ investigacio_completa += 1
    
    a "No puc perdre temps. Cada minut compta."
    
    scene bg rebedor with dissolve
    
    a "El rebedor està ple de pols. Ningú ha estat aquí des de fa setmanes."
    
    jump explorar_rebedor

label trucar_porta:
    a "Hola? Hi ha algú?"
    
    play sound "trucar_porta.mp3"
    
    pause 2.0
    
    a "Silenci absolut. Millor entro amb precaució."
    
    scene bg rebedor with dissolve
    
    jump explorar_rebedor

label explorar_rebedor:
    
    scene bg rebedor
    
    a "Hi ha dues portes. Una porta a les escales, l'altra sembla anar cap a... alguna habitació."
    
    play sound "whisper.mp3"
    
    v "Ajuda'm..." 
    
    a "Què ha estat això?!"
    
    # DECISIÓ 2
    menu:
        "Seguir la veu misteriosa":
            $ confianca_elena += 1
            jump seguir_veu
            
        "Ignorar la veu i explorar sistemàticament":
            $ investigacio_completa += 1
            jump explorar_sistematic

label seguir_veu:
    
    a "Aquella veu... sonava desesperat. He de trobar d'on ve."
    
    scene bg biblioteca with dissolve
    
    play music "mystery_music.mp3" fadeout 1.0 fadein 2.0
    
    a "Una biblioteca... Plena de llibres antics."
    
    show elena normal with dissolve
    
    e "Finalment... algú ha vingut."
    
    a "Qui ets tu? Ets la Sara?"
    
    e "No... Jo sóc Elena. Estic atrapada aquí des de fa molt de temps."
    
    # DECISIÓ 3
    menu:
        "Confiar en Elena i demanar ajuda":
            $ confianca_elena += 2
            jump confiar_elena
            
        "Desconfiar i fer preguntes":
            $ investigacio_completa += 1
            jump desconfiar_elena

label explorar_sistematic:
    
    a "No puc deixar-me portar per veus estranyes. He de ser metòdic."
    
    scene bg cuina with dissolve
    
    a "La cuina... Hi ha plats bruts des de fa setmanes."
    
    play sound "porta_obrir.mp3"
    
    a "Un diari! Pot tenir pistes."
    
    $ diari_llegit = True
    $ objectes_recollits += 1
    
    a "'Dia 15: El Dr. Moreno s'ha tornat estrany. Parla sol i fa rituals estranys al soterrani...'"
    
    a "Això és pertorbador. He de trobar aquest soterrani."
    
    jump trobar_sotano

label confiar_elena:
    
    e "Gràcies per confiar en mi, Alex. Necessito la teva ajuda."
    
    show elena triste
    
    e "El Dr. Moreno, l'antic propietari, va fer un ritual terrible. Ara ell controla aquesta casa."
    
    a "I la Sara? L'has vista?"
    
    e "Està al soterrani... però encara és viva. Ell la manté per completar el ritual."
    
    # DECISIÓ 4
    menu:
        "Anar directament al soterrani a salvar la Sara":
            $ moreno_enfadat += 2
            jump sotano_directe
            
        "Buscar més informació abans d'actuar":
            $ investigacio_completa += 1
            jump buscar_informacio

label desconfiar_elena:
    
    a "Com puc saber que dius la veritat? Pots ser una trampa."
    
    show elena sinistre
    
    e "Trampa? Jo porto dècades atrapada aquí! Tu no entens res!"
    
    $ confianca_elena -= 1
    
    a "Calma... només vull estar segur."
    
    hide elena with dissolve
    
    a "S'ha desaparegut... Això no és bo."
    
    jump explorar_pis_superior

label trobar_sotano:
    
    scene bg rebedor
    
    a "Segons el diari, hi ha una porta oculta al rebedor que porta al soterrani."
    
    play sound "buscar.mp3"
    
    a "Aquí! Una porta dissimulada darrere del quadre!"
    
    $ porta_oberta = True
    
    scene bg sotano with fade
    
    play music "terror_music.mp3" fadeout 1.0 fadein 1.0
    
    a "Fa molt de fred aquí baix... I hi ha olor de podrit."
    
    jump encontrar_sara

label sotano_directe:
    
    scene bg escales with dissolve
    
    a "He de baixar al soterrani ara mateix!"
    
    scene bg sotano with fade
    
    play music "terror_music.mp3" fadeout 1.0 fadein 1.0
    
    play sound "riure_malvat.mp3"
    
    show moreno amenaçant with vpunch
    
    m "Així que has vingut a destorbar el meu treball..."
    
    a "Dr. Moreno! On està la Sara?!"
    
    jump confrontacio_moreno

label buscar_informacio:
    
    e "Si vols ajudar-la, necessitem tres coses: el diari, la clau antiga, i els símbols de protecció."
    
    a "On puc trobar això?"
    
    e "El diari és a la cuina, la clau al dormitori, i els símbols al despatx."
    
    # DECISIÓ 5
    menu:
        "Anar primer a la cuina":
            jump explorar_cuina
            
        "Anar primer al dormitori":
            jump explorar_dormitori
            
        "Anar primer al despatx":
            jump explorar_despatx

label explorar_pis_superior:
    
    scene bg escales with dissolve
    
    a "Millor pujar al pis superior. Potser trobo alguna cosa útil."
    
    scene bg dormitori with dissolve
    
    a "Un dormitori... Hi ha sangre a les parets!"
    
    play sound "scream.mp3"
    
    show ombra with hpunch
    
    a "Què és això?!"
    
    hide ombra with dissolve
    
    # DECISIÓ 6
    menu:
        "Fugir corrents cap avall":
            $ moreno_enfadat += 1
            jump fugir_avall
            
        "Quedar-se i investigar":
            $ investigacio_completa += 1
            $ clau_trobada = True
            $ objectes_recollits += 1
            jump investigar_dormitori

label explorar_cuina:
    
    scene bg cuina with dissolve
    
    a "La cuina està molt bruta..."
    
    play sound "buscar.mp3"
    
    a "Aquí està el diari!"
    
    $ diari_llegit = True
    $ objectes_recollits += 1
    
    a "'El ritual necessita una ànima pura per alliberar el Dr. Moreno de la seva maledicció...'"
    
    jump continuar_busqueda

label explorar_dormitori:
    
    scene bg dormitori with dissolve
    
    a "Aquest dormitori té un aspecte sinistre..."
    
    play sound "buscar.mp3"
    
    a "Una clau antiga sota el matalàs!"
    
    $ clau_trobada = True
    $ objectes_recollits += 1
    
    jump continuar_busqueda

label explorar_despatx:
    
    scene bg despatx with dissolve
    
    a "El despatx del Dr. Moreno... Està ple de llibres d'ocultisme."
    
    play sound "buscar.mp3"
    
    a "Símbols de protecció! Aquests poden ser útils."
    
    $ objectes_recollits += 1
    
    jump continuar_busqueda

label continuar_busqueda:
    
    # DECISIÓ 7 - Continuar recollint objectes
    if objectes_recollits < 3:
        menu:
            "Continuar buscant els altres objectes":
                if not diari_llegit:
                    jump explorar_cuina
                elif not clau_trobada:
                    jump explorar_dormitori
                else:
                    jump explorar_despatx
                    
            "Anar directament al soterrani":
                jump sotano_amb_objectes
    else:
        a "Ja tinc tot el que necessito. És hora d'anar al soterrani."
        jump sotano_amb_objectes

label fugir_avall:
    
    scene bg rebedor with dissolve
    
    a "He de sortir d'aquí!"
    
    play sound "riure_malvat.mp3"
    
    show moreno enfadat with vpunch
    
    m "No pots fugir de la meva casa!"
    
    jump confrontacio_moreno

label investigar_dormitori:
    
    a "No puc tenir por... He de descobrir què està passant."
    
    play sound "buscar.mp3"
    
    a "Una clau antiga! Pot obrir alguna cosa important."
    
    scene bg escales with dissolve
    
    a "Baixem amb precaució..."
    
    jump trobar_sotano

label sotano_amb_objectes:
    
    scene bg sotano with fade
    
    play music "terror_music.mp3" fadeout 1.0 fadein 1.0
    
    a "El soterrani... Aquest és el lloc del ritual."
    
    jump encontrar_sara

label encontrar_sara:
    
    a "Sara! Estàs aquí?"
    
    "Sara" "Ajuda'm... si us plau..."
    
    a "Estic aquí! Et trauré d'aquí!"
    
    play sound "riure_malvat.mp3"
    
    show moreno amenaçant with vpunch
    
    m "No deixaré que destrossis els meus plans!"
    
    jump confrontacio_moreno

label confrontacio_moreno:
    
    show moreno enfadat
    
    m "Fa cent anys que espero aquest moment! Necessito una ànima per tornar a la vida!"
    
    show elena normal at right
    
    e "Alex! Ara és el moment! Hem de decidir!"
    
    # DECISIÓ 8 - Decisió crucial
    if objectes_recollits >= 3 and confianca_elena >= 2:
        menu:
            "Utilitzar els símbols de protecció i el ritual del diari":
                $ ritual_complet = True
                jump ritual_exit
                
            "Atacar directament a Moreno":
                jump atacar_moreno
    else:
        menu:
            "Intentar negociar amb Moreno":
                jump negociar_moreno
                
            "Intentar fugir amb la Sara":
                jump fugir_sara

label ritual_exit:
    
    scene bg ritual with fade
    
    play music "ritual_music.mp3" fadeout 1.0 fadein 1.0
    
    a "Utilitzaré els símbols i les paraules del diari!"
    
    play sound "magia.mp3"
    
    a "Per la llum que dissipa la foscor, t'ordeno que marxis!"
    
    show moreno amenaçant with hpunch
    
    m "NOOOO! EL MEU PODER!"
    
    hide moreno with dissolve
    
    show elena triste
    
    e "Gràcies, Alex... Finalment sóc lliure..."
    
    # DECISIÓ 9
    menu:
        "Ajudar Elena a trobar la pau":
            $ confianca_elena += 2
            jump final_bo_complet
            
        "Marxar immediatament amb la Sara":
            jump final_acceptable

label atacar_moreno:
    
    a "No tinc temps per rituals! Aniré directe!"
    
    show moreno amenaçant with hpunch
    
    m "Insolent!"
    
    play sound "atac.mp3"
    
    a "Agh!"
    
    # DECISIÓ 10
    if investigacio_completa >= 3:
        a "Espera... recordo el que deia el diari sobre la seva debilitat!"
        jump usar_debilitat
    else:
        a "Sóc massa feble..."
        jump final_dolent

label negociar_moreno:
    
    a "Dr. Moreno, potser podem arribar a un acord..."
    
    show moreno enfadat
    
    m "Acord? L'únic acord és que tu prendràs el lloc de la Sara!"
    
    play sound "atac.mp3"
    
    a "No!"
    
    jump final_dolent

label fugir_sara:
    
    a "Sara! Corre!"
    
    play sound "correr.mp3"
    
    "Sara" "No puc moure'm!"
    
    show moreno amenaçant with vpunch
    
    m "Ningú marxa d'aquí!"
    
    if confianca_elena >= 1:
        show elena normal
        e "Alex! Agafa la meva mà!"
        jump escapar_amb_elena
    else:
        jump final_dolent

label usar_debilitat:
    
    a "La clau antiga! És el vincle amb aquest món!"
    
    play sound "trencar.mp3"
    
    a "Trenc la clau!"
    
    show moreno enfadat with hpunch
    
    m "NOOOOOO!"
    
    hide moreno with dissolve
    
    jump final_acceptable

label escapar_amb_elena:
    
    play sound "magia.mp3"
    
    e "Us protegeixo!"
    
    scene bg entrada with fade
    
    play music "calm_music.mp3" fadeout 2.0 fadein 2.0
    
    a "Ho hem aconseguit... Som fora."
    
    show elena triste
    
    e "Gràcies per salvar la Sara... Jo ja puc descansar."
    
    hide elena with dissolve
    
    jump final_acceptable

label final_bo_complet:
    
    scene bg final_bo with fade
    
    play music "final_music.mp3" fadeout 2.0 fadein 2.0
    
    a "La Sara està a salva, Elena ha trobat la pau, i el Dr. Moreno ja no pot fer mal."
    
    a "La Casa Thornwood finalment està en silenci... un silenci pacífic."
    
    "Has aconseguit el millor final! - Final A: La Redempció"
    
    return

label final_acceptable:
    
    scene bg entrada with fade
    
    play music "calm_music.mp3" fadeout 2.0 fadein 2.0
    
    a "La Sara està a salva. Això és el que importa."
    
    a "Però sento que alguna cosa queda inacabada a aquesta casa..."
    
    "Has aconseguit un final acceptable - Final B: L'Escapada"
    
    return

label final_dolent:
    
    scene black with fade
    
    stop music fadeout 2.0
    
    play sound "scream.mp3"
    
    "La foscor t'envolta..."
    
    "Ara formes part de la Casa Thornwood... per sempre."
    
    "Final C: L'Atrapament"
    
    return
