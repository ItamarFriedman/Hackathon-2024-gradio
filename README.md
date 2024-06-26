<h1> Hackathon-2024-gradio - MIND CANVAS </h1> 

<img src="https://github.com/ItamarFriedman/Hackathon-2024-gradio/assets/102632171/74a0563f-de7c-49ee-9825-d281040ff942" alt="App Screenshot" width="400" style="display:block; margin:auto;"/>


<h2>Table of Contents</h2>
<ol>
    <li><a href="#what-is-mind-canvas">What is MIND CANVAS?</a></li>
    <li><a href="#the-psychology-behind-the-app">The Psychology Behind the App</a></li>
    <li><a href="#the-technical-stuff">The Technical Stuff</a></li>
    <li><a href="#screenshots">Screenshots</a></li>
    <li><a href="#example-of-usage">Example of Usage</a></li>
    <li><a href="#can-i-run-it-myself">Can I Run It Myself?</a></li>
</ol>

<h2 id="what-is-mind-canvas">What is MIND CANVAS?</h2>
MIND CANVAS is an interactive mobile web app designed for therapy sessions. It helps patients visualize past events and organize them chronologically by simply filling in details, telling their story, and receiving a series of photos and texts as a PDF.

<h2 id="the-psychology-behind-the-app">The psychology behind the app</h2>
Effective treatment for individuals with PTSD often involves controlled exposure to their traumatic experiences, often facilitated through art therapy. However, drawing during therapy sessions can be time-consuming and not everyone possesses the necessary skills.
Another challenge is that individuals with PTSD often struggle to organize their traumatic experiences chronologically. This difficulty can perpetuate the recurrence of distressing memories, as they lack a clear narrative endpoint.
Our app is designed to assist in therapy sessions where patients, under therapist supervision, can create a series of images and text descriptions detailing their experiences. This process helps them to reconstruct and order events in a clear chronological and linear manner. By the end of the session, patients receive a physical album documenting their journey. This tangible artifact empowers patients by providing them with a physical representation of their experiences that they can revisit and engage with on their own terms beyond therapy sessions.

<h2 id="the-technical-stuff">The technical stuff</h2>
The web app was developed using the Gradio Python library, leveraging OpenAI's API. During the 24-hour hackathon, we learned to use the library's interface from scratch.

<h2 id="screenshots">Screenshots:</h2>

| <img src="https://github.com/ItamarFriedman/Hackathon-2024-gradio/assets/102632171/30fa301f-7ce1-40a5-8501-e8efe35ecde5" alt="drawing" width="200" style="vertical-align:bottom"/> | <img src="https://github.com/ItamarFriedman/Hackathon-2024-gradio/assets/102632171/5e9c6555-69e0-48f2-870e-532606bd98ba" alt="drawing" width="200" style="vertical-align:bottom"/> | <img src="https://github.com/ItamarFriedman/Hackathon-2024-gradio/assets/102632171/de6029df-9aac-4334-8829-b9d28994c7d6" alt="drawing" width="200" style="vertical-align:bottom"/> | <img src="https://github.com/ItamarFriedman/Hackathon-2024-gradio/assets/102632171/61da802f-2250-4c75-b045-1c7e1b4d1c29" alt="drawing" width="200" style="vertical-align:bottom"/> |
|:------------------------------------:|:----------------------------------:|:------------------------------------:|:------------------------------------:|
| Home Screen                         | Personalization                          | Your story                        | Create the images<br/>and<br/>get a ready for printing PDF                         |


<h2 id="example-of-usage">Example of usage</h2>
1. Open the app and fill in the personalization data:

![app1](https://github.com/ItamarFriedman/Hackathon-2024-gradio/assets/102632171/c0d80c29-79a0-4ae0-833e-e8bd318e3bff)
















2. Fill in your personal story, either as text or using speech-to-text, and parse it into 6 scenes.

![app2](https://github.com/ItamarFriedman/Hackathon-2024-gradio/assets/102632171/023e69c7-4310-436b-8735-cb4cb5450317)
















3. Generate 6 images for the 6 scenes.

![app31big](https://github.com/ItamarFriedman/Hackathon-2024-gradio/assets/102632171/0b65e799-0581-4257-814f-7eefce59a9ef)                                           ![app32big](https://github.com/ItamarFriedman/Hackathon-2024-gradio/assets/102632171/e7cfa06a-b7b7-4b12-ba2f-aae00e7f9151)




















4. Export the final product to a PDF, ready for printing to create a physical album or sharing with others.

![app4big](https://github.com/ItamarFriedman/Hackathon-2024-gradio/assets/102632171/4b19d6f8-6ae3-40ab-8ff3-d96485f7258e)























5. Final exported PDF, ready for printing.

![image](https://github.com/ItamarFriedman/Hackathon-2024-gradio/assets/102632171/bd135845-431b-4055-8d4e-67d316645a86)



<h2 id="can-i-run-it-myself">Can i run it myself?</h2>
You can run MIND CANVAS locally on your machine or use ngrok to tunnel it to a public URL. Note that you'll need to insert a valid OpenAI API key for the app to function.
