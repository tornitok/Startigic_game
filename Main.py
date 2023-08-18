from Classes import EventBank, OptionsBank, RoundCounter, DangeonMaster, PropositionTeam,OppositionTeam
from Classes.unused import MakeChoice


def create_an_event(event):
    new_story = EventBank(event)
    print(event)


def create_options(options):
    print(options.options)


def create_proposition_team(name, options, description):
    proposition_team = PropositionTeam(name, options, description)
    print(proposition_team.name)
    print(proposition_team.description)


def create_opposition_team(name, options, description):
    opposition_team = OppositionTeam(name, options, description)
    print(opposition_team.name)
    print(opposition_team.options)
    print(opposition_team.description)


def create_round(round_num):
    new_round = RoundCounter(round_num)
    first_round = new_round.get_next_round()
    print("Round", first_round, "starts")


def choice(team_choice):
    print(team_choice.choice)


def create_first_round(name_of_proposition, options_proposition, name_of_opposition, options_opposition):
    print("Options of", name_of_proposition)
    for option in options_proposition.options:
        print(option)

    create_options(options_proposition)
    print("Turn of", name_of_proposition, "to pick the option")

    print("Turn of", name_of_opposition, "to pick the option")
    for option in options_opposition.options:
        print(option)

    print("Options of", name_of_opposition)
    create_options(options_proposition)


def main():
    print("Let the Battle Begins")

    event = input("Enter the event description: ")

    # First Team
    description = input("Description and goals of the side: ")
    name_of_proposition = input("Choice name for Team 1: ")

    options_proposition = OptionsBank([])
    for i in range(1, 5):
        print("Enter character of option", i, ": ")
        num_of_option = input()
        print("Enter option for", name_of_proposition, ": ")
        option_pro = input()
        options_proposition.options.append(option_pro)

    # Second team
    name_of_opposition = input("Choice name for second team: ")
    opposion_description = input("Description and goals of the side: ")

    options_opposition = OptionsBank([])
    for i in range(1, 4):
        print("Enter character of option", i, ": ")
        num_of_option = input()
        print("Enter option for", name_of_opposition, ": ")
        option_opp = input()
        options_opposition.options.append(option_opp)

    create_an_event(event)
    create_proposition_team(name_of_proposition, options_proposition, description)
    create_opposition_team(name_of_opposition, options_opposition, opposion_description)

    create_round(0)
    create_first_round(name_of_proposition, options_proposition, name_of_opposition, options_opposition)

    team_choice = input().upper()
    proposition_choice = MakeChoice(name_of_proposition, options_proposition, team_choice)
    choice(proposition_choice)

    opposition_team_choice = input().upper()
    opposition_choice = MakeChoice(name_of_opposition, options_opposition, opposition_team_choice)
    choice(opposition_choice)


if __name__ == "__main__":
    main()
