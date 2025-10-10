# app/engine/handlers/media_handlers.py
from typing import Dict, Any
from .base import ActionHandler

class SendPhotoHandler(ActionHandler):
    async def handle(self, data: Dict[str, Any], chat_id: int, context: Dict[str, Any]):
        source_type = data.get('photoSourceType', 'url')
        photo_id = data.get('photoFileId') if source_type == 'file_id' else data.get('photoUrl')
        if not photo_id: self.logger.error(f"Node data'da 'photoFileId' yoki 'photoUrl' topilmadi: {data}"); return
        params = self._prepare_common_params(data)
        if data.get('caption'): params['caption'] = data.get('caption')
        for recipient_id in self._get_recipients(data, chat_id):
            try: await self.bot.send_photo(chat_id=recipient_id, photo=photo_id, **params)
            except Exception as e: self.logger.error(f"Rasm yuborishda xatolik (chat_id: {recipient_id}): {e}")

class SendVideoHandler(ActionHandler):
    async def handle(self, data: Dict[str, Any], chat_id: int, context: Dict[str, Any]):
        source_type = data.get('videoSourceType', 'url')
        video_id = data.get('videoFileId') if source_type == 'file_id' else data.get('videoUrl')
        if not video_id: self.logger.error(f"Node data'da 'videoFileId' yoki 'videoUrl' topilmadi: {data}"); return
        params = self._prepare_common_params(data)
        if data.get('caption'): params['caption'] = data.get('caption')
        # ...boshqa video parametrlari...
        for recipient_id in self._get_recipients(data, chat_id):
            try: await self.bot.send_video(chat_id=recipient_id, video=video_id, **params)
            except Exception as e: self.logger.error(f"Video yuborishda xatolik (chat_id: {recipient_id}): {e}")

class SendAudioHandler(ActionHandler):
    async def handle(self, data: Dict[str, Any], chat_id: int, context: Dict[str, Any]):
        source_type = data.get('audioSourceType', 'url')
        audio_id = data.get('audioFileId') if source_type == 'file_id' else data.get('audioUrl')
        if not audio_id: self.logger.error(f"Node data'da 'audioFileId' yoki 'audioUrl' topilmadi: {data}"); return
        params = self._prepare_common_params(data)
        # ...boshqa audio parametrlari...
        for recipient_id in self._get_recipients(data, chat_id):
            try: await self.bot.send_audio(chat_id=recipient_id, audio=audio_id, **params)
            except Exception as e: self.logger.error(f"Audio yuborishda xatolik (chat_id: {recipient_id}): {e}")

class SendFileHandler(ActionHandler):
    async def handle(self, data: Dict[str, Any], chat_id: int, context: Dict[str, Any]):
        source_type = data.get('fileSourceType', 'url')
        file_id = data.get('fileId') if source_type == 'file_id' else data.get('fileUrl')
        if not file_id: self.logger.error(f"Node data'da 'fileId' yoki 'fileUrl' topilmadi: {data}"); return
        params = self._prepare_common_params(data)
        if data.get('caption'): params['caption'] = data.get('caption')
        for recipient_id in self._get_recipients(data, chat_id):
            try: await self.bot.send_document(chat_id=recipient_id, document=file_id, **params)
            except Exception as e: self.logger.error(f"Fayl yuborishda xatolik (chat_id: {recipient_id}): {e}")