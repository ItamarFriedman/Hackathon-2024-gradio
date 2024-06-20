import gradio as gr
from openai import OpenAI

api_key = "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"

openai = OpenAI(api_key=api_key)


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


# Create a Gradio interface
interface = gr.Interface(
    fn=process_story,
    inputs=gr.Textbox(lines=10, placeholder="Enter a full story here..."),
    outputs=[gr.Gallery(label="Generated Images")],
    title="Story to Image Sequence Generator",
    description="Enter a complete story and generate a sequence of images representing different parts of the story."
)

if __name__ == "__main__":
    interface.launch()