import firebase_admin
from firebase_admin import credentials, firestore, storage
import os

cred = credentials.Certificate(os.getcwd()+'/sieren/export'+"/sieren-8710b-firebase-adminsdk-m67jr-8f7de5846b.json")
firebase_admin.initialize_app(cred, {
    'storageBucket': 'sieren-8710b.appspot.com'
})

db = firestore.client()
bucket = storage.bucket()


def check_file_exist(file_name):
    files_ref = db.collection("excel files")
    docs = files_ref.stream()
  
    for doc in docs:
        object = doc.to_dict()
        if(object["fileName"] == file_name):
            return True
    return False



def alternative_flow(file_name):
    destination_path = os.path.join(os.getcwd(), 'container', file_name)
    os.makedirs(os.getcwd()+'\container', exist_ok=True)
    
    blob_path = "gs://sieren-8710b.appspot.com/" + file_name
    blob = bucket.blob(blob_path)

    if not blob.exists():
        print('\nFile does not exist already. We have to fetch data from server!!')
        print('should we start the scraping loop..🔥?? (yes/no)')
        user_input = input().lower()
        process_stop = ['no', 'n', 'f', 'false']
        if user_input in process_stop:
            return True
        print("Okay... Let's begin. 🏃‍♀️🏃‍♂️💨")
        return False
        
    print("File exists on fire-base-server")
    
    blob.download_to_filename(destination_path)
    print("File download completed.")
    
    return True



def file_uploading(file_path):
    print("File is being uploading... to fire-base-server")
    
    file_name=file_path.split("\\")[-1]
    blob = bucket.blob("gs://sieren-8710b.appspot.com/" + file_name)
    blob.upload_from_filename(file_path)
    
    print("File upload completed.")
