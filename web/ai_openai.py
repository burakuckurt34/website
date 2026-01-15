'''
Created on 3 Oca 2026

@author: burak
'''
import keyring 
from openai import OpenAI

ID_TYPE = "AI_OPENAI"
USERNAME = "OPENAI_API_KEY"


def _get_api_key() -> str:
    api_key = keyring.get_password(ID_TYPE, USERNAME)
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY keyring'de bulunamadı (AI_OPENAI / OPENAI_API_KEY).")
    return api_key


_client = OpenAI(
    api_key=_get_api_key(),
    timeout=15,
    max_retries=1,
)


def chat_once(user_text: str, previous_response_id: str | None = None, model: str = "gpt-4o") -> tuple[str, str]:
    """
    Minimal chat:
      - İlk mesajda previous_response_id yok
      - Sonraki mesajlarda previous_response_id ile konuşmayı sürdürür

    Dönen: (assistant_text, new_response_id)
    """
    kwargs = {}
    if previous_response_id:
        # Responses API: çok turlu konuşma için zincirleme yöntem
        kwargs["previous_response_id"] = previous_response_id

    resp = _client.responses.create(
        model=model,
        input=user_text,
        **kwargs,
    )

    return resp.output_text, resp.id
