# Here the global variables should be set in order to make it easier to do maintanece, access and verify them
from datetime import datetime
from system_environment.menu import *


# Path variables
path_output_df = r'dataframes_generated/'
path_to_specific_information = r'system_environment/specific_information/'
path_to_user_info = r'user_information/'


# Solo variables
userId = open(f'{path_to_user_info}userID.txt', 'r').readlines()[0]
client_id = open(f'{path_to_user_info}client_id.txt', 'r').readlines()[0]
client_secret = open(f'{path_to_user_info}client_secret.txt', 'r').readlines()[0]


# Links and endpoint variables
get_hobolink_data_path = f'https://webservice.hobolink.com/ws/data/file/json/user/{userId}'
post_generate_token_json_path = 'https://webservice.hobolink.com/ws/auth/token'


# Request variables
token_data = {'grant_type': 'client_credentials', 'client_id': client_id, 'client_secret': client_secret}

# ASCII Art
welcome = """█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀
▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄"""
timestamp = """▀█▀ █ █▀▄▀█ █▀▀ █▀ ▀█▀ ▄▀█ █▀▄▀█ █▀█ █▀
░█░ █ █░▀░█ ██▄ ▄█ ░█░ █▀█ █░▀░█ █▀▀ ▄█"""
end_message = """█▀▀ █▄░█ █▀▄ █
██▄ █░▀█ █▄▀ ▄"""
warning_art = """█░█░█ ▄▀█ █▀█ █▄░█ █ █▄░█ █▀▀
▀▄▀▄▀ █▀█ █▀▄ █░▀█ █ █░▀█ █▄█"""

pc_art = """                       .,,uod8B8bou,,.
              ..,uod8BBBBBBBBBBBBBBBBRPFT?l!i:.
         ,=m8BBBBBBBBBBBBBBBRPFT?!||||||||||||||
         !...:!TVBBBRPFT||||||||||!!^^""'   ||||
         !.......:!?|||||!!^^""'            ||||
         !.........||||                     ||||
         !.........||||  ##                 ||||
         !.........||||                     ||||
         !.........||||                     ||||
         !.........||||                     ||||
         !.........||||                     ||||
         `.........||||                    ,||||
          .;.......||||               _.-!!|||||
   .,uodWBBBBb.....||||       _.-!!|||||||||!:'
!YBBBBBBBBBBBBBBb..!|||:..-!!|||||||!iof68BBBBBb....
!..YBBBBBBBBBBBBBBb!!||||||||!iof68BBBBBBRPFT?!::   `.
!....YBBBBBBBBBBBBBBbaaitf68BBBBBBRPFT?!:::::::::     `.
!......YBBBBBBBBBBBBBBBBBBBRPFT?!::::::;:!^"`;:::       `.
!........YBBBBBBBBBBRPFT?!::::::::::^''...::::::;         iBBbo.
`..........YBRPFT?!::::::::::::::::::::::::;iof68bo.      WBBBBbo.
  `..........:::::::::::::::::::::::;iof688888888888b.     `YBBBP^'
    `........::::::::::::::::;iof688888888888888888888b.     `
      `......:::::::::;iof688888888888888888888888888888b.
        `....:::;iof688888888888888888888888888888888899fT!
          `..::!8888888888888888888888888888888899fT|!^"'
            `' !!988888888888888888888888899fT|!^"'
                `!!8888888888888888899fT|!^"'
                  `!988888888899fT|!^"'
                    `!9899fT|!^"'
                      `!^"'\n"""

many_loggers_art = """ ___     ___     ___     ___     ___     ___     ___     ___     ___     ___     ___
| _ |   | _ |   | _ |   | _ |   | _ |   | _ |   | _ |   | _ |   | _ |   | _ |   | _ |
|| ||   || ||   || ||   || ||   || ||   || ||   || ||   || ||   || ||   || ||   || ||
||_||   ||_||   ||_||   ||_||   ||_||   ||_||   ||_||   ||_||   ||_||   ||_||   ||_||
|=::|   |=::|   |=::|   |=::|   |=::|   |=::|   |=::|   |=::|   |=::|   |=::|   |=::|
`---'   `---'   `---'   `---'   `---'   `---'   `---'   `---'   `---'   `---'   `---'"""
unknown_logger_art = """ ___     ___     ___     ___     ___     ___     ___     ___     ___     ___
| _ |   | _ |   | _ |   | _ |   | _ |   | _ |   | _ |   | _ |   | _ |   | _ |
||?||   ||?||   ||?||   ||?||   ||?||   ||?||   ||?||   ||?||   ||?||   ||?||
||_||   ||_||   ||_||   ||_||   ||_||   ||_||   ||_||   ||_||   ||_||   ||_||
|=::|   |=::|   |=::|   |=::|   |=::|   |=::|   |=::|   |=::|   |=::|   |=::|
`---'   `---'   `---'   `---'   `---'   `---'   `---'   `---'   `---'   `---'"""

mx1102_logger_art = """ _____________________________     _____________________________   
/ MX CO2 logger               \\   / MX CO2 logger               \\
|   _____________       __    |   |   _____________       __    |
|  |             |     /  \   |   |  |             |     /  \   |
|  |             |    / /\ \  |   |  |             |    / /\ \  |
|  |             |    \ \/ /  |   |  |             |    \ \/ /  |
|  |             |     \__/   |   |  |             |     \__/   |
|  |             |            |   |  |             |            |
|  |             |         .  |   |  |             |         .  |
|  |             |     ==     |   |  |             |     ==     |
|  |_____________|  @  ==     |   |  |_____________|  @  ==     |
|   [ ]  [ ]  [ ]             |   |   [ ]  [ ]  [ ]             |
\_____________________________/   \_____________________________/"""

two_loggers_art = """ ___     ___
| _ |   | _ |
|| ||   || ||
||_||   ||_||
|=::|   |=::|
`---'   `---'"""
