# 2024CareerHack

本地端建立連線:
1. 如果要在本地端執行程式，請先安裝 Google cloud SDK: https://cloud.google.com/sdk/docs/install
2. 安裝完成後執行指令登入: gcolud auth application-default-login，會開啟瀏覽器，選擇要登入的帳號
3. 執行指令，選定要使用的專案 ID
```
gcloud auth application-default login
gcloud auth application-default set-quota-project <PROJECT_ID>
```

本地環境建立:
1. 建立 virtual env，並在虛擬環境中安裝 google-cloud-aiplatform
   ```
   pip install virtualenv
   python -m virtualenv <環境名稱>
   <環境名稱>/Scripts: activate
   <環境名稱>/Scripts: pip install google-cloud-aiplatform pandas tabulate
   
   ```
3. 將範例程式放到本地端，並使用剛剛建立的虛擬環境執行程式

[參考文獻]
1. vertex ai PaLM2: https://cloud.google.com/vertex-ai/docs/generative-ai/model-reference/text
