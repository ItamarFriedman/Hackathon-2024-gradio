import gradio as gr
from openai import OpenAI

api_key = "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"

personal_wrapper = ""
style_wrapper = ""

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


def generate_image(sub_story):
    print("starting to generate image")
    print("the current substory is:", sub_story)
    try:
        response = openai.images.generate(
            model="dall-e-2",
            prompt=sub_story,
            n=1,
            size="1024x1024"
        )
        image_url = response.data[0].url
    except Exception as e:
        print("Error generating image: ", e)
        return -1
    print("image generated successfully")
    return image_url


def handle_next_image(sub_stories, index):
    print("starting to handle next image")
    if index < len(sub_stories):
        sub_story = sub_stories[index]
        image_url = generate_image(sub_story)
        index += 1
        return sub_story, image_url, index
    else:
        return "No more texts to process.", None, index


def process_story(story):
    sub_stories = segment_story(story)
    if sub_stories:
        return sub_stories
    else:
        return ["Error in story segmentation"]


def console_test(gender, age, style, triggers):
    personal_prmpt = "Backround: the narrator is a " + gender + ", his age is " + age + "."
    style_prmpt = "In " + style + " style, avoid showing " + triggers
    print(personal_prmpt + " -=PROMPT=- " + style_prmpt)
    personal_wrapper = personal_prmpt
    style_wrapper = style_prmpt



# Create a Gradio interface
with gr.Blocks(theme=theme) as app:
    # states for the ai part
    sub_stories_state = gr.State([])
    image_urls_state = gr.State([])
    index_state = gr.State(0)

    gr.Markdown('<h1 style="font-size:50px; text-align:center; text-shadow: 2px 2px 4px rgba(0,0,0,0.5);">MIND CANVAS</h1>')
    gr.Image("background-image.jpeg", elem_id="background-image")
    with gr.Row(elem_id="overlay"):
        with gr.Column():
            gr.Markdown("<h2>A quick setup and your scene will be ready...</h2>")
            gr.Button("GUIDE", elem_classes="loved_one_button", variant='primary').click(fn=None)
            gr.Button("Privacy Information", elem_id="relative_button").click(fn=None)
            gender = gr.Dropdown(["Male", "Female", "Other"], type="value", label="Gender")
            age = gr.Textbox(lines=1, placeholder="Write a number...", label="Enter your age")
            style = gr.Textbox(lines=1, placeholder="Cartoon / realistic / hand-drawn...", label="Choose a style")
            triggers = gr.Textbox(lines=3, placeholder="Enter what you don't want to see...", label="Triggers")
            gr.Button("Save").click(fn=console_test, inputs=[gender, age, style, triggers])


    with gr.Column():
        gr.Markdown("## Story to Image Sequence Generator")
        gr.Markdown("Enter a complete story and generate a sequence of images representing different parts of the story.")

    with gr.Column():
        story_input = gr.Textbox(lines=10, placeholder="Enter a full story here...", label="Story Input")
        # submit button setup
        submit_button = gr.Button("Parse Story")

        # Text box for wait!
        wait_text = gr.Text(value="Waiting for Parsing...", interactive=False)

        # 1st generate button setup
        generate1_button = gr.Button("Generate Image from Next Text")
        story1_numbering = gr.Textbox(label="Photo Numbering", placeholder="Give this photo a number!", lines=1)
        story1_output = gr.Textbox(label="Generating Text #1", lines=3)
        image1_output = gr.Image(label="Generated Image #1")

        # 2st generate button setup
        generate2_button = gr.Button("Generate Image from Next Text")
        story2_numbering = gr.Textbox(label="Photo Numbering", placeholder="Give this photo a number!", lines=1)
        story2_output = gr.Textbox(label="Generating Text #2", lines=3)
        image2_output = gr.Image(label="Generated Image #2")

        # 3st generate button setup
        generate3_button = gr.Button("Generate Image from Next Text")
        story3_numbering = gr.Textbox(label="Photo Numbering", placeholder="Give this photo a number!", lines=1)
        story3_output = gr.Textbox(label="Generating Text #3", lines=3)
        image3_output = gr.Image(label="Generated Image #3")

        # 4st generate button setup
        generate4_button = gr.Button("Generate Image from Next Text")
        story4_numbering = gr.Textbox(label="Photo Numbering", placeholder="Give this photo a number!", lines=1)
        story4_output = gr.Textbox(label="Generating Text #4", lines=3)
        image4_output = gr.Image(label="Generated Image #4")

        # 5st generate button setup
        generate5_button = gr.Button("Generate Image from Next Text")
        story5_numbering = gr.Textbox(label="Photo Numbering", placeholder="Give this photo a number!", lines=1)
        story5_output = gr.Textbox(label="Generating Text #5", lines=3)
        image5_output = gr.Image(label="Generated Image #5")

        # 6st generate button setup
        generate6_button = gr.Button("Generate Image from Next Text")
        story6_numbering = gr.Textbox(label="Photo Numbering", placeholder="Give this photo a number!", lines=1)
        story6_output = gr.Textbox(label="Generating Text #6", lines=3)
        image6_output = gr.Image(label="Generated Image #6")

        def handle_submit_click(story_input_s):
            sub_stories = segment_story(story_input_s)
            return sub_stories, 0, gr.Text(value="All Done!", interactive=False)

        submit_button.click(fn=handle_submit_click, inputs=story_input, outputs=[sub_stories_state, index_state, wait_text])

        def handle_generate_click(sub_stories, index):
            print("starting to handle generate click")
            sub_story, image_url, new_index = handle_next_image(sub_stories, index)
            # if image_url:
            #    with main_container:
            #        gr.Text(value=sub_story, interactive=False)
            #        gr.Image(value=image_url)
            #        print("tried to print image and text")
            return sub_story, image_url, new_index

        generate1_button.click(fn=handle_generate_click, inputs=[sub_stories_state, index_state],
                               outputs=[story1_output, image1_output, index_state])

        generate2_button.click(fn=handle_generate_click, inputs=[sub_stories_state, index_state],
                               outputs=[story2_output, image2_output, index_state])

        generate3_button.click(fn=handle_generate_click, inputs=[sub_stories_state, index_state],
                               outputs=[story3_output, image3_output, index_state])

        generate4_button.click(fn=handle_generate_click, inputs=[sub_stories_state, index_state],
                               outputs=[story4_output, image4_output, index_state])

        generate5_button.click(fn=handle_generate_click, inputs=[sub_stories_state, index_state],
                               outputs=[story5_output, image5_output, index_state])

        generate6_button.click(fn=handle_generate_click, inputs=[sub_stories_state, index_state],
                               outputs=[story6_output, image6_output, index_state])


if __name__ == "__main__":
    app.launch()
