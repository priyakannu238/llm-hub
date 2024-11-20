import gradio as gr

class UIComponents:
    @staticmethod
    def create_model_info_display():
        """
        Create a component to display selected model's information
        """
        with gr.Accordion("Model Information", open=False):
            model_info = gr.Markdown(
                """
                ### Model Details
                - **Name**: 
                - **Context Length**: 
                - **Capabilities**: 
                """
            )
        return model_info

    @staticmethod
    def create_chat_settings():
        """
        Create advanced chat settings components
        """
        with gr.Accordion("Advanced Settings", open=False):
            temperature = gr.Slider(
                minimum=0.0, 
                maximum=1.0, 
                value=0.7, 
                step=0.1, 
                label="Temperature"
            )
            max_tokens = gr.Slider(
                minimum=50, 
                maximum=4096, 
                value=1024, 
                step=50, 
                label="Max Response Tokens"
            )
            top_p = gr.Slider(
                minimum=0.0, 
                maximum=1.0, 
                value=0.9, 
                step=0.1, 
                label="Top P"
            )
        return temperature, max_tokens, top_p

    @staticmethod
    def create_conversation_controls():
        """
        Create conversation control buttons
        """
        with gr.Row():
            clear_btn = gr.Button("Clear Conversation")
            save_btn = gr.Button("Save Conversation")
        return clear_btn, save_btn

    @staticmethod
    def create_token_counter():
        """
        Create a token usage display
        """
        token_display = gr.Textbox(
            label="Token Usage", 
            interactive=False
        )
        return token_display