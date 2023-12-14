import unittest
from unittest.mock import MagicMock
from telegram import Update
from telegram.ext import ContextTypes as Context
from pp_one.src.tg import start, response_to_gradio


class Test_TG_Bot(unittest.TestCase):

    def test_start(self):
        update = Update(1, message=MagicMock())
        context = Context()
        self.assertIsNone(start(update, context))
        self.assertTrue(update.message.reply_text.call_args[0][0].startswith('Привет'))

    def test_response_to_gradio(self):
        update = Update(1, message=MagicMock(text='test'))
        context = Context()
        requests = MagicMock()
        requests.post.return_value.json.return_value = {'data': 'test_output', 'duration': 1.23}
        response_to_gradio(update, context)
        update.message.reply_html.assert_called_once_with('test_output \nВремя обработки запроса 1.23')

    def test_start_invalid_update(self):
        update = None
        context = Context()
        self.assertIsNone(start(update, context))

    def test_response_to_gradio_invalid_update(self):
        update = None
        context = Context()
        self.assertIsNone(response_to_gradio(update, context))

    def test_response_to_gradio_invalid_text(self):
        update = Update(1, message=MagicMock(text=None))
        context = Context()
        self.assertIsNone(response_to_gradio(update, context))

    def test_response_to_gradio_invalid_request(self):
        update = Update(1, message=MagicMock(text='test'))
        context = Context()
        requests = MagicMock()
        requests.post.side_effect = Exception('Test error')
        with self.assertLogs() as logs:
            self.assertIsNone(response_to_gradio(update, context))
        self.assertIn('ERROR', logs.output[0])
        self.assertIn('Test error', logs.output[0])


if __name__ == '__main__':
    unittest.main()
