# APP
WINDOW_TITLE = 'Tsar Bank 2.0'

WINDOW_HEIGHT = 700
WINDOW_WIDTH = 1100

# ASSETS
WINDOW_BITMAP_ICON_PATH = 'assets\\icon\\tsar_bank.ico'

SMALL_DB_ICON_PATH = 'assets\\ui\\login_screen\\db_icon.png'
USER_ICON_PATH = 'assets\\ui\\login_screen\\user_icon.png'

SHOW_PASSWORD_ICON_PATH = 'assets\\ui\\login_screen\\show_password.png'
HIDE_PASSWORD_ICON_PATH = 'assets\\ui\\login_screen\\hide_password.png'

WARNING_ICON_PATH = 'assets\\ui\\login_screen\\warning.png'

BACK_ARROW_ICON_PATH = 'assets\\ui\\back_arrow.png'

# FONT
WELCOME_SCREEN_WELCOME_LABEL_FONT = ('Congenial Black', 70, 'bold')
WELCOME_SCREEN_BUTTON_FONT = ('Congenial Black', 40, 'bold')

LOGIN_SCREEN_DB_STATUS_FONT = ('Calibri', 18, 'bold')

LOGIN_SCREEN_FIELD_LABEl_FONT = ('Calibri', 60, 'bold')
LOGIN_SCREEN_FIELD_ENTRY_FONT = ('Calibri', 40)
LOGIN_SCREEN_BOTTOM_BUTTON_FONT = ('Calibri', 45, 'bold')

LOGIN_SCREEN_WARNING_LABEL_FONT = ('Calibri', 22, 'bold')

SIGNUP_SCREEN_LABEL_FONT = ('Calibri', 50, 'bold')
SIGNUP_SCREEN_FIELD_ENTRY_FONT = ('Calibri', 38)
SIGNUP_SCREEN_RADIO_BUTTON_FONT = ('Calibri', 25, 'bold')
SIGNUP_SCREEN_ADDRESS_FONT = ('Calibri', 32)
SIGNUP_SCREEN_OPERATION_BUTTON_FONT =('Calibri', 30, 'bold')

# DIMENSIONS
SIDE_PANEL_BUTTON_DIMENSION = 100
SIDE_PANEL_BUTTON_CORNER_RADIUS = 18

COMMON_ENTRY_CORNER_RADIUS = 40

LOGIN_SCREEN_BOTTOM_BUTTON_WIDTH = 380
LOGIN_SCREEN_BOTTOM_BUTTON_HEIGHT = 80
LOGIN_SCREEN_BOTTOM_BUTTON_CORNER_RADIUS = 100

# COLORS
APP_COLOR_THEME = 'green'  # Available -> ['blue', 'dark-blue', 'green']

# ERRORS
LOGIN_ERRORS = {
    0: '   Username or Password field cannot be empty!',
    1: '   Unable to connect to the database!',
    2: '   Invalid Username or Password! Please ensure valid credentials!'
}

SIGN_UP_ERRORS = {
    0: 'First Name field cannot be empty!',
    1: 'Last Name field cannot be empty!',
    2: 'Address field cannot be empty!',
    3: 'Email field cannot be empty!',
    4: 'Phone Number field cannot be empty!',
    5: 'First Name must be a minimum of 3 characters!',
    6: 'Last Name must be a minimum of 1 character!',
    7: 'Address must be a minimum of 30 characters!',
    8: 'Invalid Phone Number! Please enter a 10-Digit Phone Number!',
    9: 'Please select a valid Gender!',
    10: 'Sorry! Users under the age of 15 cannot sign up for an account!',
    11: 'Invalid Email! Please provide a valid email address!',
    12: 'Unable to connect to database!',
}

# DATABASE
DB = {"HOST": "sql6.freesqldatabase.com", "DATABASE": "sql6698638", "PORT": 3306, "USER": "sql6698638", "PASSWORD": "fMqmcIIyBu"}