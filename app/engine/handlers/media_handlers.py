# app/engine/executors/media_handlers.py
from typing import Dict, Any
from .base import ActionHandler

class SendPhotoHandler(ActionHandler):
    """SendPhotoNode'ni bajarish uchun mas'ul."""

    async def handle(self, data: Dict[str, Any], chat_id: int):
        source_type = data.get('photoSourceType', 'url')
        photo_id = data.get('photoFileId' if source_type == 'file_id' else 'photoUrl')
        
        if not photo_id:
            self.logger.error(f"Node data'da 'photoFileId' yoki 'photoUrl' topilmadi. Ma'lumot: {data}")
            return
            
        params = self._prepare_common_params(data)
        
        caption = data.get('caption')
        if caption:
            params['caption'] = caption
            
        await self.bot.send_photo(
            chat_id=chat_id,
            photo=photo_id,
            **params
        )


class SendVideoHandler(ActionHandler):
    """SendVideoNode'ni bajarish uchun mas'ul."""

    async def handle(self, data: Dict[str, Any], chat_id: int):
        source_type = data.get('videoSourceType', 'url')
        video_id = data.get('videoFileId' if source_type == 'file_id' else 'videoUrl')

        if not video_id:
            self.logger.error(f"Node data'da 'videoFileId' yoki 'videoUrl' topilmadi. Ma'lumot: {data}")
            return

        params = self._prepare_common_params(data)
        
        # Videoga xos parametrlarni qo'shamiz
        if data.get('caption'): params['caption'] = data.get('caption')
        if data.get('width'): params['width'] = int(data['width'])
        if data.get('height'): params['height'] = int(data['height'])
        if data.get('duration'): params['duration'] = int(data['duration'])
        if data.get('supportsStreaming'): params['supports_streaming'] = True
        
        await self.bot.send_video(
            chat_id=chat_id,
            video=video_id,
            **params
        )

# Xuddi shu tarzda SendAudioHandler va SendFileHandler ham yoziladi...
class SendAudioHandler(ActionHandler):
    """SendAudioNode'ni bajarish uchun mas'ul."""
    async def handle(self, data: Dict[str, Any], chat_id: int):
        # ... Audio uchun logikani implementatsiya qilish ...
        pass

class SendFileHandler(ActionHandler):
    """SendFileNode'ni bajarish uchun mas'ul."""
    async def handle(self, data: Dict[str, Any], chat_id: int):
        # ... Fayl (document) uchun logikani implementatsiya qilish ...
        pass