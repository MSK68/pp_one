import unittest
from unittest.mock import MagicMock, AsyncMock, patch
from pp_one.src.tg import start, response_to_gradio, requests
import aiohttp


class TestBotFunctions(unittest.IsolatedAsyncioTestCase):
    async def test_start(self):
        update = MagicMock()
        update.effective_user.first_name = 'TestUser'
        update.message.reply_text = AsyncMock()
        context = MagicMock()
        await start(update, context)

    async def test_response_to_gradio(self):
        update = MagicMock()
        update.message.text = 'Test message'
        update.message.reply_html = AsyncMock()
        context = MagicMock()
        response = {"data": "Test data", "duration": "Test duration"}

        mock_resp = AsyncMock()
        mock_resp.json = AsyncMock(return_value=response)
        mock_post = AsyncMock(return_value=mock_resp)

        with patch('aiohttp.ClientSession.post', new=AsyncMock(return_value=mock_resp)):
            await response_to_gradio(update, context)

if __name__ == '__main__':
    unittest.main()

