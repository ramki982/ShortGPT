import gradio as gr


import os

from gui.ui_abstract_component import AbstractComponentUI
from gui.asset_components import AssetComponentsUtils

class VideoListUI(AbstractComponentUI):
    def __init__(self, shortGptUI: gr.Blocks):
        self.shortGptUI = shortGptUI
    
    def create_ui(self):
        latest_df = AssetComponentsUtils.getGeneratedVideos()
        embed_height = 300
        embed_width = 300
        asset_link = latest_df.iloc[0]['name']
        print("asset_link:" + asset_link)
        # '''Create the videos UI'''
        with gr.Tab("Videos") as videos_ui:
            with gr.Row():
                    with gr.Column(scale=3):
                        asset_dataframe_ui = gr.Dataframe(latest_df, interactive=False)
                    with gr.Column(scale=2):
                        gr.Markdown("Preview")
                        video_type = 'video/mp4'
                        asset_link = ''
                        current_url = self.shortGptUI.share_url+"/" if self.shortGptUI.share else self.shortGptUI.local_url
                        file_url_path = f"{current_url}file=videos/{asset_link}"
                        # print("current_url: " + current_url)
                        # print("file_url_path: " + file_url_path)
                        embed_html = f'<video width="{embed_width}" height="{embed_height}" style="max-height: 100%;" controls><source src="{file_url_path}" type="{video_type}">Your browser does not support the video tag.</video>'
                        asset_preview_ui = gr.HTML(embed_html)
        return  videos_ui