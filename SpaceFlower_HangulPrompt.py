from googletrans import Translator

def translate_korean_to_english(text):
    translator = Translator()
    result = translator.translate(text, src='ko', dest='en')
    return result.text

class SpaceFlower_HangulPrompt:
    
    def __init__(self):
        pass
   
    @classmethod
    def INPUT_TYPES(self):        
        return {"required": {
                "positiveText": ("STRING", {"default": "긍정문을 입력하시오", "multiline": True}),
                "negativeText": ("STRING", {"default": "부정문을 입력하시오 ", "multiline": True}),
                },
        }
        
    RETURN_TYPES =("STRING", "STRING")
    RETURN_NAMES = ("positive_english_text", "negative_english_text")
    FUNCTION = "do_run"
    CATEGORY = "🌻SpaceFlower"

    def do_run(self, positiveText, negativeText):

        english_translationP=""
        english_translationN=""

        if positiveText !="":
            english_translationP = translate_korean_to_english(positiveText)
        if negativeText !="":
            english_translationN = translate_korean_to_english(negativeText)

        return ( english_translationP, english_translationN)

NODE_CLASS_MAPPINGS = {"SpaceFlower_HangulPrompt": SpaceFlower_HangulPrompt}
NODE_DISPLAY_NAME_MAPPINGS = {"SpaceFlower_HangulPrompt": "🌍 sf한글 프롬프트- Hangul_Prompt"}

# 사용전에 설치
# D:\ai\Data\Packages\ComfyUI\venv\Scripts\activate.bat 
# venv > pip install --upgrade googletrans==4.0.0-rc1
# deactivate

# 구글 번역 python 라이브러리 패키지를 ---> comfyui 가상환경 안에 설치 해야 작동함

