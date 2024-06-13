
class Config:
    DEBUG = True
    path1 = "https://www.cincinnatichildrens.org/health/h/heart-components"
    path2 = "https://my.clevelandclinic.org/health/body/21704-heart"
    path3 =  "https://www.hexahealth.com/nagpur/hospitals/cardiology"
    path4 = "https://en.wikipedia.org/wiki/Fever"
    
    
    model = 'google/flan-t5-large'
    # finetuned_peft_model = 'nikhil928/flan-t5-large-fine-tuned-peft_try2'

    # Define additional generation parameters, including temperature
    generation_params = {
        "temperature": 0.5  # Adjust the temperature as needed
    }
