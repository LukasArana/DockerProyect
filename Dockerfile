# Python 2.7 oinarri ofizial batetik abiatuko gara
FROM python:3.9.12-slim
# kontainerra hasten denean, bere lan direktorioa honakoa izango da
WORKDIR /app
# Gure proiektuko fitxategi guztiak kontainerraren /app direktoriora kopiatukoditugu:
# Uneko direktorioan dauzkagun fitxategiak kopiatuko dira, app.py eta requirements.txt
COPY . /app
# pip erabiliz, “requirements.txt” dauden menpekotasunak instalatuko ditugu.
RUN pip install --trusted-host pypi.python.org -r requirements.txt
# Kontainerra 80/tcp portutik komunikatuko dela adierazten dugu
EXPOSE 5000
# Ingurune aldagai bat sortuko dugu
ENV NAME World
# Kontainerra jaurtitzerakoan, honako komandoa exekutatuko da
CMD ["python", "app.py"]
