import gradio as gr


# Define the functions for the buttons
def continue_as_loved_one():
    return "You selected: Continue as a loved one"


def continue_as_relative():
    return "You selected: Continue as a relative"


def continue_as_therapist():
    return "You selected: Continue as a therapist"


# Define the Gradio interface
with gr.Blocks(css='styles.css') as demo:
    with gr.Column():
        # Background image section
        gr.Image("background-image.jpeg", elem_id="background-image")

        # Overlay section
        with gr.Row(elem_id="overlay"):

            with gr.Column():
                gr.Markdown("<h2>How to support your loved one with PTSD?</h2>")
                gr.Button("Continue as a loved one", elem_id="loved_one_button").click(fn=continue_as_loved_one)
                gr.Button("Continue as a relative", elem_id="relative_button").click(fn=continue_as_relative)
                gr.Button("Continue as a therapist", elem_id="therapist_button").click(fn=continue_as_therapist)

demo.launch()