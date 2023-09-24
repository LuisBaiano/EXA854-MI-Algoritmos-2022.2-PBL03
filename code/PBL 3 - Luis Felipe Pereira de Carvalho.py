import time

#A função Menu_title responsável por criar uma exibição padrão para os menus.
def menu_title(text):
    print('\n','==='*15,'\n')
    print(text)
    print('\n','==='*15)

#A função is_number responsável por validar as entradas que devem ser somente de números.
def is_number(text):
    n = ''
    while not n.isdigit():
        n = input(text)
        if not n.isdigit(): print('Valor inválido. Por favor, tente novamente!')
    return n

#A função check_all_options responsável por validar o número escolhido para o menu principal, os submenus, os grupos e as seleções.
def check_all_options(aux1, aux2):
    while True:
        n = input('\nPor favor, escolha uma das opções válidas: ')
        try:
            n = int(n)
            if aux1 <= n <= aux2:
                break
            else:
                print('\nOpção inválida, tente novamente!')
        except ValueError:
            print("\nSomente números são permitidos.")
    return n

#A função check_menu_option é responsável por exibir as opções disponíveis do menu e receber a escolha do usuário.
def check_menu_option():
    print('''\nDigite apenas o número da opção que deseja executar.\n
[1] - Cadastro \n[2] - Edição \n[3] - Exibição \n[0] - Sair do Cadastro \n==================================================\n''')
    menu_num = check_all_options(0,3)
    return menu_num

#A função check_submenu_option é responsável por exibir as opções disponíveis para os submenus e receber a escolha do usuário.
def check_submenu_option(menu_num):
    print('\nO que deseja fazer agora?\n')
    if menu_num == 1:
        print('''[1] - Cadastrar seleções dos grupos \n[2] - Cadastrar confrontos \n[0] - Voltar ao menu anterior \n==================================================\n''')
        sub_menu_num = check_all_options(0,2)
    elif menu_num == 2:
        print('''[1] - Editar seleções e grupos \n[2] - Editar confrontos \n[0] - Voltar ao menu anterior \n==================================================\n''')
        sub_menu_num = check_all_options(0,2)
    elif menu_num == 3:
        print('''[1] - Exibir seleções e grupos \n[2] - Exibir confrontos por grupo \n[0] - Voltar ao menu anterior \n==================================================\n''')
        sub_menu_num = check_all_options(0,2)
    return sub_menu_num

#A função group_option é responsável por exibir os grupos e receber a escolha do usuário.
def group_option():
    print('''\nQual Grupo deseja escolher?\n
[1] - Grupo A \n[2] - Grupo B \n[3] - Grupo C \n[4] - Grupo D \n[5] - Grupo E \n[6] - Grupo F \n[7] - Grupo G \n[8] - Grupo H \n[0] - Voltar ao menu anterior
\n==================================================\n''')
    group_num = (check_all_options(0,8))
    return group_num

#A função all_teams é responsável por verificar se a seleção já se encontra cadastrada 
# em algum grupo e evita que a mesma seja cadastrada em outro ou no mesmo grupo.
def all_teams(n, list_all_teams):
    team = input(f'Digite a {n}ª seleção: ').upper()
    if team in list_all_teams:
        print('SELEÇÃO JÁ CADASTRADA. \nPOR FAVOR, ESCOLHA OUTRA!')
        team = input(f'Digite a {n}ª seleção: ').upper()
        while team in list_all_teams:
            team = input(f'Digite a {n}ª seleção: ').upper()
    return team

#A função group_letter, é responsável por exibir a letra (A-H) que recebe cada grupo conforme a escolha na função group_option.
def group_letter(num_group):
    if num_group == 1:
        return 'A'
    elif num_group == 2:
        return 'B'
    elif num_group == 3:
        return 'C'
    elif num_group == 4:
        return 'D'
    elif num_group == 5:
        return 'E'
    elif num_group == 6:
        return 'F'
    elif num_group == 7:
        return 'G'
    elif num_group == 8:
        return 'H'

#A função create_groups, é responsável por criar os grupos.
def create_groups(list_all_teams, list_A, list_B, list_C, list_D, list_E, list_F, list_G, list_H):
    num_group = group_option()
    #recuperando as seleções cadastradas no arquivo
    with open('groups.txt','r') as f:
        alist = [line.rstrip() for line in f]
        list_A = [alist[0], alist[1], alist[2], alist[3]]
        list_B = [alist[4], alist[5], alist[6], alist[7]]
        list_C = [alist[8], alist[9], alist[10], alist[11]]
        list_D = [alist[12], alist[13], alist[14], alist[15]]
        list_E = [alist[16], alist[17], alist[18], alist[19]]
        list_F = [alist[20], alist[21], alist[22], alist[23]]
        list_G = [alist[24], alist[25], alist[26], alist[27]]
        list_H = [alist[28], alist[29], alist[30], alist[31]]

        Letter = group_letter(num_group)
        menu_title(f'\nCADASTRO DO GRUPO {Letter}')

        t1 = all_teams(1, list_all_teams)
        list_all_teams.append(t1)

        t2 = all_teams(2, list_all_teams)
        list_all_teams.append(t2)

        t3 = all_teams(3, list_all_teams)
        list_all_teams.append(t3)

        t4 = all_teams(4, list_all_teams)
        list_all_teams.append(t4)

        if num_group == 1:
            list_A = [t1, t2, t3, t4]
        elif num_group == 2:
            list_B = [t1, t2, t3, t4]
        elif num_group == 3:
            list_C = [t1, t2, t3, t4]
        elif num_group == 4:
            list_D = [t1, t2, t3, t4]
        elif num_group == 5:
            list_E = [t1, t2, t3, t4]
        elif num_group == 6:
            list_F = [t1, t2, t3, t4]
        elif num_group == 7:
            list_G = [t1, t2, t3, t4]
        elif num_group == 8:
            list_H = [t1, t2, t3, t4]
        
        with open('groups.txt','w+') as arq:
            arq.write('\n'.join(list_A))
            arq.write('\n')
            arq.write('\n'.join(list_B))
            arq.write('\n')
            arq.write('\n'.join(list_C))
            arq.write('\n')
            arq.write('\n'.join(list_D))
            arq.write('\n')
            arq.write('\n'.join(list_E))
            arq.write('\n')
            arq.write('\n'.join(list_F))
            arq.write('\n')
            arq.write('\n'.join(list_G))
            arq.write('\n')
            arq.write('\n'.join(list_H))
        arq.close()

#A show_all_groups, é responsável por mostrar os grupos.
def show_all_groups():
    with open('groups.txt','r') as f:
        alist = [line.rstrip() for line in f]
    if len(alist) >= 32:
        menu_title('            GRUPOS CADASTRADOS')
        menu_title('           Grupo A')
        print(alist[0],'|',  alist[1],'|',  alist[2],'|',  alist[3])
        menu_title('           Grupo B')
        print(alist[4],'|', alist[5],'|',  alist[6],'|',  alist[7])
        menu_title('           Grupo C')
        print(alist[0],'|',  alist[9],'|',  alist[10],'|',  alist[11])
        menu_title('           Grupo D')
        print(alist[12],'|',  alist[13],'|',  alist[14],'|',  alist[15])
        menu_title('           Grupo E')
        print(alist[16],'|',  alist[17],'|',  alist[18],'|',  alist[19])
        menu_title('           Grupo F')
        print(alist[20],'|',  alist[21],'|',  alist[22],'|',  alist[23])
        menu_title('           Grupo G')
        print(alist[24],'|',  alist[25],'|',  alist[26],'|',  alist[27])
        menu_title('           Grupo H')
        print(alist[28],'|',  alist[29],'|',  alist[30],'|',  alist[31])
    else:
        print('\nFALTAM GRUPOS A SEREM CADASTRADOS\n')

#a função matches é responsável por criar os confrontos das seleções de cada grupo
def matches():
    num_group = group_option()
    #recuperando as seleções do arquivo de grupos
    with open('groups.txt','r') as f:
        alist = [line.rstrip() for line in f]
        list_A = [alist[0], alist[1], alist[2], alist[3]]
        list_B = [alist[4], alist[5], alist[6], alist[7]]
        list_C = [alist[8], alist[9], alist[10], alist[11]]
        list_D = [alist[12], alist[13], alist[14], alist[15]]
        list_E = [alist[16], alist[17], alist[18], alist[19]]
        list_F = [alist[20], alist[21], alist[22], alist[23]]
        list_G = [alist[24], alist[25], alist[26], alist[27]]
        list_H = [alist[28], alist[29], alist[30], alist[31]]
    #indexando as seleções obtidas por grupo, para que sejam utilizadas no cadastro dos confrontos 
    if num_group == 1:
        team1 = list_A[0]; team2 = list_A[1]; team3 = list_A[2]; team4 = list_A[3]
    elif num_group == 2:
        team1 = list_B[0]; team2 = list_B[1]; team3 = list_B[2]; team4 = list_B[3]
    elif num_group == 3:
        team1 = list_C[0]; team2 = list_C[1]; team3 = list_C[2]; team4 = list_C[3]
    elif num_group == 4:
        team1 = list_D[0]; team2 = list_D[1]; team3 = list_D[2]; team4 = list_D[3]
    elif num_group == 5:
        team1 = list_E[0]; team2 = list_E[1]; team3 = list_E[2]; team4 = list_E[3]
    elif num_group == 6:
        team1 = list_F[0]; team2 = list_F[1]; team3 = list_F[2]; team4 = list_F[3]
    elif num_group == 7:
        team1 = list_G[0]; team2 = list_G[1]; team3 = list_G[2]; team4 = list_G[3]
    elif num_group == 8:
        team1 = list_H[0]; team2 = list_H[1]; team3 = list_H[2]; team4 = list_H[3]
    #recuperando os confrontos cadastrados no arquivo, de modo a alterá-los ou não
    with open('matches.txt','r') as f:
        alist = [line.rstrip() for line in f]
        m1_group_A = alist[0]; m2_group_A = alist[1]; m3_group_A = alist[2]; m4_group_A = alist[3]; m5_group_A = alist[4]; m6_group_A = alist[5]
        m1_group_B = alist[6]; m2_group_B = alist[7]; m3_group_B = alist[8]; m4_group_B = alist[9]; m5_group_B = alist[10]; m6_group_B = alist[11]
        m1_group_C = alist[12]; m2_group_C = alist[13]; m3_group_C = alist[14]; m4_group_C = alist[15]; m5_group_C = alist[16]; m6_group_C = alist[17]
        m1_group_D = alist[18]; m2_group_D = alist[19]; m3_group_D = alist[20]; m4_group_D = alist[21]; m5_group_D = alist[22]; m6_group_D = alist[23]
        m1_group_E = alist[24]; m2_group_E = alist[25]; m3_group_E = alist[26]; m4_group_E = alist[27]; m5_group_E = alist[28]; m6_group_E = alist[29]
        m1_group_F = alist[30]; m2_group_F = alist[31]; m3_group_F = alist[32]; m4_group_F = alist[33]; m5_group_F = alist[34]; m6_group_F = alist[35]
        m1_group_G = alist[36]; m2_group_G = alist[37]; m3_group_G = alist[38]; m4_group_G = alist[39]; m5_group_G = alist[40]; m6_group_G = alist[41]
        m1_group_H = alist[42]; m2_group_H = alist[43]; m3_group_H = alist[44]; m4_group_H = alist[45]; m5_group_H = alist[46]; m6_group_H = alist[47]
    f.close()
    
    #recebendo as entradas para os 6 confrontos
    Letter = group_letter(num_group)
    menu_title(f'\nCADASTRO DOS CONFRONTOS DO GRUPO {Letter}')
    
    print(f'\n {team1} VS {team2} \n')
    date_1 =  input('informe o dia do confronto: ')
    time_1 =  input('Informe o horário do confronto: ')
    local_1 = input('Informe o estádio: ').upper()
    goals_t1_m1 = is_number(f'Digite a quantidade de gols de {team1}: ')
    goals_t2_m1 = is_number(f'Digite a quantidade de gols de {team2}: ')

    print(f'\n {team3} VS {team4} \n')
    date_2 =  input('informe o dia do confronto: ')
    time_2 =  input('Informe o horário do confronto: ')
    local_2 = input('Informe o estádio: ').upper()
    goals_t3_m2 = is_number(f'Digite a quantidade de gols de {team3}: ')
    goals_t4_m2 = is_number(f'Digite a quantidade de gols de {team4}: ')

    print(f'\n {team1} VS {team4} \n')
    date_3 =  input('informe o dia do confronto: ')
    time_3 =  input('Informe o horário do confronto: ')
    local_3 = input('Informe o estádio: ').upper()
    goals_t1_m3 = is_number(f'Digite a quantidade de gols de {team1}: ')
    goals_t4_m3 = is_number(f'Digite a quantidade de gols de {team4}: ')

    print(f'\n {team3} VS {team2} \n')
    date_4 =  input('informe o dia do confronto: ')
    time_4 =  input('Informe o horário do confronto: ')
    local_4 = input('Informe o estádio: ').upper()
    goals_t3_m4 = is_number(f'Digite a quantidade de gols de {team3}: ')
    goals_t2_m4 = is_number(f'Digite a quantidade de gols de {team2}: ')

    print(f'\n {team1} VS {team3} \n')
    date_5 =  input('informe o dia do confronto: ')
    time_5 =  input('Informe o horário do confronto: ')
    local_5 = input('Informe o estádio: ').upper()
    goals_t1_m5 = is_number(f'Digite a quantidade de gols de {team1}: ')
    goals_t3_m5 = is_number(f'Digite a quantidade de gols de {team3}: ')

    print(f'\n {team4} VS {team2} \n')
    date_6 =  input('informe o dia do confronto: ')
    time_6 =  input('Informe o horário do confronto: ')
    local_6 = input('Informe o estádio: ').upper()
    goals_t4_m6 = is_number(f'Digite a quantidade de gols de {team4}: ')
    goals_t2_m6 = is_number(f'Digite a quantidade de gols de {team2}: ')
    
    #indenxando os dados dos confrontos em 6 listas distintas
    match1 = [team1 ,'VS', team2, date_1, time_1, local_1, 'Gols time 1:',goals_t1_m1,'Gols time 2:', goals_t2_m1]; match2 = [team3 ,'VS', team4, date_2, time_2, local_2,'Gols time 1:', goals_t3_m2,'gols time 2:',goals_t4_m2]; match3 = [team1 ,'VS', team4, date_3, time_3, local_3,'Gols time 1:',goals_t1_m3,'Gols time 2:',goals_t4_m3]
    match4 = [team3 ,'VS', team2, date_4, time_4, local_4, 'Gols time 1:',goals_t3_m4,'Gols time 2:',goals_t2_m4]; match5 = [team1 ,'VS', team3, date_5, time_5, local_5,'Gols time 1:',goals_t1_m5,'gols time 2:', goals_t3_m5]; match6 = [team4 ,'VS', team2, date_6, time_6, local_6,'Gols time 1:',goals_t4_m6,'Gols time 2:',goals_t2_m6]
    
    #atualizando os confrontos, conforme o grupo que foi escolhido para ser alterado
    with open('matches.txt','w') as arq:
        if num_group == 1:
            m1_group_A = match1; m2_group_A = match2; m3_group_A = match3; m4_group_A = match4; m5_group_A = match5; m6_group_A = match6
        elif num_group == 2:
            m1_group_B = match1; m2_group_B = match2; m3_group_B = match3; m4_group_B = match4; m5_group_B = match5; m6_group_B = match6
        elif num_group == 3:
            m1_group_C = match1; m2_group_C = match2; m3_group_C = match3; m4_group_C = match4; m5_group_C = match5; m6_group_C = match6
        elif num_group == 4:
            m1_group_D = match1; m2_group_D = match2; m3_group_D = match3; m4_group_D = match4; m5_group_D = match5; m6_group_D = match6
        elif num_group == 5:
            m1_group_E = match1; m2_group_E = match2; m3_group_E = match3; m4_group_E = match4; m5_group_E = match5; m6_group_E = match6
        elif num_group == 6:
            m1_group_F = match1; m2_group_F = match2; m3_group_F = match3; m4_group_F = match4; m5_group_F = match5; m6_group_F = match6
        elif num_group == 7:
            m1_group_G = match1; m2_group_G = match2; m3_group_G = match3; m4_group_G = match4; m5_group_G = match5; m6_group_G = match6
        elif num_group == 8:
            m1_group_H = match1; m2_group_H = match2; m3_group_H = match3; m4_group_H = match4; m5_group_H = match5; m6_group_H = match6
        arq.write(str(m1_group_A)); arq.write('\n'); arq.write(str(m2_group_A)); arq.write('\n'); arq.write(str(m3_group_A)); arq.write('\n'); arq.write(str(m4_group_A)); arq.write('\n'); arq.write(str(m5_group_A)); arq.write('\n'); arq.write(str(m6_group_A)); arq.write('\n')
        arq.write(str(m1_group_B)); arq.write('\n'); arq.write(str(m2_group_B)); arq.write('\n'); arq.write(str(m3_group_B)); arq.write('\n'); arq.write(str(m4_group_B)); arq.write('\n'); arq.write(str(m5_group_B)); arq.write('\n'); arq.write(str(m6_group_B)); arq.write('\n')
        arq.write(str(m1_group_C)); arq.write('\n'); arq.write(str(m2_group_C)); arq.write('\n'); arq.write(str(m3_group_C)); arq.write('\n'); arq.write(str(m4_group_C)); arq.write('\n'); arq.write(str(m5_group_C)); arq.write('\n'); arq.write(str(m6_group_C)); arq.write('\n')
        arq.write(str(m1_group_D)); arq.write('\n'); arq.write(str(m2_group_D)); arq.write('\n'); arq.write(str(m3_group_D)); arq.write('\n'); arq.write(str(m4_group_D)); arq.write('\n'); arq.write(str(m5_group_D)); arq.write('\n'); arq.write(str(m6_group_D)); arq.write('\n')
        arq.write(str(m1_group_E)); arq.write('\n'); arq.write(str(m2_group_E)); arq.write('\n'); arq.write(str(m3_group_E)); arq.write('\n'); arq.write(str(m4_group_E)); arq.write('\n'); arq.write(str(m5_group_E)); arq.write('\n'); arq.write(str(m6_group_E)); arq.write('\n')
        arq.write(str(m1_group_F)); arq.write('\n'); arq.write(str(m2_group_F)); arq.write('\n'); arq.write(str(m3_group_F)); arq.write('\n'); arq.write(str(m4_group_F)); arq.write('\n'); arq.write(str(m5_group_F)); arq.write('\n'); arq.write(str(m6_group_F)); arq.write('\n')
        arq.write(str(m1_group_G)); arq.write('\n'); arq.write(str(m2_group_G)); arq.write('\n'); arq.write(str(m3_group_G)); arq.write('\n'); arq.write(str(m4_group_G)); arq.write('\n'); arq.write(str(m5_group_G)); arq.write('\n'); arq.write(str(m6_group_G)); arq.write('\n')
        arq.write(str(m1_group_H)); arq.write('\n'); arq.write(str(m2_group_H)); arq.write('\n'); arq.write(str(m3_group_H)); arq.write('\n'); arq.write(str(m4_group_H)); arq.write('\n'); arq.write(str(m5_group_H)); arq.write('\n'); arq.write(str(m6_group_H)); arq.write('\n')
    arq.close()

#A função show_matches, é responsável por mostrar os confrontos por cada grupo, conforme solicitação do usuário.
def show_matches():
    num_group = group_option()
    with open('matches.txt') as f:
        alist = [line.rstrip() for line in f]
        menu_title('            CONFRONTOS DOS GRUPOS CADASTRADOS')
        if num_group == 1:
            menu_title('           Grupo A')
            print(alist[0])
            print(alist[1])
            print(alist[2])
            print(alist[3])
            print(alist[4])
            print(alist[5])
        elif num_group == 2:
            menu_title('           Grupo B')
            print(alist[6])
            print(alist[7])
            print(alist[8])
            print(alist[9])
            print(alist[10])
            print(alist[11])
        elif num_group == 3:
            menu_title('           Grupo C')
            print(alist[12])
            print(alist[13])
            print(alist[14])
            print(alist[15])
            print(alist[16])
            print(alist[17])
        elif num_group == 4:
            menu_title('           Grupo D')
            print(alist[18])
            print(alist[19])
            print(alist[20])
            print(alist[21])
            print(alist[22])
            print(alist[23])
        elif num_group == 5:
            menu_title('           Grupo E')
            print(alist[24])
            print(alist[25])
            print(alist[26])
            print(alist[27])
            print(alist[28])
            print(alist[29])
        elif num_group == 6:
            menu_title('           Grupo F')
            print(alist[30])
            print(alist[31])
            print(alist[32])
            print(alist[33])
            print(alist[34])
            print(alist[35])
        elif num_group == 7:
            menu_title('           Grupo G')
            print(alist[36])
            print(alist[37])
            print(alist[38])
            print(alist[39])
            print(alist[40])
            print(alist[41])
        elif num_group == 8:
            menu_title('           Grupo H')
            print(alist[42])
            print(alist[43])
            print(alist[44])
            print(alist[45])
            print(alist[46])
            print(alist[47])
    f.close()

#A função main é responsável pela execução principal do sistema.
def main():

    list_all_teams = []; list_A = []; list_B = []
    list_C = []; list_D = []; list_E = []; list_F = []; list_G = []; list_H = []
    print('''===================================================================================
        BEM-VINDOS AO SISTEMA DE CADASTRO DE JOGOS DA COPA DO MUNDO DE 2022
===================================================================================''')
    num_menu = check_menu_option()
    while num_menu != 0:

        sub_menu_num = check_submenu_option(num_menu)
        while sub_menu_num != 0:

            #menu responsável pela cadastro dos grupos e seleções e dos confrontos de cada grupo.
            if num_menu == 1:
                if sub_menu_num == 1: create_groups(list_all_teams, list_A, list_B, list_C, list_D, list_E, list_F, list_G, list_H)
                elif sub_menu_num == 2: matches()
                sub_menu_num = check_submenu_option(num_menu)

            #menu responsável pela edição dos grupos e seleções.
            elif num_menu == 2:
                if sub_menu_num == 1: create_groups(list_all_teams, list_A, list_B, list_C, list_D, list_E, list_F, list_G, list_H)
                elif sub_menu_num == 2: matches()
                sub_menu_num = check_submenu_option(num_menu)

            #menu responsável pela exibição dos grupos e seleções.
            elif num_menu == 3:
                if sub_menu_num == 1: show_all_groups()
                elif sub_menu_num == 2: show_matches()
                sub_menu_num = check_submenu_option(num_menu)

        num_menu = check_menu_option()
    #mensagem de encerramento do jogo.
    time.sleep(1)
    menu_title('\n      CADASTRO ENCERRADO COM SUCESSO!!!')

main()
