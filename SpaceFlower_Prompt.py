import os
import io

# txt 파일을 읽어온다.
def read_list_from_txt(txt_file_path):
    full_path= os.path.dirname(os.path.realpath(__file__)) + "/txt/"+txt_file_path
    with io.open(full_path, mode="r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]

# 한글 , 영어 분리 - 영어 앞 공백제거
def splitPrompt(strAll, splitString, splitCount):
    if ',' in strAll:
        prompt=strAll.split(',', 2)
        prompt = prompt[1].lstrip() +",\n"
    else:
        prompt="" +",\n"
    return prompt

class SpaceFlower_Prompt: 
    def __init__(self):
        pass

    @classmethod    # class 자신 입력
    def INPUT_TYPES(cls):

        txt_filepath1 = "1_그림체_positive.txt"
        긍정문_그림체list = read_list_from_txt(txt_filepath1)

        txt_filepath2 = "1_그림체_negative.txt"
        부정문_그림체list = read_list_from_txt(txt_filepath2)

        txt_filepath3 = "2_캐랙터구도_Compose.txt"
        캐랙터구도list = read_list_from_txt(txt_filepath3)

        txt_filepath4 = "3_얼굴표정.txt"
        얼굴표정list = read_list_from_txt(txt_filepath4)

        txt_filepath5 = "3_헤어.txt"
        헤어list = read_list_from_txt(txt_filepath5)

        txt_filepath6 = "4_체형.txt"
        체형list = read_list_from_txt(txt_filepath6)

        txt_filepath7 = "5_의상.txt"
        의상list = read_list_from_txt(txt_filepath7)

        txt_filepath8 = "6_배경.txt"
        배경list = read_list_from_txt(txt_filepath8)

        txt_filepath9 = "7_악세사리.txt"
        악세사리list = read_list_from_txt(txt_filepath9)        

        txt_filepath10 = "8_동작.txt"
        동작list = read_list_from_txt(txt_filepath10)     

        return {
            # 입력 매개변수
            "required": { 
                "Main_Prompt": ("STRING", {"default": "", "multiline": True}),
                "Positive_그림체": (긍정문_그림체list,),      # txt 파일에서 읽은 리스트 값
                "Negative_그림체": (부정문_그림체list,),
                "Compose_캐랙터구도": (캐랙터구도list,),
                "Facial_얼굴표정": (얼굴표정list,),
                "Hair_헤어": (헤어list,),
                "body_체형": (체형list,),
                "cloth_의상1": (의상list,),
                "cloth_의상2": (의상list,),
                "cloth_의상3": (의상list,),
                "accessory_악세사리1": (악세사리list,),
                "accessory_악세사리2": (악세사리list,),
                "accessory_악세사리3": (악세사리list,),
                "background_배경": (배경list,),
                "motion_동작": (동작list,)
            },
        }

    # 리턴 타입, 이름
    #              전체 합치기 메인프롬프트  P-그림체   N-그림체    구도      얼굴       헤어      체형            의상1-2-3                  악세사리1-2-3,               배경     동작    
    RETURN_TYPES = (  "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING",  "STRING","STRING","STRING",   "STRING","STRING","STRING",  "STRING", "STRING",  )   
    RETURN_NAMES = ("AllConcat_전체연결", "Main_Prompt", "Positive_그림체", "Negative_그림체", "Compose_캐랙터구도", "Facial_얼굴표정", "Hair_헤어",  "body_체형", 
                    "cloth_의상1", "cloth_의상2","cloth_의상3", "accessory_악세사리1", "accessory_악세사리2", "accessory_악세사리3", 
                    "background_배경", "motion_동작" )

    # 호출시 실행함수
    FUNCTION = "do_run"
    CATEGORY = "🌻SpaceFlower"
    
    # 처리 함수
    def do_run(self, Main_Prompt, Positive_그림체, Negative_그림체, Compose_캐랙터구도, Facial_얼굴표정, Hair_헤어, body_체형, 
               cloth_의상1, cloth_의상2, cloth_의상3, accessory_악세사리1, accessory_악세사리2, accessory_악세사리3, background_배경,  motion_동작):
        
        prompt프롬프트=Main_Prompt +",\n"                                      # 이 부분은 그냥 위치로 구분, 추가시 대충 줄맞춰서
        selected_Positive그림체 =Positive_그림체[11:len(Positive_그림체)] +",\n"
        selected_Negative그림체 = Negative_그림체[11:len(Negative_그림체)] +",\n"
        selected_Compose캐랙터구도 = Compose_캐랙터구도[11:len(Compose_캐랙터구도)].lstrip() +",\n"  

        selected_Facial얼굴 = Facial_얼굴표정[11:len(Facial_얼굴표정)].lstrip() +",\n"
        selected_Hair헤어 = Hair_헤어[17:len(Hair_헤어)].lstrip()+",\n"
        selected_body체형 = body_체형[11:len(body_체형)].lstrip()  +",\n"

        selected_cloth의상1=splitPrompt(cloth_의상1, ",", 2)     # txt 파일에 추가시 여기는 , 구분 , 여긴 대충 ,로만 주면 됨
        selected_cloth의상2=splitPrompt(cloth_의상2, ",", 2)
        selected_cloth의상3=splitPrompt(cloth_의상3, ",", 2)

        selected_accessory악세사리1=splitPrompt(accessory_악세사리1, ",", 2)   # txt 파일에 추가시 여기는 , 구분
        selected_accessory악세사리2=splitPrompt(accessory_악세사리2, ",", 2)
        selected_accessory악세사리3=splitPrompt(accessory_악세사리3, ",", 2)

        selected_background배경=splitPrompt(background_배경, ",", 2)        # txt 파일에 추가시 여기는 , 구분
        selected_동작=splitPrompt(motion_동작, ",", 2)

        allConcat_전체연결=prompt프롬프트 + selected_Positive그림체 + selected_Compose캐랙터구도 + selected_Facial얼굴 + selected_Hair헤어 + selected_body체형 + selected_cloth의상1 + selected_cloth의상2 + selected_cloth의상3 + selected_accessory악세사리1 + selected_accessory악세사리2 + selected_accessory악세사리3 + selected_background배경 + selected_동작
        
        
        return ( allConcat_전체연결,                                                                                # All Concat
                prompt프롬프트, 
                selected_Positive그림체, selected_Negative그림체, selected_Compose캐랙터구도,                   # Positive , Negative, Compose
                selected_Facial얼굴, selected_Hair헤어, selected_body체형,                                     # Face, Hair, Body
                selected_cloth의상1, selected_cloth의상2, selected_cloth의상3,                                 # Cloth1-2,3
                selected_accessory악세사리1, selected_accessory악세사리2, selected_accessory악세사리3,          # Accessory1-2-3
                selected_background배경, selected_동작,                                                       # Background, Motion
                )   # 리턴

    
NODE_CLASS_MAPPINGS = {"SpaceFlower_Prompt": SpaceFlower_Prompt,}
NODE_DISPLAY_NAME_MAPPINGS = {"SpaceFlower_Prompt" :"🚀 sf프롬프트 - Prompt",}


