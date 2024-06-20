import gradio as gr
from openai import OpenAI
from fpdf import FPDF

api_key = "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"

openai = OpenAI(api_key=api_key)

theme = gr.themes.Base(
    primary_hue="purple",
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

def create_pdf(image_urls):
    if not image_urls:
        return "No image URLs provided."

    pdf = FPDF()
    pdf.add_page()
    x_position = 10
    y_position = 10
    image_width = 180
    y_increment = 60

    try:
        for url in image_urls:
            pdf.image(url, x=x_position, y=y_position, w=image_width)
            y_position += y_increment
    except Exception as e:
        return f"Failed to add images to PDF: {str(e)}"

    pdf_filename = "Generated_Images.pdf"
    try:
        pdf.output(pdf_filename)
    except Exception as e:
        return f"Failed to save PDF: {str(e)}"

    return pdf_filename


# Create a Gradio interface
with gr.Blocks(theme=theme) as app:
    gr.Markdown("## MIND CANVAS")
    gr.Image("background-image.jpeg", elem_id="background-image")
    with gr.Row(elem_id="overlay"):
        with gr.Column():
            gr.Markdown("<h2>How to support your loved one with PTSD?</h2>")
            gr.Button("Continue as a loved one", elem_classes="loved_one_button").click(fn=None)
            gr.Button("Continue as a relative", elem_id="relative_button").click(fn=None)
    gr.Markdown("## Story to Image Sequence Generator")
    gr.Markdown("Enter a complete story and generate a sequence of images representing different parts of the story.")

    with gr.Column():
        story_input = gr.Textbox(lines=10, placeholder="Enter a full story here...", label="Story Input")
        submit_button = gr.Button("Generate Images")
        output_gallery = gr.Gallery(label="Generated Images")
        pdf_button = gr.Button("Export as PDF")
        output_label = gr.Label()
        pdf_button.click(fn=create_pdf, inputs=[output_gallery], outputs=output_label)

    submit_button.click(fn=process_story, inputs=story_input, outputs=output_gallery)

if __name__ == "__main__":
    app.launch()