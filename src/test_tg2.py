import unittest
from unittest.mock import MagicMock, AsyncMock, patch
import aiohttp


class Test_TG_Bot_2(unittest.IsolatedAsyncioTestCase):
    async def test_start(self):
        update = MagicMock()
        update.effective_user.first_name = 'FirstName'
        update.message.reply_text = AsyncMock()
        context = MagicMock()

    async def test_response_to_gradio(self):
        update = MagicMock()
        update.message.text = 'Text'
        update.message.reply_html = AsyncMock()
        context = MagicMock()
        response = {"data": "Data something", "duration": "Duration something"}

        mock_res = AsyncMock()
        mock_res.json = AsyncMock(return_value=response)
        mock_post = AsyncMock(return_value=mock_res)

if __name__ == '__main__':
    unittest.main()

