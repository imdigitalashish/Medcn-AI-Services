


from pydantic_ai import Agent

from pydantic import BaseModel

from dotenv import load_dotenv

load_dotenv()
class SOAPArchitectureReturn(BaseModel):
    subjective: dict
    objective: dict
    assesment: dict
    plan: dict


class AITranscribeService:
    
    def __init__(self):
        
        self.system_prompt = """
        
        You're a doctor, you're task to generate SOAP notes for the given conversation
        The conversation would be the transcription and it would be provided to you in the text format
        Based on the conversation you've to generate the SOAP Notes.
        
        
        """
        self.agent = Agent(
            model="google-gla:gemini-2.5-flash",   
            system_prompt=self.system_prompt,
            output_type=[SOAPArchitectureReturn]
        )
    
    def query(self, query):
        return self.agent.run_sync(user_prompt=query).output
        
        
user_query = """


Doctor: Good morning, Mr. Thompson. How have you been feeling lately?

Patient (Mr. Thompson): Hi Doctor. I've been having some difficulty with my breathing and 
chest pain. It's worse when I exercise or do any kind of physical activity.

Doctor: Have you noticed any other symptoms?

Patient: Yes, my heart rate seems to be a bit higher than usual, and I also have 
experienced some fatigue and dizziness.

Doctor: Alright, let's review your medical history. When did these symptoms start?

Patient: It began about two weeks ago, but it has gradually worsened over time.

Doctor: It sounds like you may be experiencing angina pectoris or a heart attack. I will 
need to conduct an electrocardiogram (ECG) and other tests to confirm this diagnosis. In 
the meantime, avoid any strenuous activities and follow your prescribed medication 
regimen. Please call me if there are any changes in your condition.

Patient: Okay, thank you for your advice, Doctor. I will be sure to get in touch if 
anything worsens.

Doctor: You're welcome, Mr. Thompson. Take care and stay safe.
"""
        
ai_transcribe_service = AITranscribeService()
ai_transcribe_service.query(query=user_query)