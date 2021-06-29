from random import randint

# Mago
vida_max_mago = randint(10, 20)
mana_max = randint(5, 10)
vida_max_guerreiro = randint(15, 25)
est_max = randint(5, 15)

# Monstro
vida_max_monstro = 20

nome = input('Qual é o nome do seu aventureiro?'
             '\n---> ')
print('Wow! Que belo nome')
print('=-' * 40)
classe = input(f'Agora escolha uma classe\n'
               f'Opções:'
               f'\n1-Mago'
               f'\n2-Guerreiro'
               f'\n---> ').lower()
print('=-' * 40)
if classe == 'mago' or classe == '1':
    print(f'Você escolheu a classe mago, você possui {vida_max_mago} de vida e '
          f'\n{mana_max} de mana')
if classe == 'guerreiro' or classe == '2':
    print(f'Você escolheu a classe guerreiro, você possui {vida_max_guerreiro} de vida e '
          f'\n{est_max} de estamina')

print(f'Olá {nome}, blá blá blá historinha desnecessária....')
if classe == 'mago' or classe == '1':
    num_monstro = 1
    num_chefao = 1
    chefao = 11
    atk_min = 0
    atk_max = 5
    atk_monstro = 2
    while True:
        mana = mana_max
        vida = vida_max_mago
        vida_monstro = vida_max_monstro
        print(f'Wow, Acaba de aparecer um monstro!!!! (0 c 0)')
        rd = 1
        while vida_monstro > 0:
            acao_monstro = randint(0, 2)
            print('=-' * 40)
            print(f'\n\n R O D A D A #{rd}\n')
            print('=-' * 40)
            print(f'\nStatus do Monstro:'
                  f'\nMonstro N°#{num_monstro} vida: [{vida_monstro}/{vida_max_monstro}] '
                  f'\nAtaque: [Defende um terço do dano recebido]')
            print('=-' * 40)
            action = input(f'{nome} [vida: {vida}/{vida_max_mago}]'
                           f'\nOpções de ações:'
                           f'\n1- Ataque'
                           f'\n2- Curar'
                           f'\n3- Defesa'
                           f'\n4- Descansar ----->  ').lower()  # .lower() => transforma o valor digitado em minúsculo
            print('=-' * 40)

            # Ataque do personagem e cura do monstro
            if mana >= 2:
                if action == 'ataque' or action == '1':
                    atk = 10  # randint(atk_min, atk_max)
                    mana -= 2
                    gelo = randint(1, 10)
                    if gelo == 10:
                        print('Wow!!! Voê congelou o monstro, deixando o sem reação'
                              '\npor 1 rodada!')
                        acao_monstro = 0
                    if acao_monstro == 2:
                        dfs_monstro = int(atk / 3)
                        print('O monstro defendeu o seu ataque')
                        print(f'Por isso você deu apenas {dfs_monstro} de dano no monstro!')
                        vida_monstro -= dfs_monstro
                    else:
                        print(f'Wow!!! Você acaba de dar {atk} de dano no monstro!!!')
                        vida_monstro -= atk

                        # if/else corrigindo o bug do monstro com vida negativa
                        if vida_monstro >= 1:
                            print(f'Deixando ele com {vida_monstro} de vida!!!'
                                  f'\nPorém acabou gastando 2 de mana nesse'
                                  f'\nataque, ficando com {mana} de mana')
                        else:
                            print('=-' * 40)
                            seg = input(f'Deseja continuar? (s/n)').lower()
                            if seg == 's' or seg == 'sim':
                                print(f'Você {nome}, esse(a) bravo(a) e destemido(a) mago(a) derrotou '
                                      f'\no horrendo monstro e salvou as pessoas novamente! '
                                      f'\nParabéns nobre mago(a), agora você pode '
                                      f'\nseguir sua jornada!')
                                vida_max_mago += 5
                                atk_min += 5
                                atk_max += 5
                                vida_max_monstro += 10
                                atk_monstro += 3
                                num_monstro += 1
                            else:
                                print(f'Você {nome}, esse(a) bravo(a) e destemido(a) mago(a) derrotou '
                                      f'\no horrendo monstro e salvou as pessoas novamente! '
                                      f'\nParabéns nobre mago(a), nos vemos em breve!')
                                exit()
                elif action != 'ataque' or action != '1' and acao_monstro == 2:
                    print('O monstro usou de defesa!')
            else:
                print(f'Putz!!! Você não possui mana suficiente,'
                      f'\ndescanse para recuperar mana')

            # Cura do personagem
            if mana >= 2:
                if action == 'curar' or action == '2':
                    cura = randint((int(vida / 10)), (int(vida / 2.5)))
                    new_vida = vida + cura
                    mana -= 2

                    # if/else corrigindo o bug da vida excedendo 50 de HP
                    if new_vida > vida_max_mago:
                        cura = vida_max_mago - vida
                        new_vida_curada = vida + cura
                        print(f'Como?!??!?'
                              f'\nVocê acaba de recuperar {cura} de vida,'
                              f'\nantes você tinha {vida} de vida, mas agora acaba de ter {new_vida_curada}'
                              f'\nPorém acabou gastando 2 de mana nesse'
                              f'\nprocesso, ficando com {mana} de mana')
                        vida = vida_max_mago
                    else:
                        print(f'Como?!??!?'
                              f'\nVocê acaba de recuperar {cura} de vida,'
                              f'\nantes você tinha {vida} de vida, mas agora acaba de ter {new_vida}')
                        vida = new_vida
                        print(f'\nPorém acabou gastando 2 de mana nesse'
                              f'\nprocesso, ficando com {mana} de mana')
            else:
                print(f'Putz!!! Você não possui mana suficiente,'
                      f'\ndescanse para recuperar mana')

            if action == 'descansar' or action == '4':
                descansar = randint(1, 7)
                new_mana = mana + descansar
                if new_mana > mana_max:
                    descansar = mana_max - mana
                    new_mana = mana + descansar
                    print(f'Você olhou pro monstro e correu mata adentro'
                          f'\nNisso você resolve meditar e recupera '
                          f'\níncriveis {descansar} de mana,'
                          f'\ntotalizando {new_mana} de mana')
                    mana = new_mana
                else:
                    print(f'Você olhou pro monstro e correu mata adentro'
                          f'\nNisso você resolve meditar e recupera '
                          f'\níncriveis {descansar} de mana,'
                          f'\ntotalizando {new_mana} de mana')
                mana = new_mana

            # Ataque do monstro e defesa do personagem
            if acao_monstro == 1:
                print('=-' * 40)

                # A ação de defesa está aqui porque só é possível defender quando o monstro ataca
                if mana >= 2:
                    if action == 'defesa' or action == '3':
                        defesa = int(atk_monstro / 2)
                        print('Nossa que defesa!!!')
                        print(f'Você sofreu apenas {defesa} de dano após essa defesa espetacular!')
                        vida -= defesa
                        mana -= 2
                        print(f'Porém você gastou 2 de mana nessa ação,'
                              f'\nficando com {mana} de mana')

                    else:
                        print(f'O monstro te deu {atk_monstro} de dano ')
                        vida -= atk_monstro

                    # Morte do personagem
                    if vida <= 0:
                        print('=-' * 40)
                        print("Infelizmente você morreu após essa árdua batalha!!!")
                        exit()
                    else:
                        print(f'Sua vida agora é {vida}')
                else:
                    print(f'Putz!!! Você não possui mana suficiente,'
                          f'\ndescanse para recuperar mana')
                    print(f'O monstro te deu {atk_monstro} de dano ')
                    vida -= atk_monstro
                    # Morte do personagem
                    if vida <= 0:
                        print('=-' * 40)
                        print("Infelizmente você morreu após essa árdua batalha!!!")
                        exit()
                    else:
                        print(f'Sua vida agora é {vida}')
            rd += 1
            mana += 1
            if mana < mana_max:
                print(f'Você recuperou 1 de mana, totalizando {mana} de mana')
            elif mana == mana_max:
                mana = mana_max
                print(f'Você possui {mana} de mana')

        if num_monstro == chefao:
            vida_max_chefao = vida_monstro * 3
            vida_chefao = vida_max_chefao
            atk_chefao = atk_monstro * 3
            rd = 1
            while vida_chefao > 0:
                acao_chefao = randint(0, 2)
                print('=-' * 40)
                print(f'\n\n R O D A D A #{rd}\n')
                print('=-' * 40)
                print(f'\nStatus do Chefão:'
                      f'\nChefão N°#{num_chefao} vida: [{vida_chefao}/{vida_max_chefao}] '
                      f'\nAtaque: [Defende um terço do dano recebido]')
                print('=-' * 40)
                action = input(f'{nome} [vida: {vida}/{vida_max_mago}]'
                               f'\nOpções de ações:'
                               f'\n1- Ataque'
                               f'\n2- Curar'
                               f'\n3- Defesa'
                               f'\n4- Descansar ----->  ').lower()  # .lower() => transforma o valor digitado em minúsculo
                print('=-' * 40)

                # Ataque do personagem e cura do monstro
                if mana >= 2:
                    if action == 'ataque' or action == '1':
                        atk = randint(atk_min, atk_max)
                        mana -= 2
                        gelo = randint(1, 10)
                        if gelo == 10:
                            print("Wow!!! Você congelou o chefão, deixando"
                                  "\nele sem ação durante 1 rodada!")
                            acao_chefao = 0
                        if acao_chefao == 2:
                            dfs_chefao = int(atk / 3)
                            print('O chefão defendeu o seu ataque')
                            print(f'Por isso você deu apenas {dfs_chefao} de dano nele!')
                            vida_chefao -= dfs_chefao
                        else:
                            print(f'Wow!!! Você acaba de dar {atk} de dano no chefão!!!')
                            vida_chefao -= atk

                            # if/else corrigindo o bug do monstro com vida negativa
                            if vida_chefao >= 1:
                                print(f'Deixando ele com {vida_chefao} de vida!!!'
                                      f'\nPorém acabou gastando 2 de mana nesse'
                                      f'\nataque, ficando com {mana} de mana')
                            else:
                                print('=-' * 40)
                                seg = input(f'Deseja continuar? (s/n)').lower()
                                if seg == 's' or seg == 'sim':
                                    print(f'Você {nome}, esse(a) bravo(a) e destemido(a) mago(a) derrotou '
                                          f'\n o horrendo chefão e salvou as pessoas novamente! '
                                          f'\nParabéns nobre mago(a), agora você pode '
                                          f'\nseguir sua jornada!')
                                    vida_max_mago += 5
                                    atk_min += 5
                                    atk_max += 5
                                    vida_max_monstro += 10
                                    atk_monstro += 3
                                    num_monstro += 1
                                    chefao += 10
                                    num_chefao += 1
                                else:
                                    print(f'Você {nome}, esse(a) bravo(a) e destemido(a) mago(a) derrotou '
                                          f'\n o horrendo monstro e salvou as pessoas novamente! '
                                          f'\nParabéns nobre mago(a), nos vemos em breve!')
                                    exit()
                    elif action != 'ataque' or action != '1' and acao_chefao == 2:
                        print('O chefão usou de defesa!')
                else:
                    print(f'Putz!!! Você não possui mana suficiente,'
                          f'\ndescanse para recuperar mana')

                # Cura do personagem
                if mana >= 2:
                    if action == 'curar' or action == '2':
                        cura = randint((int(vida / 10)), (int(vida / 2.5)))
                        new_vida = vida + cura
                        mana -= 2

                        # if/else corrigindo o bug da vida excedendo 50 de HP
                        if new_vida > vida_max_mago:
                            cura = vida_max_mago - vida
                            new_vida_curada = vida + cura
                            print(f'Como?!??!?'
                                  f'\nVocê acaba de recuperar {cura} de vida,'
                                  f'\nantes você tinha {vida} de vida, mas agora acaba de ter {new_vida_curada}'
                                  f'\nPorém acabou gastando 2 de mana nesse'
                                  f'\nprocesso, ficando com {mana} de mana')
                            vida = vida_max_mago
                        else:
                            print(f'Como?!??!?'
                                  f'\nVocê acaba de recuperar {cura} de vida,'
                                  f'\nantes você tinha {vida} de vida, mas agora acaba de ter {new_vida}'
                                  f'\nPorém acabou gastando 2 de mana nesse'
                                  f'\nprocesso, ficando com {mana} de mana')
                            vida = new_vida
                else:
                    print(f'Putz!!! Você não possui mana suficiente,'
                          f'\ndescanse para recuperar mana')

                if action == 'descansar' or action == '4':
                    descansar = randint(1, 7)
                    new_mana = mana + descansar
                    if new_mana > mana_max:
                        descansar = mana_max - mana
                        new_mana = mana + descansar
                        print(f'Você olhou pro chefão e correu mata adentro'
                              f'\nNisso você resolve meditar e recupera '
                              f'\níncriveis {descansar} de mana,'
                              f'\ntotalizando {new_mana} de mana')
                    else:
                        print(f'Você olhou pro chefao e correu mata adentro'
                              f'\nNisso você resolve meditar e recupera '
                              f'\níncriveis {descansar} de mana,'
                              f'\ntotalizando {new_mana} de mana')

                # Ataque do monstro e defesa do personagem
                if acao_chefao == 1:
                    print('=-' * 40)

                    # A ação de defesa está aqui porque só é possível defender quando o monstro ataca
                    if mana >= 2:
                        if action == 'defesa' or action == '3':
                            defesa = int(atk_chefao / 2)
                            mana -= 2
                            print('Nossa que defesa!!!')
                            print(f'Você sofreu apenas {defesa} de dano após essa defesa espetacular!'
                                  f'\nPorém acabou gastando 2 de mana nesse'
                                  f'\nprocesso, ficando com {mana} de mana')
                            vida -= defesa
                        else:
                            print(f'O monstro te deu {atk_chefao} de dano ')
                            vida -= atk_chefao

                        # Morte do personagem
                        if vida <= 0:
                            print('=-' * 40)
                            print("Infelizmente você morreu após essa árdua batalha!!!")
                            exit()
                        else:
                            print(f'Sua vida agora é {vida}')
                    else:
                        print(f'Putz!!! Você não possui mana suficiente,'
                              f'\ndescanse para recuperar mana')
                        print(f'O monstro te deu {atk_chefao} de dano ')
                        vida -= atk_chefao
                        # Morte do personagem
                        if vida <= 0:
                            print('=-' * 40)
                            print("Infelizmente você morreu após essa árdua batalha!!!")
                            exit()
                        else:
                            print(f'Sua vida agora é {vida}')
                rd += 1
                mana += 1
                if mana < mana_max:
                    print(f'Você recuperou 1 de mana, totalizando {mana} de mana')
                else:
                    mana = mana_max
                    print(f'Você possui {mana} de mana')
if classe == 'guerreiro' or classe == '2':
    num_monstro = 1
    num_chefao = 1
    chefao = 11
    atk_min = 0
    atk_max = 5
    atk_monstro = 2
    while True:
        estamina = est_max
        vida = vida_max_guerreiro
        vida_monstro = vida_max_monstro
        print(f'Whow, Acaba de aparecer um monstro!!!! (0 c 0)')
        rd = 1
        while vida_monstro > 0:
            acao_monstro = randint(0, 2)
            print('=-' * 40)
            print(f'\n\n R O D A D A #{rd}\n')
            print('=-' * 40)
            print(f'\nStatus do Monstro:'
                  f'\nMonstro N°#{num_monstro} vida: [{vida_monstro}/{vida_max_monstro}] '
                  f'\nAtaque: [Defende um terço do dano recebido]')
            print('=-' * 40)
            action = input(f'{nome} [vida: {vida}/{vida_max_guerreiro}]'
                           f'\nOpções de ações:'
                           f'\n1- Ataque'
                           f'\n2- Curar'
                           f'\n3- Defesa'
                           f'\n4- Descansar ----->  ').lower()  # .lower() => transforma o valor digitado em minúsculo
            print('=-' * 40)

            # Ataque do personagem e cura do monstro
            if estamina >= 2:
                if action == 'ataque' or action == '1':
                    atk = randint(atk_min, atk_max)
                    estamina -= 2
                    if acao_monstro == 2:
                        dfs_monstro = int(atk / 3)
                        print('O monstro defendeu o seu ataque')
                        print(f'Por isso você deu apenas {dfs_monstro} de dano no monstro!')
                        vida_monstro -= dfs_monstro
                    else:
                        print(f'Wow!!! Você acaba de dar {atk} de dano no monstro!!!')
                        vida_monstro -= atk

                        # if/else corrigindo o bug do monstro com vida negativa
                        if vida_monstro >= 1:
                            print(f'Deixando ele com {vida_monstro} de vida!!!'
                                  f'\nPorém acabou gastando 2 de estamina nesse'
                                  f'\nataque, ficando com {estamina} de mana')
                        else:
                            print('=-' * 40)
                            seg = input(f'Deseja continuar? (s/n)').lower()
                            if seg == 's' or seg == 'sim':
                                print(f'Você {nome}, esse(a) bravo(a) e destemido(a) guerreiro(a) derrotou '
                                      f'\n o horrendo monstro e salvou as pessoas novamente! '
                                      f'\nParabéns nobre guerreiro(a), agora você pode '
                                      f'\nseguir sua jornada!')
                                vida_max_guerreiro += 5
                                atk_min += 5
                                atk_max += 5
                                vida_max_monstro += 10
                                atk_monstro += 3
                                num_monstro += 1
                            else:
                                print(f'Você {nome}, esse(a) bravo(a) e destemido(a) guerreiro(a) derrotou '
                                      f'\n o horrendo monstro e salvou as pessoas novamente! '
                                      f'\nParabéns nobre guerreiro(a), nos vemos em breve!')
                                exit()
                elif action != 'ataque' or action != '1' and acao_monstro == 2:
                    print('O monstro usou de defesa!')
            else:
                print(f'Putz!!! Você não possui estamina suficiente,'
                      f'\ndescanse para recuperar estamina')

            # Cura do personagem
            if estamina >= 2:
                if action == 'curar' or action == '2':
                    cura = randint(int(vida / 10), int(vida / 2.5))
                    new_vida = vida + cura
                    estamina -= 2

                    # if/else corrigindo o bug da vida excedendo 50 de HP
                    if new_vida > vida_max_guerreiro:
                        cura = vida_max_guerreiro - vida
                        new_vida_curada = vida + cura
                        print(f'Como?!??!?'
                              f'\nVocê acaba de recuperar {cura} de vida,'
                              f'\nantes você tinha {vida} de vida, mas agora acaba de ter {new_vida_curada}'
                              f'\nPorém acabou gastando 2 de estamina nesse'
                              f'\nprocesso, ficando com {estamina} de estamina')
                        vida = vida_max_guerreiro
                    else:
                        print(f'Como?!??!?'
                              f'\nVocê acaba de recuperar {cura} de vida,'
                              f'\nantes você tinha {vida} de vida, mas agora acaba de ter {new_vida}'
                              f'\nPorém acabou gastando 2 de estamina nesse'
                              f'\nprocesso, ficando com {estamina} de estamina')
                        vida = new_vida
            else:
                print(f'Putz!!! Você não possui estamina suficiente,'
                      f'\ndescanse para recuperar estamina')

            if action == 'descansar' or action == '4':
                descansar = randint(1, 7)
                new_est = estamina + descansar
                if new_est > mana_max:
                    descansar = est_max - estamina
                    new_est = estamina + descansar
                    print(f'Você olhou pro monstro e correu mata adentro'
                          f'\nNisso você resolve descansar e recupera '
                          f'\níncriveis {descansar} de estamina,'
                          f'\ntotalizando {new_est} de estamina')
                else:
                    print(f'Você olhou pro monstro e correu mata adentro'
                          f'\nNisso você resolve meditar e recupera '
                          f'\níncriveis {descansar} de estamina,'
                          f'\ntotalizando {new_est} de estamina')

            # Ataque do monstro e defesa do personagem
            if acao_monstro == 1:
                print('=-' * 40)

                # A ação de defesa está aqui porque só é possível defender quando o monstro ataca
                if estamina >= 2:
                    if action == 'defesa' or action == '3':
                        estamina -= 2
                        defesa = int(atk_monstro / 2)
                        print('Nossa que defesa!!!')
                        print(f'Você sofreu apenas {defesa} de dano após essa defesa espetacular!'
                              f'Porém acabou gastando 2 de estamina nessa ação,'
                              f'\nficando com {estamina} de estamina')
                        vida -= defesa
                    else:
                        print(f'O monstro te deu {atk_monstro} de dano ')
                        vida -= atk_monstro

                    # Morte do personagem
                    if vida <= 0:
                        print('=-' * 40)
                        print("Infelizmente você morreu após essa árdua batalha!!!")
                        exit()
                    else:
                        print(f'Sua vida agora é {vida}')
                else:
                    print(f'Putz!!! Você não possui estamina suficiente,'
                          f'\ndescanse para recuperar estamina')
                    print(f'O monstro te deu {atk_monstro} de dano ')
                    vida -= atk_monstro
                    # Morte do personagem
                    if vida <= 0:
                        print('=-' * 40)
                        print("Infelizmente você morreu após essa árdua batalha!!!")
                        exit()
                    else:
                        print(f'Sua vida agora é {vida}')
            rd += 1
            estamina += 1
            if estamina < est_max:
                print(f'Você recuperou 1 de estamina, totalizando {estamina} de estamina')
            else:
                estamina = est_max
                print(f'Você possui {estamina} de estamina')
        if num_monstro == chefao:
            vida_max_chefao = vida_monstro * 3
            vida_chefao = vida_max_chefao
            atk_chefao = atk_monstro * 3
            rd = 1
            while vida_chefao > 0:
                acao_chefao = randint(1, 2)
                print('=-' * 40)
                print(f'\n\n R O D A D A #{rd}\n')
                print('=-' * 40)
                print(f'\nStatus do Chefão:'
                      f'\nChefão N°#{num_chefao} vida: [{vida_chefao}/{vida_max_chefao}] '
                      f'\nAtaque: [Defende um terço do dano recebido]')
                print('=-' * 40)
                action = input(f'{nome} [vida: {vida}/{vida_max_guerreiro}]'
                               f'\nOpções de ações:'
                               f'\n1- Ataque'
                               f'\n2- Curar'
                               f'\n3- Defesa'
                               f'\n4- Descansar ----->  ').lower()  # .lower() => transforma o valor digitado em minúsculo
                print('=-' * 40)

                # Ataque do personagem e cura do monstro
                if estamina >= 2:
                    if action == 'ataque' or action == '1':
                        atk = randint(atk_min, atk_max)
                        estamina -= 2
                        if acao_chefao == 2:
                            dfs_chefao = int(atk / 3)
                            print('O chefão defendeu o seu ataque')
                            print(f'Por isso você deu apenas {dfs_chefao} de dano nele!')
                            vida_chefao -= dfs_chefao
                        else:
                            print(f'Wow!!! Você acaba de dar {atk} de dano no chefão!!!')
                            vida_chefao -= atk

                            # if/else corrigindo o bug do monstro com vida negativa
                            if vida_chefao >= 1:
                                print(f'Deixando ele com {vida_chefao} de vida!!!'
                                      f'\nPorém acabou gastando 2 de estamina nesse'
                                      f'\nataque, ficando com {estamina} de estamina')
                            else:
                                print('=-' * 40)
                                seg = input(f'Deseja continuar? (s/n)').lower()
                                if seg == 's' or seg == 'sim':
                                    print(f'Você {nome}, esse(a) bravo(a) e destemido(a) guerreiro(a) derrotou '
                                          f'\n o horrendo chefão e salvou as pessoas novamente! '
                                          f'\nParabéns nobre guerreiro(a), agora você pode '
                                          f'\nseguir sua jornada!')
                                    vida_max_guerreiro += 5
                                    atk_min += 5
                                    atk_max += 5
                                    vida_max_monstro += 10
                                    atk_monstro += 3
                                    num_monstro += 1
                                    chefao += 10
                                    num_chefao += 1
                                else:
                                    print(f'Você {nome}, esse(a) bravo(a) e destemido(a) guerreiro(a) derrotou '
                                          f'\n o horrendo monstro e salvou as pessoas novamente! '
                                          f'\nParabéns nobre guerreiro(a), nos vemos em breve!')
                                    exit()
                    elif action != 'ataque' or action != '1' and acao_chefao == 2:
                        print('O chefão usou de defesa!')
                else:
                    print(f'Putz!!! Você não possui estamina suficiente,'
                          f'\ndescanse para recuperar estamina')

                # Cura do personagem
                if estamina >= 2:
                    if action == 'curar' or action == '2':
                        cura = randint(int(vida / 10), int(vida / 2.5))
                        new_vida = vida + cura
                        estamina -= 2

                        # if/else corrigindo o bug da vida excedendo 50 de HP
                        if new_vida > vida_max_guerreiro:
                            cura = vida_max_guerreiro - vida
                            new_vida_curada = vida + cura
                            print(f'Como?!??!?'
                                  f'\nVocê acaba de recuperar {cura} de vida,'
                                  f'\nantes você tinha {vida} de vida, mas agora acaba de ter {new_vida_curada}'
                                  f'\nPorém acabou gastando 2 de estamina nesse'
                                  f'\nprocesso, ficando com {estamina} de estamina')
                            vida = vida_max_guerreiro
                        else:
                            print(f'Como?!??!?'
                                  f'\nVocê acaba de recuperar {cura} de vida,'
                                  f'\nantes você tinha {vida} de vida, mas agora acaba de ter {new_vida}'
                                  f'\nPorém acabou gastando 2 de estamina nesse'
                                  f'\nprocesso, ficando com {estamina} de estamina')
                            vida = new_vida
                else:
                    print(f'Putz!!! Você não possui estamina suficiente,'
                          f'\ndescanse para recuperar estamina')

                if action == 'descansar' or action == '4':
                    descansar = randint(1, 7)
                    new_est = estamina + descansar
                    if new_est > est_max:
                        descansar = est_max - estamina
                        new_mana = estamina + descansar
                        print(f'Você olhou pro chefão e correu mata adentro'
                              f'\nNisso você resolve meditar e recupera '
                              f'\níncriveis {descansar} de estamina,'
                              f'\ntotalizando {new_est} de estamina')
                    else:
                        print(f'Você olhou pro chefao e correu mata adentro'
                              f'\nNisso você resolve meditar e recupera '
                              f'\níncriveis {descansar} de estamina,'
                              f'\ntotalizando {new_est} de estamina')

                # Ataque do monstro e defesa do personagem
                if acao_chefao == 1:
                    print('=-' * 40)

                    # A ação de defesa está aqui porque só é possível defender quando o monstro ataca
                    if estamina >= 2:
                        if action == 'defesa' or action == '3':
                            estamina -= 2
                            defesa = int(atk_chefao / 2)
                            print('Nossa que defesa!!!')
                            print(f'Você sofreu apenas {defesa} de dano após essa defesa espetacular!'
                                  f'\nPorém você acabou gastando 2 de estamina nessa ação,'
                                  f'\nficando com {estamina} de estamina')
                            vida -= defesa
                        else:
                            print(f'O monstro te deu {atk_chefao} de dano ')
                            vida -= atk_chefao

                        # Morte do personagem
                        if vida <= 0:
                            print('=-' * 40)
                            print("Infelizmente você morreu após essa árdua batalha!!!")
                            exit()
                        else:
                            print(f'Sua vida agora é {vida}')
                    else:
                        print(f'Putz!!! Você não possui estamina suficiente,'
                              f'\ndescanse para recuperar estamina')
                        print(f'O monstro te deu {atk_chefao} de dano ')
                        vida -= atk_chefao
                        # Morte do personagem
                        if vida <= 0:
                            print('=-' * 40)
                            print("Infelizmente você morreu após essa árdua batalha!!!")
                            exit()
                        else:
                            print(f'Sua vida agora é {vida}')
                rd += 1
                estamina += 1
                if estamina < est_max:
                    print(f'Você recuperou 1 de mana, totalizando {estamina} de estamina')
                else:
                    estamina = est_max
                    print(f'Você possui {estamina} de estamina')
