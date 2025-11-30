# Falling Characters - Complete Game Manual

## 📚 Table of Contents
1. [Game Overview](#game-overview)
2. [How to Play](#how-to-play)
3. [Game Modes](#game-modes)
4. [Scoring System](#scoring-system)
5. [Combo System](#combo-system)
6. [Lives & Game Over](#lives--game-over)
7. [Level Progression](#level-progression)
8. [Mistake Review System](#mistake-review-system)
9. [Daily Streak Tracker](#daily-streak-tracker)
10. [Content Viewer](#content-viewer)
11. [Theme System](#theme-system)
12. [Instructions Section](#instructions-section)
13. [Tips & Strategies](#tips--strategies)
14. [Keyboard Controls](#keyboard-controls)
15. [Files & Data](#files--data)

---

## Game Overview

**Falling Characters** is an educational typing game designed to help you learn Traditional Chinese characters from the textbook "當代中文課程1" (Contemporary Chinese Course 1), specifically Lessons 7 and 8.

### Core Concept
Chinese characters fall from the top of the screen. You must type the correct answer (pinyin or English meaning) before they reach the bottom. Miss too many and it's game over!

### Educational Value
- **Active Recall**: Type answers from memory, strengthening neural pathways
- **Spaced Repetition**: Characters appear randomly, providing natural review
- **Immediate Feedback**: Know instantly if you're correct or not
- **Mistake Tracking**: Review what you got wrong after each session
- **Progress Tracking**: Daily streaks and high scores motivate consistent practice

---

## How to Play

### Starting a Game

1. **Launch the game** - Double-click the executable or run the Python file
2. **Main Menu** - You'll see:
   - High Score (your best score ever)
   - Daily Streak (consecutive days played)
   - Menu options
3. **Select "Start Game"** - Press ENTER
4. **Choose Lesson** - Lesson 7 or Lesson 8
5. **Choose Mode** - Pinyin Mode or Meaning Mode
6. **Play!** - Characters start falling immediately

### During Gameplay

**The Screen Shows:**
- **Top Left**: Score, Lives (starts at 5), Level (starts at 1)
- **Top Right**: Current mode (PINYIN or MEANING)
- **Top Center**: Combo counter (appears after 2+ correct answers)
- **Center**: Falling Chinese characters
- **Bottom**: Input box where you type your answers
- **Middle**: Feedback messages ("Correct!", "Try again!", "Missed!")

**Game Flow:**
1. A character appears at the top and starts falling
2. Type the answer in the input box
3. Press ENTER to submit
4. If correct: Character disappears, you get points
5. If wrong: Try again! Character keeps falling
6. If it reaches the bottom: You lose a life

---

## Game Modes

### Pinyin Mode
**What you type:** The pinyin pronunciation with tone numbers

**Examples:**
- Character: 你 → Type: `ni3`
- Character: 好 → Type: `hao3`
- Character: 唱歌 → Type: `chang4ge1` or `changge`

**Tips:**
- Tone numbers are recommended but not always required
- Multiple pinyin variations are accepted
- No spaces needed for multi-character words

### Meaning Mode
**What you type:** The English translation

**Examples:**
- Character: 你 → Type: `you`
- Character: 好 → Type: `good`
- Character: 唱歌 → Type: `sing` or `to sing`

**Tips:**
- Both "verb" and "to verb" forms are accepted
- Multiple meanings accepted for flexible learning
- Type exactly as shown in your lesson content

---

## Scoring System

### Base Points
- **10 points** per correct character (at 1x combo)

### Point Calculation
```
Points Earned = Base Points (10) × Combo Multiplier
```

### Examples
- **No combo** (first answer): 10 points
- **5-answer combo**: 20 points (10 × 2)
- **10-answer combo**: 30 points (10 × 3)

### Total Score
Your total score is the sum of all points earned in a game session.

### High Score
- The highest score you've ever achieved
- Saved automatically to `high_score.txt`
- Displayed on the main menu
- Persists across game sessions

---

## Combo System

The combo system rewards consecutive correct answers with bonus points!

### How It Works

**Building a Combo:**
1. Answer first character correctly → No combo yet
2. Answer second character correctly → Combo starts! (2x)
3. Keep answering correctly → Combo increases
4. At 5 correct answers → 2x multiplier
5. At 10 correct answers → 3x multiplier

### Combo Levels

| Combo Count | Multiplier | Points per Character | Display Color |
|-------------|------------|---------------------|---------------|
| 0-1         | 1x         | 10 points           | Normal        |
| 2-4         | 1x         | 10 points           | Yellow        |
| 5-9         | 2x         | 20 points           | Orange        |
| 10+         | 3x         | 30 points           | Gold          |

### Breaking the Combo

Your combo resets to 0 when you:
- ❌ Type a wrong answer
- 💔 Miss a character (let it fall off screen)

### Combo Display

**Location:** Top center of screen

**When visible:** Only shows when combo ≥ 2

**What you see:**
- "COMBO: 5x" (shows current combo count)
- Color changes based on combo level
- Feedback shows "Correct! x2 COMBO!" when multiplier is active

### Strategy Tips

1. **Focus on accuracy first** - One mistake ruins your combo
2. **Start with easier mode** - Build confidence with Pinyin mode
3. **Practice one lesson** - Master Lesson 7 before mixing
4. **Watch for patterns** - Some characters are easier than others
5. **Stay calm** - Rushing leads to typos and broken combos

### Maximum Combo

Your highest combo in a game session is tracked and displayed at game over.

---

## Lives & Game Over

### Lives System

**Starting Lives:** 5 ♥♥♥♥♥

**Losing Lives:**
- Each character that falls off the bottom = -1 life
- Wrong answers do NOT cost lives (try again!)

**Display:**
Top left corner shows: "Lives: X"

### Game Over Trigger

When lives reach 0, the game ends immediately.

### Game Over Screen Shows:

1. **"GAME OVER"** banner (red text)
2. **Final Score** - Your total points
3. **Max Combo** - Highest combo you achieved
4. **"NEW HIGH SCORE!"** - If you beat your record (yellow text)
5. **Instructions** - "Press SPACE to menu or ESC to quit"

### After Game Over

Press **SPACE** → Goes to **Mistake Review** screen
Press **ESC** → Exits the game

---

## Level Progression

### How Levels Work

The game automatically increases in difficulty as you play!

**Starting:** Level 1

**Level Up Trigger:** Every 100 points

**Example:**
- 0-99 points: Level 1
- 100-199 points: Level 2
- 200-299 points: Level 3
- And so on...

### What Changes Each Level

1. **Fall Speed Increases**
   - Starting speed: 1 pixel per frame
   - Increase: +0.2 pixels per frame per level
   - Example: Level 5 = 1.8 pixels per frame

2. **Spawn Rate Increases**
   - Starting delay: 120 frames (2 seconds at 60 FPS)
   - Decrease: -10 frames per level
   - Minimum: 60 frames (1 second)
   - Example: Level 5 = 80 frames between spawns

### Level Display

**Location:** Top left corner

**Format:** "Level: X"

**Feedback:** When you level up, you see "Level X!" message in the center

### Strategy by Level

**Levels 1-3 (Easy):**
- Perfect for learning new characters
- Take your time, build accuracy
- Focus on memorizing pinyin/meanings

**Levels 4-6 (Medium):**
- Speed becomes a factor
- Need to recognize characters quickly
- Good for building combos

**Levels 7+ (Hard):**
- Fast-paced, intense gameplay
- Requires mastery of the vocabulary
- Multiple characters on screen at once

---

## Mistake Review System

After every game, you'll see a detailed breakdown of your mistakes - one of the most powerful learning features!

### What It Shows

**Mistake Review Screen displays a table with:**
- **Character** - The Chinese character/word you missed
- **Correct Answer** - What you should have typed
- **Your Answer** - What you actually typed (or "MISSED")

### Types of Mistakes Tracked

1. **Wrong Answers** 
   - You typed something incorrect
   - Shows what you typed vs. correct answer
   - Example: Character 時候 | Correct: shi2hou4 | You typed: gan1

2. **Missed Characters**
   - Character fell off screen before you answered
   - Shows "MISSED" in red
   - Example: Character 剛 | Correct: gang1 | MISSED

### How to Use It

**Navigation:**
- Use **UP/DOWN** arrow keys to scroll through mistakes
- Shows ~9 mistakes at a time
- Scroll indicators appear at bottom: "▲ Scroll Up" / "▼ Scroll Down"

**Bottom displays:**
- **Left side**: Total mistakes count (e.g., "Total: 6 (1 wrong, 5 missed)")
- **Right side**: "Press ENTER or ESC to continue"

**Press ENTER or ESC** → Returns to main menu

### Learning from Mistakes

**Effective Review Strategy:**

1. **Immediate Review** - Don't skip this screen!
2. **Identify Patterns** - Are you missing certain tones? Similar characters?
3. **Write It Down** - Keep a notebook of frequently missed characters
4. **Screenshot** - Take a photo for later review
5. **Practice Target** - Focus on your mistake characters next game

**Common Patterns to Look For:**
- **Tone confusion** - Getting pinyin right but wrong tone
- **Similar characters** - Confusing 很 and 跟, etc.
- **Multi-character words** - Forgetting compound words
- **Speed issues** - All "MISSED" means you need to type faster

### Perfect Game

If you make NO mistakes (rare and impressive!):
- Screen shows: **"Perfect! No mistakes!"** (green text)
- No table displayed
- Press ENTER to continue to main menu

---

## Daily Streak Tracker

Track your learning consistency with the daily streak system!

### How It Works

**First Time Playing:**
- Streak starts at: **1 day**
- Saved to `daily_streak.txt`

**Playing Next Day:**
- If you play within 24 hours: Streak increases by 1
- Display: "Daily Streak: 2 days"

**Playing Same Day:**
- Streak doesn't increase
- Multiple sessions count as one day
- Display remains same

**Missing a Day:**
- Streak resets to: **1 day**
- Start over! (But your high score remains)

### Streak Display

**Location:** Main menu, below high score

**Format:** 
- "Daily Streak: X day" (singular)
- "Daily Streak: X days" (plural)

**Updates:** Automatically when you launch the game

### Streak Milestones

While not formally tracked in-game, aim for:
- 🎯 **3 days** - Great start!
- 🎯 **7 days** - One week streak!
- 🎯 **14 days** - Two weeks!
- 🎯 **30 days** - One month! Excellent dedication!
- 🎯 **100 days** - Master level commitment!

### Tips for Building Streaks

1. **Play at the same time daily** - Morning or evening routine
2. **Set a phone reminder** - Don't forget!
3. **Even 5 minutes counts** - One quick game is enough
4. **Tell a friend** - Accountability helps
5. **Track on calendar** - Mark off each day you play

### Technical Details

**File:** `daily_streak.txt`
**Contents:** 
```
2024-01-15
7
```
(Last play date and current streak)

**Time Zone:** Uses your computer's system time
**Reset Time:** Midnight in your local time zone

---

## Content Viewer

Review all vocabulary from Lessons 7 and 8 anytime!

### Accessing Content Viewer

1. Main menu → Select **"Content"**
2. Choose **Lesson 7** or **Lesson 8**
3. View scrollable vocabulary list

### What You See

**Table with three columns:**
- **Character** - Chinese character/word (centered, large)
- **Pinyin** - Pronunciation with tone numbers
- **Meaning** - English translation

**Example:**
```
Character    Pinyin          Meaning
點           dian3           o'clock
唱歌         chang4ge1       to sing
分           fen1            minute
```

### Features

**Scrolling:**
- Use **UP/DOWN** arrows to scroll
- Indicators at bottom: "▲ Scroll Up" / "▼ Scroll Down"

**Display:**
- ~9 items visible at once
- Characters centered for easy reading
- Clean, organized layout

**Bottom shows:**
- Total count: "Total: 37 words/characters"
- Exit instruction: "Press ESC to go back"

### How to Use It

**Before Playing:**
- Review vocabulary you'll encounter
- Familiarize yourself with new characters
- Practice pronunciation

**After Playing:**
- Look up characters you struggled with
- Cross-reference with mistake review
- Study meanings and pinyin together

**General Study:**
- Quick reference while doing homework
- Compare similar characters
- Print or screenshot for flashcards

### Lesson Content Summary

**Lesson 7: 早上九點去KTV (Going to KTV at 9 O'Clock in the Morning)**
- 37 words/characters
- Topics: Time, daily activities, making plans
- Key words: 點 (o'clock), 唱歌 (sing), 時候 (when), 有空 (have free time)

**Lesson 8: 坐火車去臺南 (Taking a Train to Tainan)**
- 33 words/characters
- Topics: Transportation, travel, comparisons
- Key words: 坐 (take), 火車 (train), 怎麼 (how), 快 (fast)

---

## Theme System

Customize the visual appearance of your game with 6 beautiful themes!

### Available Themes

#### 1. Default Blue (Original)
- **Background:** Cornflower blue
- **Text:** White
- **Accent:** Yellow
- **Vibe:** Friendly, casual, energetic
- **Best for:** General use, beginners

#### 2. Dark Mode
- **Background:** Dark gray-blue
- **Text:** Light gray
- **Accent:** Light blue
- **Vibe:** Modern, easy on eyes
- **Best for:** Night study, reducing eye strain

#### 3. Forest
- **Background:** Forest green
- **Text:** Ivory
- **Accent:** Gold
- **Vibe:** Nature, calming, grounded
- **Best for:** Relaxed practice, stress relief

#### 4. Sunset
- **Background:** Coral/orange
- **Text:** White
- **Accent:** Gold
- **Vibe:** Warm, energetic, vibrant
- **Best for:** Morning energy, motivation

#### 5. Ocean
- **Background:** Deep ocean blue
- **Text:** Alice blue
- **Accent:** Cyan
- **Vibe:** Calm, focused, deep
- **Best for:** Deep focus sessions, meditation

#### 6. Traditional Chinese
- **Background:** Dark red
- **Text:** Gold
- **Accent:** Light yellow
- **Vibe:** Cultural, elegant, classic
- **Best for:** Immersive Chinese learning experience

### Changing Themes

**Steps:**
1. Main menu → Select **"Themes"**
2. Use **UP/DOWN** arrows to browse themes
3. Press **ENTER** to apply selected theme
4. See instant preview on the menu
5. Press **ESC** to go back (keeps selected theme)

### Theme Persistence

**Automatic Saving:**
- Selected theme saved to `theme.txt`
- Applies to ALL screens (menus, gameplay, content viewer)
- Persists between game sessions
- Loads automatically on startup

### All Screens Use Your Theme

The theme affects:
- ✓ Main menu
- ✓ All sub-menus (content, themes, instructions)
- ✓ Gameplay screen
- ✓ Game over screen
- ✓ Mistake review
- ✓ Content viewer

### Choosing the Right Theme

**For Different Times:**
- Morning: Sunset or Default Blue
- Afternoon: Default Blue or Ocean
- Evening: Dark Mode or Forest
- Night: Dark Mode (easiest on eyes)

**For Different Moods:**
- Need energy: Sunset
- Want calm: Ocean or Forest
- Feeling cultural: Traditional Chinese
- Just comfortable: Dark Mode or Default Blue

**For Different Settings:**
- Bright room: Any theme works
- Dark room: Dark Mode recommended
- Outdoor: Default Blue (highest contrast)
- Library/Public: Dark Mode (less distracting to others)

---

## Instructions Section

The in-game instructions provide a quick reference guide.

### Accessing Instructions

Main menu → Select **"Instructions"** → Press ENTER

### What's Included

**Gameplay Overview:**
1. "Chinese characters will fall from the top"
2. "Type the answer before they reach the bottom"
3. "Pinyin Mode: Type pinyin (e.g., ni3, hao3)"
4. "Meaning Mode: Type English meaning"
5. "Press ENTER to submit your answer"
6. "Don't let characters fall! You have 5 lives"

**Pinyin Tone Guide:**

Comprehensive explanation of Mandarin tones:

**1st Tone (ā):** High, flat - like singing a high note
- Example: mā (妈, mother)
- Pitch: ━━━

**2nd Tone (á):** Rising - like asking 'what?'
- Example: má (麻, numb)
- Pitch: ╱

**3rd Tone (ǎ):** Falling then rising - like 'huh?'
- Example: mǎ (马, horse)
- Pitch: ╲╱

**4th Tone (à):** Sharp falling - like a command 'Stop!'
- Example: mà (骂, to scold)
- Pitch: ╲

**5th Tone (a):** Neutral/light - short and unstressed
- Example: ma (吗, question particle)
- Pitch: (no mark)

**Typing Instructions:**
"Type tones with numbers: ma1, ma2, ma3, ma4, or just 'ma'"

### Using the Instructions

**Before First Game:**
- Read through completely
- Understand tone system
- Learn input format

**As Reference:**
- Come back when confused
- Check tone explanations
- Verify input format

**Exit:**
Press **ENTER** or **ESC** to go back to main menu

---

## Tips & Strategies

### For Beginners

**Week 1: Learning the Ropes**
1. Start with **Lesson 7, Pinyin Mode**
2. Use **Content Viewer** to study before playing
3. Don't worry about score - focus on accuracy
4. Review **Mistake Review** after every game
5. Goal: 50% accuracy, understand all characters

**Week 2: Building Confidence**
1. Continue Lesson 7, try **Meaning Mode**
2. Try to build a **5x combo**
3. Use mistakes to identify weak characters
4. Goal: 70% accuracy, reach Level 3

**Week 3: Expanding Knowledge**
1. Try **Lesson 8, Pinyin Mode**
2. Practice your weak characters from Lesson 7
3. Try to beat your **high score**
4. Goal: 75% accuracy, 10x combo

**Week 4: Mastery**
1. Mix both lessons
2. Try both modes
3. Focus on **daily streak**
4. Goal: 85% accuracy, Level 5+, 15x combo

### Advanced Strategies

**Speed Techniques:**
1. **Touch Typing** - Don't look at keyboard
2. **Muscle Memory** - Practice common characters repeatedly
3. **Anticipation** - Predict next character based on lesson patterns
4. **Peripheral Vision** - See multiple characters at once

**Accuracy Techniques:**
1. **Slow Down** - Speed comes with practice
2. **Read Fully** - Don't guess from first glance
3. **Tone Marks** - Always include tone numbers in pinyin
4. **Double Check** - Scan before pressing ENTER

**Combo Building:**
1. **Start Fresh** - Play when alert and focused
2. **Remove Distractions** - Quiet environment
3. **Warm Up** - Play an easy game first
4. **Stay Calm** - Don't panic as speed increases

**High Score Tactics:**
1. **Build Combos** - 3x multiplier is massive
2. **Survive Long** - More levels = more points
3. **Know Your Weakness** - Practice problem characters beforehand
4. **Perfect Practice** - Use Content Viewer before playing

### Study Schedule Suggestions

**Daily (15-20 minutes):**
- 1-2 games
- Review mistakes
- Keep streak alive

**3x per week (30 minutes):**
- 3-4 games
- Content Viewer review
- Focus on weak areas

**Weekly (1 hour):**
- Marathon session
- Try to beat high score
- Alternate lessons and modes
- Track progress

### Dealing with Frustration

**When you're struggling:**
1. **Take a Break** - Come back in 10 minutes
2. **Change Theme** - Fresh visuals help
3. **Switch Mode** - Try the other mode
4. **Review Content** - Study before playing
5. **Lower Expectations** - Progress isn't always linear

**Remember:**
- Learning takes time
- Mistakes are normal and valuable
- Daily practice beats cramming
- Have fun! It's a game!

---

## Keyboard Controls

### Universal Controls

| Key | Action |
|-----|--------|
| **UP Arrow** | Move selection up in menus / Scroll up in content |
| **DOWN Arrow** | Move selection down in menus / Scroll down in content |
| **ENTER** | Confirm selection / Submit answer / Continue |
| **ESC** | Go back / Exit |

### During Gameplay

| Key | Action |
|-----|--------|
| **Any Letter/Number** | Type your answer |
| **BACKSPACE** | Delete last character |
| **ENTER** | Submit answer |
| **ESC** | Quit to main menu |

### Menu Navigation

**Main Menu:**
- UP/DOWN: Select option
- ENTER: Confirm
- ESC: Quit game

**Lesson Selection:**
- UP/DOWN: Choose lesson
- ENTER: Confirm
- ESC: Back to main menu

**Mode Selection:**
- UP/DOWN: Choose mode
- ENTER: Start game
- ESC: Back to lesson selection

**Content Viewer:**
- UP/DOWN: Scroll through vocabulary
- ESC: Back to content selection

**Theme Selection:**
- UP/DOWN: Browse themes
- ENTER: Apply theme (and stay/go back)
- ESC: Back to main menu

**Mistake Review:**
- UP/DOWN: Scroll through mistakes
- ENTER: Continue to main menu
- ESC: Continue to main menu

### Typing Tips

**For Pinyin:**
- Use numbers for tones: `ma1`, `ma2`, `ma3`, `ma4`
- Or omit tones if accepted: `ma`
- No spaces between syllables: `changge` not `chang ge`

**For Meanings:**
- Lowercase is fine: `hello` or `Hello`
- Articles optional: `to sing` or `sing`
- Exact match required for your lesson data

**General:**
- Type carefully - accuracy over speed
- Use BACKSPACE to fix mistakes before submitting
- Practice touch typing for speed

---

## Files & Data

The game creates several files to save your progress and settings.

### Game Files

**1. high_score.txt**
- **Purpose:** Stores your highest score
- **Contents:** Single number (e.g., `500`)
- **Location:** Same folder as game
- **Updates:** Automatically when you beat your record

**2. daily_streak.txt**
- **Purpose:** Tracks your daily practice streak
- **Contents:** 
  ```
  2024-01-15
  7
  ```
  (Last play date, then current streak)
- **Location:** Same folder as game
- **Updates:** Automatically when you launch game

**3. theme.txt**
- **Purpose:** Remembers your selected theme
- **Contents:** Theme name (e.g., `dark`)
- **Location:** Same folder as game
- **Updates:** When you change themes

### Game Assets

**Sound Files (must be present):**
- `correct.wav` - Plays when answer is correct
- `wrong.wav` - Plays when answer is wrong
- `miss.wav` - Plays when character falls

**Note:** These files must be in the same folder as the game executable or Python file.

### Managing Your Data

**Resetting High Score:**
- Delete `high_score.txt`
- Or edit it to change the number

**Resetting Daily Streak:**
- Delete `daily_streak.txt`
- Or edit the date/number

**Changing Default Theme:**
- Edit `theme.txt`
- Valid values: `default`, `dark`, `forest`, `sunset`, `ocean`, `traditional`

**Complete Reset:**
- Delete all three .txt files
- Game will recreate them with default values

### Backup Your Progress

**To save your progress:**
1. Copy all .txt files to a backup location
2. Copy them back to restore progress

**Useful when:**
- Moving to a new computer
- Reinstalling the game
- Sharing progress with a teacher

---

## Frequently Asked Questions

### Gameplay Questions

**Q: Can I pause the game?**
A: No, characters keep falling. You can press ESC to quit to menu (but lose your progress).

**Q: How do I know which character to answer?**
A: Answer any visible character! The game checks your answer against all active characters.

**Q: What happens if two characters have the same answer?**
A: You'll get points for one of them. The other continues falling.

**Q: Do I lose lives for wrong answers?**
A: No! Only missed characters (falling off screen) cost lives. Wrong answers let you try again.

**Q: Can I change modes during a game?**
A: No, you must finish or quit the current game, then start a new one.

### Technical Questions

**Q: What if sound files are missing?**
A: The game works without sound, but you'll miss audio feedback.

**Q: Can I play without internet?**
A: Yes! This is a fully offline game.

**Q: Does it work on Mac/Linux?**
A: Yes, if you run the Python file or create an executable for your platform.

**Q: How do I update the game?**
A: Download the new version and replace the old file. Your .txt files (progress) are separate.

### Learning Questions

**Q: Which mode is harder - Pinyin or Meaning?**
A: Varies by person! Pinyin is more technical (tones), Meaning requires translation.

**Q: Should I play every day?**
A: Recommended! Daily practice is more effective than cramming. Even 5 minutes helps.

**Q: How long to master both lessons?**
A: Depends on practice frequency. With daily play: 2-4 weeks for solid recognition.

**Q: Can I add more lessons?**
A: Not without modifying the code. This version includes Lessons 7-8 only.

---

## Credits & About

**Game:** Falling Characters
**Version:** 1.0
**Created with:** Python 3, Pygame
**Purpose:** Educational tool for learning Traditional Chinese

**Textbook:** 當代中文課程1 (Contemporary Chinese Course 1)
**Lessons:** 7 and 8

**Features:**
- 70 unique characters/words
- 2 game modes
- 6 themes
- Combo scoring system
- Mistake review
- Daily streak tracking
- Content reference

**Special Thanks:**
- Pygame community
- Chinese language teachers
- Everyone learning Traditional Chinese

---

## Quick Reference Card

```
===========================================
FALLING CHARACTERS - QUICK REFERENCE
===========================================

CONTROLS:
  Arrow Keys → Navigate menus / Scroll
  ENTER → Confirm / Submit
  ESC → Back / Quit
  Letters/Numbers → Type answers
  BACKSPACE → Delete

GAMEPLAY:
  Lives: 5 ♥♥♥♥♥
  Points: 10 per character (×combo)
  Level up: Every 100 points
  
COMBO SYSTEM:
  5+ correct: 2× points
  10+ correct: 3× points
  
GAME MODES:
  Pinyin: Type pronunciation (ni3, hao3)
  Meaning: Type English (you, good)

THEMES:
  1. Default Blue
  2. Dark Mode
  3. Forest
  4. Sunset
  5. Ocean
  6. Traditional Chinese

TIPS:
  • Build daily streaks
  • Review mistakes
  • Focus on accuracy
  • Use Content Viewer
  • Practice combos

FILES SAVED:
  high_score.txt → Best score
  daily_streak.txt → Streak data
  theme.txt → Selected theme

Have fun learning! 加油! (jiāyóu)
===========================================
```

---

**End of Manual**

加油！(jiāyóu - Keep going!)
