<h2>Setup guide 🚀</h2><br>


**1. Create and activate  virtual environment  📦**
```shell
python3 -m venv venv
source venv/bin/activate
```
<br>

**2. Install dependencies 📥**
```shell
pip install -r requirements.txt
```
<br>

**3. Setup Environment Variables ⚙️ <br>**
_Create `.env` file in the root directory and add:_
```env
DATABASE_URL=postgresql://<your_pg_username>:<your_pg_password>@<your_pg_ip_or_host>:5432/baybol_bot_db
TELEGRAM_TOKEN=<your_bot_token>
WEBHOOK_URL=https://<your_host>/webhook
```
<br>

**4. Start the FastAPI Server  🌐**
```shell
uvicorn main:app --reload
```
<br>


<h3>Extra steps for testing purpose 🧪</h3><br>

**1. Run PostgreSQL with Docker  🐘**
```shell
docker compose -f Docker/docker-compose.yml up -d
```
<br>

**2. Run Ngrok for Webhook**
```shell
ngrok http 8000
```
_Copy the generated HTTPS URL and update the WEBHOOK_URL in .env accordingly_




