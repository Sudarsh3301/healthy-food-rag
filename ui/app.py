import os
import sys
import gradio as gr

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)

from retrieval.rag_pipeline import RAGPipeline

# Initialize RAG once
rag = RAGPipeline(top_k=5)

def respond(message, history):
    if not message or not message.strip():
        return ""
    try:
        return rag.generate_answer(message)
    except Exception:
        return "Sorry, something went wrong. Please try again."

def paste_suggestion(text):
    return text

with gr.Blocks() as app:
    gr.HTML("<div id='top-brand'>🥗 Healthy Food Advisor</div>")

    with gr.Column(elem_id="center-content"):
        gr.HTML(
            """
            <div style="text-align:center; margin-top:10vh;">
                <p style="font-size: 1.5rem; font-weight: 600; color: #b388eb;">Fuel Your Body Right</p>
                <h1 style="font-size: 3rem; font-weight: 500; color: white; margin-top: -10px;">Ready to change your life?</h1>
            </div>
            """
        )

        chat_input = gr.Textbox(
            placeholder="Ask about nutritious foods...",
            lines=1,
            container=False,
            elem_id="query-box"
        )

        gr.ChatInterface(
            fn=respond,
            textbox=chat_input,
            title=None,
            description=None
        )

        with gr.Row(elem_id="suggestions-row"):
            s1 = gr.Button("🍎 High-protein snacks", elem_classes="suggestion-btn")
            s2 = gr.Button("🥬 Low-carb dinner", elem_classes="suggestion-btn")
            s3 = gr.Button("⚡ Energy foods", elem_classes="suggestion-btn")

    s1.click(fn=paste_suggestion, inputs=s1, outputs=chat_input)
    s2.click(fn=paste_suggestion, inputs=s2, outputs=chat_input)
    s3.click(fn=paste_suggestion, inputs=s3, outputs=chat_input)

if __name__ == "__main__":
    app.launch(
        css="""
        /* 1. Solid Dark Background */
        .gradio-container {
            background-color: #0f0f0f !important;
            min-height: 100vh !important;
            display: flex !important;
            flex-direction: column;
            align-items: center;
        }

        /* 2. Top-Brand Position */
        #top-brand {
            position: absolute;
            top: 25px;
            left: 25px;
            font-size: 1.2rem;
            font-weight: bold;
            color: white;
        }

        /* 3. Center Scaling */
        #center-content {
            max-width: 850px;
            width: 100%;
            margin: 0 auto;
            background: transparent !important;
        }

        /* 4. Styling the search box */
        #query-box textarea {
            border-radius: 30px !important;
            background: #1e1e1e !important;
            border: 1px solid #333 !important;
            color: white !important;
            padding: 15px 25px !important;
        }

        /* Cleaning up Gradio containers for a seamless look */
        .chatbot, .bubble-wrap, .form, .gr-box {
            background: transparent !important;
            border: none !important;
            box-shadow: none !important;
        }

        /* 5. Suggestions Row Styling */
        #suggestions-row {
            justify-content: center !important;
            gap: 15px;
            margin-top: 15px;
        }

        .suggestion-btn {
            border-radius: 20px !important;
            background: #252525 !important;
            border: 1px solid #333 !important;
            color: #efefef !important;
            width: auto !important;
            padding: 6px 18px !important;
            transition: 0.3s;
        }
        .suggestion-btn:hover {
            background: #333 !important;
        }
        """
    )
