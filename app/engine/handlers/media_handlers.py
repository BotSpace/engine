# app/engine/handlers/media_handlers.py
from typing import Dict, Any
from .base import ActionHandler

class SendPhotoHandler(ActionHandler):
    """SendPhotoNode'ni bajarish uchun mas'ul."""
    async def handle(self, data: Dict[str, Any], chat_id: int, context: Dict[str, Any]):
        source_type = data.get('photoSourceType', 'url')
        photo_id = data.get('photoFileId') if source_type == 'file_id' else data.get('photoUrl')
        
        if not photo_id:
            self.logger.error(f"Node data'da 'photoFileId' yoki 'photoUrl' topilmadi: {data}")
            return
            
        params = self._prepare_common_params(data)
        if data.get('caption'):
            params['caption'] = data.get('caption')
            
        recipient_ids = self._get_recipients(data, chat_id)
        for recipient_id in recipient_ids:
            try:
                await self.bot.send_photo(chat_id=recipient_id, photo=photo_id, **params)
            except Exception as e:
                self.logger.error(f"Rasm yuborishda xatolik (chat_id: {recipient_id}): {e}")

class SendVideoHandler(ActionHandler):
    """SendVideoNode'ni bajarish uchun mas'ul."""
    async def handle(self, data: Dict[str, Any], chat_id: int, context: Dict[str, Any]):
        source_type = data.get('videoSourceType', 'url')
        video_id = data.get('videoFileId') if source_type == 'file_id' else data.get('videoUrl')

        if not video_id:
            self.logger.error(f"Node data'da 'videoFileId' yoki 'videoUrl' topilmadi: {data}")
            return

        params = self._prepare_common_params(data)
        if data.get('caption'): params['caption'] = data.get('caption')
        if data.get('width'): params['width'] = int(data['width'])
        if data.get('height'): params['height'] = int(data['height'])
        if data.get('duration'): params['duration'] = int(data['duration'])
        if data.get('supportsStreaming'): params['supports_streaming'] = True
        
        recipient_ids = self._get_recipients(data, chat_id)
        for recipient_id in recipient_ids:
            try:
                await self.bot.send_video(chat_id=recipient_id, video=video_id, **params)
            except Exception as e:
                self.logger.error(f"Video yuborishda xatolik (chat_id: {recipient_id}): {e}")

class SendAudioHandler(ActionHandler):
    """SendAudioNode'ni bajarish uchun mas'ul."""
    async def handle(self, data: Dict[str, Any], chat_id: int, context: Dict[str, Any]):
        source_type = data.get('audioSourceType', 'url')
        audio_id = data.get('audioFileId') if source_type == 'file_id' else data.get('audioUrl')

        if not audio_id:
            self.logger.error(f"Node data'da 'audioFileId' yoki 'audioUrl' topilmadi: {data}")
            return

        params = self._prepare_common_params(data)
        if data.get('caption'): params['caption'] = data.get('caption')
        if data.get('performer'): params['performer'] = data.get('performer')
        if data.get('title'): params['title'] = data.get('title')
        if data.get('duration'): params['duration'] = int(data['duration'])
        
        recipient_ids = self._get_recipients(data, chat_id)
        for recipient_id in recipient_ids:
            try:
                await self.bot.send_audio(chat_id=recipient_id, audio=audio_id, **params)
            except Exception as e:
                self.logger.error(f"Audio yuborishda xatolik (chat_id: {recipient_id}): {e}")

class SendFileHandler(ActionHandler):
    """SendFileNode'ni (document) bajarish uchun mas'ul."""
    async def handle(self, data: Dict[str, Any], chat_id: int, context: Dict[str, Any]):
        source_type = data.get('fileSourceType', 'url')
        file_id = data.get('fileId') if source_type == 'file_id' else data.get('fileUrl')

        if not file_id:
            self.logger.error(f"Node data'da 'fileId' yoki 'fileUrl' topilmadi: {data}")
            return

        params = self._prepare_common_params(data)
        if data.get('caption'): params['caption'] = data.get('caption')
        
        recipient_ids = self._get_recipients(data, chat_id)
        for recipient_id in recipient_ids:
            try:
                await self.bot.send_document(chat_id=recipient_id, document=file_id, **params)
            except Exception as e:
                self.logger.error(f"Fayl yuborishda xatolik (chat_id: {recipient_id}): {e}")