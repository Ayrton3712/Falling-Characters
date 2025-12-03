import pygame
import random
import sys

# Initialize Pygame
pygame.init()
pygame.mixer.init()  # Initialize sound mixer

# Sound effects
sound_correct = pygame.mixer.Sound('correct.wav')
sound_wrong = pygame.mixer.Sound('wrong.wav')
sound_miss = pygame.mixer.Sound('miss.wav')

# Background music - TO ADD BACKGROUND MUSIC:
# 1. Get a music file (.mp3, .ogg, or .wav format)
# 2. Place it in the same folder as this script
# 3. Call it background_music.mp3
#
# pygame.mixer.music.load('background_music.mp3')
# pygame.mixer.music.set_volume(0.3)  # Set volume (0.0 to 1.0)
# pygame.mixer.music.play(-1)  # -1 means loop forever
#
# To stop music: pygame.mixer.music.stop()
# To pause music: pygame.mixer.music.pause()
# To resume music: pygame.mixer.music.unpause()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700  # Increased from 600 to 700

# Colors - Default theme
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (100, 149, 237)
YELLOW = (255, 255, 0)

# Theme system
THEMES = {
    'default': {
        'bg': (100, 149, 237),  # Cornflower blue
        'text': (255, 255, 255),  # White
        'accent': (255, 255, 0),  # Yellow
        'correct': (0, 255, 0),  # Green
        'wrong': (255, 0, 0),  # Red
        'name': 'Default Blue'
    },
    'dark': {
        'bg': (30, 30, 40),  # Dark gray-blue
        'text': (220, 220, 220),  # Light gray
        'accent': (100, 200, 255),  # Light blue
        'correct': (100, 255, 100),  # Light green
        'wrong': (255, 100, 100),  # Light red
        'name': 'Dark Mode'
    },
    'forest': {
        'bg': (34, 87, 50),  # Forest green
        'text': (255, 255, 240),  # Ivory
        'accent': (255, 215, 0),  # Gold
        'correct': (144, 238, 144),  # Light green
        'wrong': (255, 99, 71),  # Tomato
        'name': 'Forest'
    },
    'sunset': {
        'bg': (255, 140, 100),  # Coral/sunset
        'text': (255, 255, 255),  # White
        'accent': (200, 50, 0),  # Dark orange-red for better contrast
        'correct': (255, 255, 150),  # Light yellow
        'wrong': (139, 0, 0),  # Dark red
        'name': 'Sunset'
    },
    'ocean': {
        'bg': (25, 60, 90),  # Deep ocean blue
        'text': (240, 248, 255),  # Alice blue
        'accent': (0, 255, 255),  # Cyan
        'correct': (127, 255, 212),  # Aquamarine
        'wrong': (255, 127, 80),  # Coral
        'name': 'Ocean'
    },
    'traditional': {
        'bg': (139, 0, 0),  # Dark red
        'text': (255, 215, 0),  # Gold
        'accent': (255, 255, 150),  # Light yellow
        'correct': (255, 215, 0),  # Gold
        'wrong': (100, 100, 100),  # Gray
        'name': 'Traditional Chinese'
    }
}

# Load saved theme
def load_theme():
    try:
        with open('theme.txt', 'r') as f:
            theme_name = f.read().strip()
            return theme_name if theme_name in THEMES else 'default'
    except:
        return 'default'

# Save theme
def save_theme(theme_name):
    try:
        with open('theme.txt', 'w') as f:
            f.write(theme_name)
    except:
        pass

current_theme = load_theme()

# Game settings
FPS = 60
INITIAL_FALL_SPEED = 1
SPEED_INCREMENT = 0.2
SCORE_PER_CHARACTER = 10
HIGH_SCORE_FILE = "high_score.txt"

# Load high score from file
def load_high_score():
    try:
        with open(HIGH_SCORE_FILE, 'r') as f:
            return int(f.read().strip())
    except:
        return 0

# Save high score to file
def save_high_score(score):
    try:
        with open(HIGH_SCORE_FILE, 'w') as f:
            f.write(str(score))
    except:
        pass

# Initialize high score
high_score = load_high_score()

# Daily streak system
STREAK_FILE = "daily_streak.txt"

def load_streak_data():
    """Load last play date and current streak"""
    try:
        with open(STREAK_FILE, 'r') as f:
            lines = f.readlines()
            last_date = lines[0].strip()
            streak = int(lines[1].strip())
            return last_date, streak
    except:
        return "", 0

def save_streak_data(date_str, streak):
    """Save current date and streak"""
    try:
        with open(STREAK_FILE, 'w') as f:
            f.write(f"{date_str}\n{streak}")
    except:
        pass

def update_streak():
    """Update streak based on current date"""
    from datetime import datetime, timedelta
    
    today = datetime.now().date()
    today_str = today.strftime("%Y-%m-%d")
    
    last_date_str, current_streak = load_streak_data()
    
    if last_date_str == "":
        # First time playing
        save_streak_data(today_str, 1)
        return 1
    
    last_date = datetime.strptime(last_date_str, "%Y-%m-%d").date()
    days_diff = (today - last_date).days
    
    if days_diff == 0:
        # Already played today
        return current_streak
    elif days_diff == 1:
        # Played yesterday, continue streak
        current_streak += 1
        save_streak_data(today_str, current_streak)
        return current_streak
    else:
        # Streak broken, start over
        save_streak_data(today_str, 1)
        return 1

daily_streak = update_streak()

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Falling Characters")
clock = pygame.time.Clock()

# Fonts
try:
    # Try to use DFKai-SB font for Chinese characters (common on Windows)
    chinese_font = pygame.font.SysFont('dfkai-sb', 72)
    if chinese_font.get_height() == 0:  # Font not found
        raise Exception("DFKai-SB not available")
except:
    # Fallback to other common Chinese fonts
    try:
        chinese_font = pygame.font.SysFont('microsoftyaheui', 72)
    except:
        try:
            chinese_font = pygame.font.SysFont('simhei', 72)
        except:
            try:
                chinese_font = pygame.font.SysFont('mingliub', 72)
            except:
                # Last resort - try any available font
                chinese_font = pygame.font.SysFont('arial', 72)

# UI fonts - using more visually pleasing fonts
try:
    # Try modern, clean fonts for menu
    menu_title_font = pygame.font.SysFont('segoeui', 64, bold=True)
    menu_font = pygame.font.SysFont('segoeui', 32)
    ui_font = pygame.font.SysFont('segoeui', 36)
    input_font = pygame.font.SysFont('segoeui', 32)
    small_font = pygame.font.SysFont('segoeui', 24)
except:
    # Fallback to Arial
    menu_title_font = pygame.font.SysFont('arial', 64, bold=True)
    menu_font = pygame.font.SysFont('arial', 32)
    ui_font = pygame.font.SysFont('arial', 36)
    input_font = pygame.font.SysFont('arial', 32)
    small_font = pygame.font.SysFont('arial', 24)

# Character database from Lessons 7 and 8
# Format: 'character': {'pinyin': [...], 'meaning': [...]}
LESSON_7_DATA = {
    '點': {'pinyin': ['dian3'], 'meaning': ["o'clock", "oclock"]},
    '唱歌': {'pinyin': ['chang4ge1', 'changge'], 'meaning': ['sing', 'to sing']},
    '分': {'pinyin': ['fen1'], 'meaning': ['minute']},
    '見面': {'pinyin': ['jian4mian4', 'jianmian'], 'meaning': ['meet', 'to meet']},
    '從': {'pinyin': ['cong2'], 'meaning': ['from']},
    '中午': {'pinyin': ['zhong1wu3', 'zhongwu'], 'meaning': ['noon']},
    '得': {'pinyin': ['de', 'dei3'], 'meaning': ['must', 'resultative complement']},
    '銀行': {'pinyin': ['yin2hang2', 'yinhang'], 'meaning': ['bank']},
    '時候': {'pinyin': ['shi2hou4', 'shihou'], 'meaning': ['when']},
    '後天': {'pinyin': ['hou4tian1', 'houtian'], 'meaning': ['the day after tomorrow', 'day after tomorrow']},
    '下次': {'pinyin': ['xia4ci4', 'xiaci'], 'meaning': ['next time']},
    '沒問題': {'pinyin': ['mei2wen4ti2', 'meiwenti'], 'meaning': ['no problem']},
    '對了': {'pinyin': ['dui4le', 'duile'], 'meaning': ['by the way']},
    '有空': {'pinyin': ['you3kong4', 'youkong'], 'meaning': ['have free time', 'to have free time']},
    '再見': {'pinyin': ['zai4jian4', 'zaijian'], 'meaning': ['goodbye']},
    '在': {'pinyin': ['zai4'], 'meaning': ['at', 'progressive']},
    '午餐': {'pinyin': ['wu3can1', 'wucan'], 'meaning': ['lunch']},
    '剛': {'pinyin': ['gang1'], 'meaning': ['just now']},
    '下課': {'pinyin': ['xia4ke4', 'xiake'], 'meaning': ['finish class', 'to finish class']},
    '下午': {'pinyin': ['xia4wu3', 'xiawu'], 'meaning': ['afternoon']},
    '半': {'pinyin': ['ban4'], 'meaning': ['half']},
    '比賽': {'pinyin': ['bi3sai4', 'bisai'], 'meaning': ['game', 'competition']},
    '結束': {'pinyin': ['jie2shu4', 'jieshu'], 'meaning': ['finish', 'to finish']},
    '最近': {'pinyin': ['zui4jin4', 'zuijin'], 'meaning': ['recently', 'lately']},
    '忙': {'pinyin': ['mang2'], 'meaning': ['busy']},
    '每': {'pinyin': ['mei3'], 'meaning': ['every', 'each']},
    '天': {'pinyin': ['tian1'], 'meaning': ['day', 'measure word for day']},
    '書法': {'pinyin': ['shu1fa3', 'shufa'], 'meaning': ['calligraphy']},
    '課': {'pinyin': ['ke4'], 'meaning': ['class']},
    '開始': {'pinyin': ['kai1shi3', 'kaishi'], 'meaning': ['begin', 'to begin', 'start', 'to start']},
    '字': {'pinyin': ['zi4'], 'meaning': ['character']},
    '寫': {'pinyin': ['xie3'], 'meaning': ['write', 'to write']},
    '可以': {'pinyin': ['ke3yi3', 'keyi'], 'meaning': ['may']},
    '問': {'pinyin': ['wen4'], 'meaning': ['ask', 'to ask']},
    '等一下': {'pinyin': ['deng3yi2xia4', 'dengyixia'], 'meaning': ['later']},
    '有事': {'pinyin': ['you3shi4', 'youshi'], 'meaning': ['busy', 'to be busy', 'engaged', 'to be engaged']},
    '有意思': {'pinyin': ['you3yi4si', 'youyisi'], 'meaning': ['interesting', 'to be interesting', 'fun', 'to be fun']},
}

LESSON_8_DATA = {
    '坐': {'pinyin': ['zuo4'], 'meaning': ['take', 'to take', 'travel by', 'to travel by']},
    '火車': {'pinyin': ['huo3che1', 'huoche'], 'meaning': ['train']},
    '跟': {'pinyin': ['gen1'], 'meaning': ['with']},
    '玩': {'pinyin': ['wan2'], 'meaning': ['have fun', 'to have fun']},
    '怎麼': {'pinyin': ['zen3me', 'zenme'], 'meaning': ['how']},
    '慢': {'pinyin': ['man4'], 'meaning': ['slow']},
    '鐘頭': {'pinyin': ['zhong1tou2', 'zhongtou'], 'meaning': ['hour']},
    '比較': {'pinyin': ['bi3jiao4', 'bijiao'], 'meaning': ['relatively', 'more']},
    '快': {'pinyin': ['kuai4'], 'meaning': ['fast']},
    '車票': {'pinyin': ['che1piao4', 'chepiao'], 'meaning': ['ticket']},
    '非常': {'pinyin': ['fei1chang2', 'feichang'], 'meaning': ['very']},
    '但是': {'pinyin': ['dan4shi4', 'danshi'], 'meaning': ['but', 'however']},
    '又': {'pinyin': ['you4'], 'meaning': ['both', 'and', 'both and']},
    '舒服': {'pinyin': ['shu1fu2', 'shufu'], 'meaning': ['comfortable']},
    '站': {'pinyin': ['zhan4'], 'meaning': ['station']},
    '或是': {'pinyin': ['huo4shi4', 'huoshi'], 'meaning': ['or']},
    '臺南': {'pinyin': ['tai2nan2', 'tainan'], 'meaning': ['tainan']},
    '高鐵': {'pinyin': ['gao1tie3', 'gaotie'], 'meaning': ['high speed rail', 'tren bala']},
    '網路上': {'pinyin': ['wang3lu4shang4', 'wanglushang'], 'meaning': ['on the internet', 'internet', 'online']},
    '便利商店': {'pinyin': ['bian4li4shang1dian4', 'bianli shangdian', 'bianli4shangdian'], 'meaning': ['convenience store']},
    '同學': {'pinyin': ['tong2xue2', 'tongxue'], 'meaning': ['classmate']},
    '參觀': {'pinyin': ['can1guan1', 'canguan'], 'meaning': ['visit', 'to visit']},
    '古代': {'pinyin': ['gu3dai4', 'gudai'], 'meaning': ['ancient times']},
    '騎': {'pinyin': ['qi2'], 'meaning': ['ride', 'to ride']},
    '機車': {'pinyin': ['ji1che1', 'jiche'], 'meaning': ['motorcycle', 'scooter']},
    '載': {'pinyin': ['zai4'], 'meaning': ['give someone a ride', 'to give someone a ride']},
    '捷運': {'pinyin': ['jie2yun4', 'jieyun'], 'meaning': ['metro']},
    '比': {'pinyin': ['bi3'], 'meaning': ['than']},
    '公車': {'pinyin': ['gong1che1', 'gongche'], 'meaning': ['bus']},
    '不行': {'pinyin': ['bu4xing2', 'buxing'], 'meaning': ['will not do', 'not do']},
    '計程車': {'pinyin': ['ji4cheng2che1', 'jichengche'], 'meaning': ['taxi']},
    '差不多': {'pinyin': ['cha1bu4duo1', 'chabuduo'], 'meaning': ['about']},
}

class FallingCharacter:
    def __init__(self, character, answer_options, x, y, speed):
        self.character = character
        self.answer_options = answer_options  # List of acceptable answers (pinyin or meanings)
        self.x = x
        self.y = y
        self.speed = speed
        self.active = True
        
    def update(self):
        if self.active:
            self.y += self.speed
            
    def draw(self, surface):
        if self.active:
            # Draw character
            text_surface = chinese_font.render(self.character, True, WHITE)
            text_rect = text_surface.get_rect(center=(self.x, self.y))
            surface.blit(text_surface, text_rect)
            
    def is_off_screen(self):
        return self.y > SCREEN_HEIGHT
    
    def check_answer(self, user_input):
        # Check if user input matches any acceptable answer (case insensitive)
        user_input = user_input.lower().strip()
        for answer in self.answer_options:
            if user_input == answer.lower():
                return True
        return False

class Game:
    def __init__(self, lesson_data, game_mode):
        self.lesson_data = lesson_data  # Dictionary of characters for this lesson
        self.game_mode = game_mode  # 'pinyin' or 'meaning'
        self.characters = []
        self.score = 0
        self.lives = 5
        self.level = 1
        self.fall_speed = INITIAL_FALL_SPEED
        self.spawn_timer = 0
        self.spawn_delay = 120  # Frames between spawns
        self.user_input = ""
        self.game_over = False
        self.feedback_message = ""
        self.feedback_timer = 0
        self.new_high_score = False
        
        # Combo system
        self.combo = 0
        self.max_combo = 0
        self.combo_multiplier = 1
        
        # Mistake tracking
        self.mistakes = []  # List of (character, correct_answer, user_answer)
        self.missed_characters = []  # Characters that fell off screen
        
    def spawn_character(self):
        # Pick random character from lesson data
        character = random.choice(list(self.lesson_data.keys()))
        char_data = self.lesson_data[character]
        
        # Get answer options based on game mode
        if self.game_mode == 'pinyin':
            answer_options = char_data['pinyin']
        else:  # meaning mode
            answer_options = char_data['meaning']
        
        # Ensure character spawns within visible bounds (with margin for character size)
        x = random.randint(100, SCREEN_WIDTH - 100)
        y = -50
        new_char = FallingCharacter(character, answer_options, x, y, self.fall_speed)
        self.characters.append(new_char)
        
    def update(self):
        global high_score
        
        if self.game_over:
            return
            
        # Spawn new characters
        self.spawn_timer += 1
        if self.spawn_timer >= self.spawn_delay:
            self.spawn_character()
            self.spawn_timer = 0
            
        # Update all characters
        for char in self.characters[:]:
            char.update()
            
            # Check if character fell off screen
            if char.is_off_screen() and char.active:
                self.lives -= 1
                # Track missed character
                self.missed_characters.append((char.character, char.answer_options[0]))
                self.characters.remove(char)
                self.feedback_message = "Missed!"
                self.feedback_timer = 60
                sound_miss.play()
                
                # Reset combo
                self.combo = 0
                self.combo_multiplier = 1
                
                if self.lives <= 0:
                    self.game_over = True
                    # Check if new high score
                    if self.score > high_score:
                        high_score = self.score
                        self.new_high_score = True
                        save_high_score(high_score)
                    
        # Update feedback timer
        if self.feedback_timer > 0:
            self.feedback_timer -= 1
            
        # Check for level up
        if self.score > 0 and self.score % 100 == 0 and self.score != self.level * 100:
            self.level_up()
            
    def level_up(self):
        self.level += 1
        self.fall_speed += SPEED_INCREMENT
        self.spawn_delay = max(60, self.spawn_delay - 10)
        self.feedback_message = f"Level {self.level}!"
        self.feedback_timer = 90
        
    def check_input(self):
        if not self.user_input:
            return
            
        # Check against all active characters
        for char in self.characters[:]:
            if char.active and char.check_answer(self.user_input):
                # Correct answer!
                # Update combo
                self.combo += 1
                if self.combo > self.max_combo:
                    self.max_combo = self.combo
                
                # Calculate combo multiplier
                if self.combo >= 10:
                    self.combo_multiplier = 3
                elif self.combo >= 5:
                    self.combo_multiplier = 2
                else:
                    self.combo_multiplier = 1
                
                # Award points with multiplier
                points = SCORE_PER_CHARACTER * self.combo_multiplier
                self.score += points
                
                char.active = False
                self.characters.remove(char)
                
                # Show combo in feedback
                if self.combo_multiplier > 1:
                    self.feedback_message = f"Correct! x{self.combo_multiplier} COMBO!"
                else:
                    self.feedback_message = "Correct!"
                self.feedback_timer = 30
                self.user_input = ""
                sound_correct.play()
                return
                
        # If no match found, wrong answer
        # Track the mistake - find which character they were trying to answer
        if self.characters:
            # Assume they were trying to answer the lowest character
            lowest_char = min(self.characters, key=lambda c: c.y)
            self.mistakes.append((lowest_char.character, lowest_char.answer_options[0], self.user_input))
        
        self.feedback_message = "Try again!"
        self.feedback_timer = 30
        sound_wrong.play()
        
        # Reset combo on wrong answer
        self.combo = 0
        self.combo_multiplier = 1
        
    def draw(self, surface):
        # Draw background with current theme
        theme = THEMES[current_theme]
        surface.fill(theme['bg'])
        
        # Draw all characters
        for char in self.characters:
            char.draw(surface)
            
        # Draw UI
        mode_text = "PINYIN" if self.game_mode == 'pinyin' else "MEANING"
        mode_display = ui_font.render(mode_text, True, theme['accent'])
        score_text = ui_font.render(f"Score: {self.score}", True, theme['text'])
        lives_text = ui_font.render(f"Lives: {self.lives}", True, theme['text'])
        level_text = ui_font.render(f"Level: {self.level}", True, theme['text'])
        
        surface.blit(mode_display, (SCREEN_WIDTH - 180, 10))
        surface.blit(score_text, (10, 10))
        surface.blit(lives_text, (10, 50))
        surface.blit(level_text, (10, 90))
        
        # Draw combo counter
        if self.combo > 1:
            combo_color = theme['accent']
            if self.combo >= 10:
                combo_color = (255, 215, 0)  # Gold for 10+ combo
            elif self.combo >= 5:
                combo_color = (255, 165, 0)  # Orange for 5+ combo
            
            combo_text = ui_font.render(f"COMBO: {self.combo}x", True, combo_color)
            combo_rect = combo_text.get_rect(center=(SCREEN_WIDTH // 2, 50))
            surface.blit(combo_text, combo_rect)
        
        # Draw input box
        input_box_rect = pygame.Rect(SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT - 80, 400, 50)
        pygame.draw.rect(surface, theme['text'], input_box_rect, 2)
        
        input_text = input_font.render(f"Type: {self.user_input}", True, theme['text'])
        input_rect = input_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 55))
        surface.blit(input_text, input_rect)
        
        # Draw feedback message
        if self.feedback_timer > 0:
            if "Correct" in self.feedback_message or "COMBO" in self.feedback_message:
                feedback_color = theme['correct']
            elif "Missed" in self.feedback_message:
                feedback_color = theme['wrong']
            else:
                feedback_color = theme['accent']
            
            feedback_text = ui_font.render(self.feedback_message, True, feedback_color)
            feedback_rect = feedback_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            surface.blit(feedback_text, feedback_rect)
            
        # Draw game over screen
        if self.game_over:
            overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
            overlay.set_alpha(200)
            overlay.fill((0, 0, 0))
            surface.blit(overlay, (0, 0))
            
            game_over_text = chinese_font.render("GAME OVER", True, theme['wrong'])
            final_score_text = ui_font.render(f"Final Score: {self.score}", True, theme['text'])
            max_combo_text = menu_font.render(f"Max Combo: {self.max_combo}x", True, theme['accent'])
            
            # Show if new high score
            y_offset = 0
            if self.new_high_score:
                new_high_text = ui_font.render("NEW HIGH SCORE!", True, theme['accent'])
                surface.blit(new_high_text, new_high_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100)))
                y_offset = 30
            
            restart_text = ui_font.render("Press SPACE to menu or ESC to quit", True, theme['text'])
            
            surface.blit(game_over_text, game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50 + y_offset)))
            surface.blit(final_score_text, final_score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20 + y_offset)))
            surface.blit(max_combo_text, max_combo_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 60 + y_offset)))
            surface.blit(restart_text, restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 110 + y_offset)))

def draw_mistake_review(screen, mistakes, missed_characters, scroll_offset):
    """Draw a review screen showing all mistakes from the game"""
    theme = THEMES[current_theme]
    screen.fill(theme['bg'])
    
    # Draw title
    title_text = menu_title_font.render("Mistake Review", True, theme['text'])
    title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, 40))
    screen.blit(title_text, title_rect)
    
    # Count total mistakes
    total_mistakes = len(mistakes) + len(missed_characters)
    
    if total_mistakes == 0:
        # Perfect game!
        perfect_text = menu_font.render("Perfect! No mistakes!", True, theme['correct'])
        perfect_rect = perfect_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(perfect_text, perfect_rect)
        
        back_text = small_font.render("Press ENTER or ESC to continue", True, theme['text'])
        screen.blit(back_text, back_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50)))
        return
    
    # Draw headers
    header_y = 90
    header_char = small_font.render("Character", True, theme['accent'])
    header_correct = small_font.render("Correct Answer", True, theme['accent'])
    header_your = small_font.render("Your Answer", True, theme['accent'])
    
    screen.blit(header_char, (50, header_y))
    screen.blit(header_correct, (280, header_y))
    screen.blit(header_your, (530, header_y))
    
    pygame.draw.line(screen, theme['text'], (30, 120), (SCREEN_WIDTH - 30, 120), 2)
    
    # Combine all mistakes
    all_mistakes = []
    
    # Add wrong answers
    for char, correct, user_ans in mistakes:
        all_mistakes.append((char, correct, user_ans, "Wrong"))
    
    # Add missed characters
    for char, correct in missed_characters:
        all_mistakes.append((char, correct, "MISSED", "Missed"))
    
    # Scrolling
    content_y = 140
    row_height = 50
    visible_rows = (SCREEN_HEIGHT - 220) // row_height  # Adjusted for new screen height
    start_idx = max(0, scroll_offset)
    end_idx = min(len(all_mistakes), start_idx + visible_rows)
    
    # Draw each mistake
    for i in range(start_idx, end_idx):
        char, correct, user_ans, mistake_type = all_mistakes[i]
        y_pos = content_y + (i - start_idx) * row_height
        
        # Character
        char_font = pygame.font.SysFont('dfkai-sb', 36)
        try:
            if char_font.get_height() == 0:
                char_font = chinese_font
        except:
            char_font = chinese_font
        
        char_text = char_font.render(char, True, theme['text'])
        char_rect = char_text.get_rect()
        char_x = 50 + (200 - char_rect.width) // 2
        screen.blit(char_text, (char_x, y_pos + 5))
        
        # Correct answer (green)
        correct_text = small_font.render(correct, True, theme['correct'])
        screen.blit(correct_text, (280, y_pos + 12))
        
        # User answer (red)
        user_color = theme['wrong']
        user_text = small_font.render(user_ans, True, user_color)
        screen.blit(user_text, (530, y_pos + 12))
    
    # Draw scroll indicators
    if scroll_offset > 0:
        up_arrow = menu_font.render("▲ Scroll Up", True, theme['accent'])
        screen.blit(up_arrow, (SCREEN_WIDTH // 2 - 60, SCREEN_HEIGHT - 100))
    
    if end_idx < len(all_mistakes):
        down_arrow = menu_font.render("▼ Scroll Down", True, theme['accent'])
        screen.blit(down_arrow, (SCREEN_WIDTH // 2 - 70, SCREEN_HEIGHT - 70))
    
    # Draw totals and instruction on separate lines
    count_text = small_font.render(f"Total: {total_mistakes} ({len(mistakes)} wrong, {len(missed_characters)} missed)", True, theme['text'])
    screen.blit(count_text, (30, SCREEN_HEIGHT - 40))
    
    # Draw instruction on the right
    back_text = small_font.render("Press ENTER or ESC to continue", True, theme['text'])
    back_rect = back_text.get_rect(right=SCREEN_WIDTH - 30, bottom=SCREEN_HEIGHT - 15)
    screen.blit(back_text, back_rect)

def draw_content_viewer(screen, lesson_data, lesson_name, scroll_offset):
    """Draw a scrollable content viewer showing all characters in a lesson"""
    theme = THEMES[current_theme]
    screen.fill(theme['bg'])
    
    # Draw title
    title_text = menu_title_font.render(f"{lesson_name} Content", True, theme['text'])
    title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, 40))
    screen.blit(title_text, title_rect)
    
    # Draw column headers (adjusted positions for wider character column)
    header_y = 90
    header_char = small_font.render("Character", True, theme['accent'])
    header_pinyin = small_font.render("Pinyin", True, theme['accent'])
    header_meaning = small_font.render("Meaning", True, theme['accent'])
    
    screen.blit(header_char, (50, header_y))
    screen.blit(header_pinyin, (280, header_y))  # Moved further right
    screen.blit(header_meaning, (530, header_y))  # Moved further right
    
    # Draw a line under headers
    pygame.draw.line(screen, theme['text'], (30, 120), (SCREEN_WIDTH - 30, 120), 2)
    
    # Create scrollable content area
    content_y = 140
    row_height = 50  # Increased from 45 to 50 for better spacing
    visible_rows = (SCREEN_HEIGHT - 200) // row_height
    
    # Get sorted list of characters
    characters = list(lesson_data.keys())
    start_idx = max(0, scroll_offset)
    end_idx = min(len(characters), start_idx + visible_rows)
    
    # Draw each character entry
    for i in range(start_idx, end_idx):
        char = characters[i]
        data = lesson_data[char]
        
        y_pos = content_y + (i - start_idx) * row_height
        
        # Character (Chinese font) - render at larger size without scaling
        # Render at size 36 directly instead of scaling down
        char_font = pygame.font.SysFont('dfkai-sb', 36)
        try:
            if char_font.get_height() == 0:
                char_font = chinese_font
        except:
            char_font = chinese_font
            
        char_text = char_font.render(char, True, theme['text'])
        # Center the character within its column (50-250 = 200px wide column)
        char_rect = char_text.get_rect()
        char_x = 50 + (200 - char_rect.width) // 2  # Center within 200px column
        screen.blit(char_text, (char_x, y_pos + 5))
        
        # Pinyin (show first option)
        pinyin_text = small_font.render(data['pinyin'][0], True, theme['text'])
        screen.blit(pinyin_text, (280, y_pos + 12))  # Moved further right
        
        # Meaning (show first option, truncate if too long)
        meaning = data['meaning'][0]
        if len(meaning) > 22:
            meaning = meaning[:19] + "..."
        meaning_text = small_font.render(meaning, True, theme['text'])
        screen.blit(meaning_text, (530, y_pos + 12))  # Moved further right
    
    # Draw scroll indicators
    if scroll_offset > 0:
        up_arrow = menu_font.render("▲ Scroll Up", True, theme['accent'])
        screen.blit(up_arrow, (SCREEN_WIDTH // 2 - 60, SCREEN_HEIGHT - 100))
    
    if end_idx < len(characters):
        down_arrow = menu_font.render("▼ Scroll Down", True, theme['accent'])
        screen.blit(down_arrow, (SCREEN_WIDTH // 2 - 70, SCREEN_HEIGHT - 70))
    
    # Draw total count on the left
    count_text = small_font.render(f"Total: {len(characters)} words/characters", True, theme['text'])
    screen.blit(count_text, (30, SCREEN_HEIGHT - 40))
    
    # Draw back instruction on the right, properly aligned
    back_text = small_font.render("Press ESC to go back", True, theme['text'])
    back_rect = back_text.get_rect(right=SCREEN_WIDTH - 30, bottom=SCREEN_HEIGHT - 15)
    screen.blit(back_text, back_rect)

def draw_menu(screen, title, options, selected_index):
    """Draw a menu screen with selectable options"""
    theme = THEMES[current_theme]
    screen.fill(theme['bg'])
    
    # Draw title
    title_text = menu_title_font.render(title, True, theme['text'])
    title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, 100))
    screen.blit(title_text, title_rect)
    
    # Draw high score and daily streak if on main menu
    if title == "Falling Characters":
        high_score_text = menu_font.render(f"High Score: {high_score}", True, theme['accent'])
        high_score_rect = high_score_text.get_rect(center=(SCREEN_WIDTH // 2, 180))
        screen.blit(high_score_text, high_score_rect)
        
        # Daily streak (without emoji as it doesn't render properly)
        streak_text = menu_font.render(f"Daily Streak: {daily_streak} day{'s' if daily_streak != 1 else ''}", True, theme['accent'])
        streak_rect = streak_text.get_rect(center=(SCREEN_WIDTH // 2, 220))
        screen.blit(streak_text, streak_rect)
        
        options_start_y = 280
    else:
        options_start_y = 230
    
    # Draw options
    for i, option in enumerate(options):
        color = theme['accent'] if i == selected_index else theme['text']
        option_text = menu_font.render(option, True, color)
        option_rect = option_text.get_rect(center=(SCREEN_WIDTH // 2, options_start_y + i * 60))
        screen.blit(option_text, option_rect)
        
        # Draw arrow for selected option
        if i == selected_index:
            arrow = menu_font.render("►", True, theme['accent'])
            arrow_rect = arrow.get_rect(center=(SCREEN_WIDTH // 2 - 150, options_start_y + i * 60))
            screen.blit(arrow, arrow_rect)
    
    # Draw instructions
    inst_text = small_font.render("Use UP/DOWN arrows and press ENTER to select", True, theme['text'])
    inst_rect = inst_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50))
    screen.blit(inst_text, inst_rect)

def main():
    game = None
    running = True
    
    # Menu states
    menu_state = "main"  # main, lesson_select, mode_select, instructions, playing, content_select, content_view, theme_select, mistake_review
    lesson_selected = None
    mode_selected = None
    selected_option = 0
    scroll_offset = 0  # For content viewer scrolling
    content_lesson = None  # Which lesson content to view
    mistake_scroll = 0  # For mistake review scrolling
    
    # Menu options
    main_menu_options = ["Start Game", "Content", "Themes", "Instructions", "Quit"]
    lesson_menu_options = ["Lesson 7", "Lesson 8", "Back"]
    mode_menu_options = ["Pinyin Mode", "Meaning Mode", "Back"]
    theme_menu_options = [THEMES[key]['name'] for key in THEMES.keys()] + ["Back"]
    
    while running:
        clock.tick(FPS)
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            if event.type == pygame.KEYDOWN:
                if menu_state == "main":
                    if event.key == pygame.K_UP:
                        selected_option = (selected_option - 1) % len(main_menu_options)
                    elif event.key == pygame.K_DOWN:
                        selected_option = (selected_option + 1) % len(main_menu_options)
                    elif event.key == pygame.K_RETURN:
                        if selected_option == 0:  # Start Game
                            menu_state = "lesson_select"
                            selected_option = 0
                        elif selected_option == 1:  # Content
                            menu_state = "content_select"
                            selected_option = 0
                        elif selected_option == 2:  # Themes
                            menu_state = "theme_select"
                            selected_option = 0
                        elif selected_option == 3:  # Instructions
                            menu_state = "instructions"
                        elif selected_option == 4:  # Quit
                            running = False
                    elif event.key == pygame.K_ESCAPE:
                        running = False
                        
                elif menu_state == "lesson_select":
                    if event.key == pygame.K_UP:
                        selected_option = (selected_option - 1) % len(lesson_menu_options)
                    elif event.key == pygame.K_DOWN:
                        selected_option = (selected_option + 1) % len(lesson_menu_options)
                    elif event.key == pygame.K_RETURN:
                        if selected_option == 0:  # Lesson 7
                            lesson_selected = LESSON_7_DATA
                            menu_state = "mode_select"
                            selected_option = 0
                        elif selected_option == 1:  # Lesson 8
                            lesson_selected = LESSON_8_DATA
                            menu_state = "mode_select"
                            selected_option = 0
                        elif selected_option == 2:  # Back
                            menu_state = "main"
                            selected_option = 0
                    elif event.key == pygame.K_ESCAPE:
                        menu_state = "main"
                        selected_option = 0
                
                elif menu_state == "content_select":
                    if event.key == pygame.K_UP:
                        selected_option = (selected_option - 1) % len(lesson_menu_options)
                    elif event.key == pygame.K_DOWN:
                        selected_option = (selected_option + 1) % len(lesson_menu_options)
                    elif event.key == pygame.K_RETURN:
                        if selected_option == 0:  # Lesson 7
                            content_lesson = LESSON_7_DATA
                            menu_state = "content_view"
                            scroll_offset = 0
                        elif selected_option == 1:  # Lesson 8
                            content_lesson = LESSON_8_DATA
                            menu_state = "content_view"
                            scroll_offset = 0
                        elif selected_option == 2:  # Back
                            menu_state = "main"
                            selected_option = 0
                    elif event.key == pygame.K_ESCAPE:
                        menu_state = "main"
                        selected_option = 0
                
                elif menu_state == "content_view":
                    lesson_size = len(content_lesson)
                    max_scroll = max(0, lesson_size - 10)  # Approximate visible items
                    
                    if event.key == pygame.K_UP:
                        scroll_offset = max(0, scroll_offset - 1)
                    elif event.key == pygame.K_DOWN:
                        scroll_offset = min(max_scroll, scroll_offset + 1)
                    elif event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                        menu_state = "content_select"
                        selected_option = 0
                
                elif menu_state == "theme_select":
                    if event.key == pygame.K_UP:
                        selected_option = (selected_option - 1) % len(theme_menu_options)
                    elif event.key == pygame.K_DOWN:
                        selected_option = (selected_option + 1) % len(theme_menu_options)
                    elif event.key == pygame.K_RETURN:
                        if selected_option == len(theme_menu_options) - 1:  # Back
                            menu_state = "main"
                            selected_option = 0
                        else:
                            # Select theme
                            global current_theme
                            theme_keys = list(THEMES.keys())
                            current_theme = theme_keys[selected_option]
                            save_theme(current_theme)
                    elif event.key == pygame.K_ESCAPE:
                        menu_state = "main"
                        selected_option = 0
                
                elif menu_state == "mistake_review":
                    if game:
                        total_mistakes = len(game.mistakes) + len(game.missed_characters)
                        visible_rows = (SCREEN_HEIGHT - 220) // 50  # Match the calculation in draw function
                        max_scroll = max(0, total_mistakes - visible_rows)
                        
                        if event.key == pygame.K_UP:
                            mistake_scroll = max(0, mistake_scroll - 1)
                        elif event.key == pygame.K_DOWN:
                            mistake_scroll = min(max_scroll, mistake_scroll + 1)
                        elif event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE:
                            menu_state = "main"
                            selected_option = 0
                            game = None
                            mistake_scroll = 0
                        
                elif menu_state == "mode_select":
                    if event.key == pygame.K_UP:
                        selected_option = (selected_option - 1) % len(mode_menu_options)
                    elif event.key == pygame.K_DOWN:
                        selected_option = (selected_option + 1) % len(mode_menu_options)
                    elif event.key == pygame.K_RETURN:
                        if selected_option == 0:  # Pinyin Mode
                            mode_selected = 'pinyin'
                            game = Game(lesson_selected, mode_selected)
                            menu_state = "playing"
                        elif selected_option == 1:  # Meaning Mode
                            mode_selected = 'meaning'
                            game = Game(lesson_selected, mode_selected)
                            menu_state = "playing"
                        elif selected_option == 2:  # Back
                            menu_state = "lesson_select"
                            selected_option = 0
                    elif event.key == pygame.K_ESCAPE:
                        menu_state = "lesson_select"
                        selected_option = 0
                        
                elif menu_state == "instructions":
                    if event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE:
                        menu_state = "main"
                        selected_option = 0
                        
                elif menu_state == "playing":
                    if game.game_over:
                        if event.key == pygame.K_SPACE:
                            menu_state = "mistake_review"
                            mistake_scroll = 0
                        elif event.key == pygame.K_ESCAPE:
                            running = False
                    else:
                        if event.key == pygame.K_RETURN:
                            game.check_input()
                            game.user_input = ""
                        elif event.key == pygame.K_BACKSPACE:
                            game.user_input = game.user_input[:-1]
                        elif event.key == pygame.K_ESCAPE:
                            menu_state = "main"
                            selected_option = 0
                            game = None
                        else:
                            # Add character to input
                            if event.unicode.isalnum() or event.unicode in [' ', '']:
                                game.user_input += event.unicode
        
        # Update game if playing
        if menu_state == "playing" and game:
            game.update()
        
        # Draw based on current state
        if menu_state == "main":
            draw_menu(screen, "Falling Characters", main_menu_options, selected_option)
            
        elif menu_state == "lesson_select":
            draw_menu(screen, "Select Lesson", lesson_menu_options, selected_option)
            
        elif menu_state == "mode_select":
            draw_menu(screen, "Select Mode", mode_menu_options, selected_option)
            
        elif menu_state == "instructions":
            theme = THEMES[current_theme]
            screen.fill(theme['bg'])
            title = menu_title_font.render("How to Play", True, theme['text'])
            inst1 = small_font.render("Chinese characters will fall from the top", True, theme['text'])
            inst2 = small_font.render("Type the answer before they reach the bottom", True, theme['text'])
            inst3 = small_font.render("Pinyin Mode: Type pinyin (e.g., ni3, hao3)", True, theme['text'])
            inst4 = small_font.render("Meaning Mode: Type English meaning", True, theme['text'])
            inst5 = small_font.render("Press ENTER to submit your answer", True, theme['text'])
            inst6 = small_font.render("Don't let characters fall! You have 5 lives", True, theme['text'])
            
            # Pinyin tone guide
            tone_title = menu_font.render("Pinyin Tone Guide:", True, theme['accent'])
            tone1 = small_font.render("1st tone (ā): High, flat - like singing a high note", True, theme['text'])
            tone2 = small_font.render("2nd tone (á): Rising - like asking 'what?'", True, theme['text'])
            tone3 = small_font.render("3rd tone (ǎ): Falling then rising - like 'huh?'", True, theme['text'])
            tone4 = small_font.render("4th tone (à): Sharp falling - like a command 'Stop!'", True, theme['text'])
            tone5 = small_font.render("5th tone (a): Neutral/light - short and unstressed", True, theme['text'])
            tone_note = small_font.render("Type tones with numbers: ma1, ma2, ma3, ma4, or just 'ma'", True, theme['correct'])
            
            back = menu_font.render("Press ENTER or ESC to go back", True, theme['accent'])
            
            screen.blit(title, title.get_rect(center=(SCREEN_WIDTH // 2, 40)))
            screen.blit(inst1, inst1.get_rect(center=(SCREEN_WIDTH // 2, 100)))
            screen.blit(inst2, inst2.get_rect(center=(SCREEN_WIDTH // 2, 130)))
            screen.blit(inst3, inst3.get_rect(center=(SCREEN_WIDTH // 2, 160)))
            screen.blit(inst4, inst4.get_rect(center=(SCREEN_WIDTH // 2, 190)))
            screen.blit(inst5, inst5.get_rect(center=(SCREEN_WIDTH // 2, 220)))
            screen.blit(inst6, inst6.get_rect(center=(SCREEN_WIDTH // 2, 250)))
            
            screen.blit(tone_title, tone_title.get_rect(center=(SCREEN_WIDTH // 2, 300)))
            screen.blit(tone1, tone1.get_rect(center=(SCREEN_WIDTH // 2, 340)))
            screen.blit(tone2, tone2.get_rect(center=(SCREEN_WIDTH // 2, 370)))
            screen.blit(tone3, tone3.get_rect(center=(SCREEN_WIDTH // 2, 400)))
            screen.blit(tone4, tone4.get_rect(center=(SCREEN_WIDTH // 2, 430)))
            screen.blit(tone5, tone5.get_rect(center=(SCREEN_WIDTH // 2, 460)))
            screen.blit(tone_note, tone_note.get_rect(center=(SCREEN_WIDTH // 2, 500)))
            
            screen.blit(back, back.get_rect(center=(SCREEN_WIDTH // 2, 560)))
            
        elif menu_state == "content_select":
            draw_menu(screen, "Select Lesson Content", lesson_menu_options, selected_option)
            
        elif menu_state == "content_view":
            lesson_name = "Lesson 7" if content_lesson == LESSON_7_DATA else "Lesson 8"
            draw_content_viewer(screen, content_lesson, lesson_name, scroll_offset)
        
        elif menu_state == "theme_select":
            draw_menu(screen, "Select Theme", theme_menu_options, selected_option)
        
        elif menu_state == "mistake_review":
            if game:
                draw_mistake_review(screen, game.mistakes, game.missed_characters, mistake_scroll)
            
        elif menu_state == "playing" and game:
            game.draw(screen)
        
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()