import gradio as gr
from openai import OpenAI

api_key = "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"

openai = OpenAI(api_key=api_key)

theme = gr.themes.Base(
    primary_hue="yellow",
    secondary_hue="fuchsia",
    neutral_hue="cyan")

def segment_story(story):
    try:
        response = openai.chat.completions.create(
            model="gpt-4-0613",
            messages=[
                {"role": "system", "content": "You are an expert story segmenter."},
                {"role": "user", "content": f"Divide this story into exactly six chronological parts,"
                                            f" between every two parts put the character &: {story}"}
            ],
            max_tokens=1500
        )
        parts = response.choices[0].message.content.strip().split('&')
        for part in parts:
            print(part)
        return parts
    except Exception as e:
        print(e)
        return []


def generate_images(sub_stories):
    images = []
    for story in sub_stories:
        try:
            response = openai.images.generate(
                model="dall-e-2",
                prompt=story,
                n=1,
                size="1024x1024"
            )
            image_url = response.data[0].url
            images.append(image_url)
        except Exception as e:
            print(e)
            images.append("Error generating image")
    return images


def process_story(story):
    sub_stories = segment_story(story)
    if sub_stories:
        return generate_images(sub_stories)
    else:
        return ["Error in story segmentation"]


def set_personal_prompt(gender, distance, style, triggers):
    pass


# Create a Gradio interface
with gr.Blocks(theme=theme) as app:
    gr.Markdown('<h1 style="font-size:50px;"> MIND CANVAS</h1>')
    gr.Image("background-image.jpeg", elem_id="background-image")
    personal_prompt = ""
    with gr.Row(elem_id="overlay"):
        with gr.Column():
            gr.Markdown("<h2>How to support your loved one with PTSD?</h2>")
            gr.Button("Continue as a loved one", elem_classes="loved_one_button", variant='primary').click(fn=None)
            gr.Button("Continue as a relative", elem_id="relative_button").click(fn=None)
            gender = gr.Dropdown(["Male", "Female", "Other"], type="value", label="Gender")

            style = gr.Textbox(lines=1, placeholder="Cartoon / realistic / hand-drawn...", label="Choose a style")
            triggers = gr.Textbox(lines=3, placeholder="Enter what you don't want to see...", label="Triggers")
            personal_prompt = set_personal_prompt(gender, distance, style, triggers)

    with gr.Column():
        gr.Markdown("## Story to Image Sequence Generator")
        gr.Markdown("Enter a complete story and generate a sequence of images representing different parts of the story.")

    with gr.Column():
        story_input = gr.Textbox(lines=10, placeholder="Enter a full story here...", label="Story Input")
        submit_button = gr.Button("Generate Images", variant='primary')
        output_gallery = gr.Gallery(label="Generated Images")
    submit_button.click(fn=process_story, inputs=story_input, outputs=output_gallery)

if __name__ == "__main__":
    app.launch()