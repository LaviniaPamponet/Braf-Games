﻿image elevador = "images/elevador.png"
image hipnose = "images/hipnose.gif"
image shunormal = "images/shunormal.png"
image templo = "images/templo.jpg"
image amuleto = "amuleto.png"
image logo = "logo.jpeg"

define c = Character ("Camila")
define s = Character ("Shu")

define points = 0

label start:


    #play music ambiente
    scene elevador at center with fade: 
        zoom 2

    c "Eu estava admirando o Elevador Lacerda, quando senti uma tontura. Ao mesmo tempo que senti algo me tocar."
    #stop music ambiente
    

    
    show hipnose at center:
        zoom 4
        yalign 0.5
       
    c "O que está acontecendo?"
    #play music suspense
    
    c "O que está acontecendo?"
    #stop music suspense
    
    jump fase2
    
label fase2:

    
    scene templo at center:
        zoom 2
        
    play music ambiente    
    c "Onde estou? Como vim parar aqui?"
    c "Parece um templo egípcio"
    
    s "Então você reconhece esse lugar."
    c "Quem disse isso?"
    
    s "Atrás de você"
    show shunormal at center:
        zoom 0.3
        yalign 0.07
        xalign 0.03
    
    menu:
        "Desculpe, mas não sei quem é o senhor, nem que lugar é esse.":
            s "Então é hora de descobrir."
        "Acho que talvez já tenha visto esse ambiente em alguma foto ou filme":
            $points = points + 1
            
    s "E eu? Já ouviu falar de mim?"
    menu:
        "Você se parece com o deus Shu.":
            s "Acho que você não conhece muito sobre os deuses do Egito."
        "Você seria o deus Geb?":
            $points = points + 1
            
    s "E o que você acha que eu faço? Você não veio parar aqui à toa. Então eu não vou lhe ajudar se você nem sequer me conhece."
    menu:
        "Você tem o poder da fertilidade da terra":
            $points = points + 1
        "Você faz a cura de doenças.":
            s "Tem certeza?"
        
    c "Acho que estou passando por um teste ou algo do tipo"
    s "Na verdade até eu não sei o que você está fazendo aqui. De onde você veio?"
    
    c "Apophis, o seu antigo nome era Salvador."
    s "E por que mudaram de nome? Você sabe o que significa esse nome?"
    menu: 
        "Apophis é o nome do Deus do Caos.":
            $points = points + 1
        "Apophis é o nome do Deus da Prosperidade.":
            s "Talvez você esteja aqui para aprender mais sobre uma cultura que você está inserida e não faz a mínima ideia."
            
    s "Já que você veio de um lugar chamado Apophis, me conte mais sobre. Tem muitos anos que não tenho contato com a humanidade"
    c "É um local muito devastado. Diziam que antigamente era possível se banhar nas praias de lá. Mas hoje, não podemos sequer pisar os pés na areia."
    s "E as pessoas? Como elas reagem a tudo?"
    c "Simplesmente não reagem. Elas estão ocupadas demais em sobreviver."
    s "Você já ouviu alguém comentar sobre o Deus Shu?"
    c "Dificilmente vejo alguém falando de religião e deuses."
    s "Em que ano você vive? Suas vestes são muito diferentes de qualquer outra que eu já tenha visto."
   
            
    s "Vou lhe propor um teste, caso passe. Terá direito à 4 desejos, além de conhecer outros deuses."
    #stop music ambiente
    
    call puzzle1
     
label puzzle1:
    
    s "Encontre meu amuleto escondido para ir para o próximo templo."
    show amuleto at center:
        yalign 0.5
        zoom 0.3
        
    
    show logo:
        zoom 0.2
    
    return
    
    

