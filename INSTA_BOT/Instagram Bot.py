import schedule
import time
import pyjokes
from instagrapi import Client
from PIL import Image, ImageDraw, ImageFont

# Initialize the Instagram client
client = Client()

# Login credentials
username = "_python_code_challenge"
password = "Mayur@2001"

try:
    client.login(username, password)
    print("Logged in successfully!")
except Exception as e:
    print(f"Error logging in: {e}")

# Generate an image with a joke
def create_joke_image(joke_text, output_path="joke_story.jpg"):
    width, height = 1080, 1920  # Instagram Story dimensions
    background_color = (255, 255, 255)  # White background

    # Create a blank image
    image = Image.new("RGB", (width, height), background_color)
    draw = ImageDraw.Draw(image)

    # Load a font
    font_path = "D:\PRACTICE-01\PYTHON\PROJECTS\PROJECT_100\INSTA_BOT\Sriracha\Sriracha-Regular.ttf"  # Adjust this path for your system
    font = ImageFont.truetype(font_path, size=60)

    # Wrap the joke text
    margin = 50
    max_width = width - 2 * margin
    lines = []
    words = joke_text.split(" ")
    current_line = ""
    for word in words:
        test_line = f"{current_line} {word}".strip()
        if draw.textsize(test_line, font=font)[0] <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)

    # Draw the text
    y_text = (height - len(lines) * 80) // 2  # Center vertically
    for line in lines:
        text_width, text_height = draw.textsize(line, font=font)
        x_text = (width - text_width) // 2  # Center horizontally
        draw.text((x_text, y_text), line, fill="black", font=font)
        y_text += 80  # Line spacing

    # Save the image
    image.save(output_path)

# Post the joke as an Instagram story
def post_joke_story():
    joke = pyjokes.get_joke()
    create_joke_image(joke)
    try:
        client.photo_upload_to_story("joke_story.jpg", caption="Here's a joke for you! 😄")
        print("Joke posted to story!")
    except Exception as e:
        print(f"Error posting story: {e}")

# Schedule the joke posting
schedule.every().day.at("10:00").do(post_joke_story)
schedule.every().day.at("15:00").do(post_joke_story)
schedule.every().day.at("20:00").do(post_joke_story)

# Run the scheduler
print("Bot is running...")
while True:
    schedule.run_pending()
    time.sleep(1)
