# Deployment Guide for MediCare AI

## Streamlit Cloud Deployment

### Prerequisites
- GitHub account
- Streamlit account (free)
- Repository with code pushed

### Step-by-Step Deployment

#### 1. Prepare Your Repository

```bash
# Ensure all files are committed
git add .
git commit -m "Prepare for deployment"
git push origin main
```

#### 2. Create Streamlit Cloud Account

1. Go to https://share.streamlit.io
2. Sign up with GitHub account
3. Authorize Streamlit to access your repositories

#### 3. Deploy Your App

1. Click "New app" button
2. Select your repository:
   - Choose repository containing the code
   - Select branch: `main` (or your branch)
3. Configure app:
   - Main file path: `app.py`
   - Python version: 3.11 (auto-detected)
4. Click "Deploy" button

#### 4. Add Secrets

After deployment:

1. Click on your app
2. Click menu (3 dots) → Edit secrets
3. Add secrets:

```toml
GEMINI_API_KEY = "your_gemini_key_here"
OPENAI_API_KEY = "your_openai_key_here"
```

4. Save and redeploy

#### 5. Your App is Live!

Your app URL: `https://yourusername-medical-ai-website.streamlit.app`

### Troubleshooting Deployment

#### Issue: "Module not found"
- Ensure `requirements.txt` lists all dependencies
- Check spelling of package names
- Run `pip install -r requirements.txt` locally to verify

#### Issue: "Secret key error"
- Verify keys in Streamlit Cloud secrets
- Ensure keys are valid
- Redeploy after adding secrets

#### Issue: "App crashes on load"
- Check app.py for syntax errors
- Verify all imports are in requirements.txt
- View logs in Streamlit Cloud dashboard

#### Issue: "Pages not showing"
- Ensure page files start with numbers (1_About.py, 2_Services.py, etc.)
- Files must be in `pages/` folder
- Restart app after adding new pages

### Performance Optimization

1. **Cache Results**
```python
import streamlit as st

@st.cache_data
def load_data():
    # Your code here
    pass
```

2. **Lazy Load Images**
```python
st.image("url", use_column_width=True)
```

3. **Limit API Calls**
```python
@st.cache_data(ttl=3600)  # Cache for 1 hour
def get_response(query):
    return get_response(query)
```

### Database Integration (Optional)

For production with persistent storage:

```python
import sqlite3

@st.cache_resource
def get_db_connection():
    conn = sqlite3.connect('data.db')
    return conn

conn = get_db_connection()
cursor = conn.cursor()
```

### Monitoring

1. Check app usage in Streamlit Cloud dashboard
2. Monitor API calls and costs
3. Review logs for errors
4. Track user interactions

### Auto-Deployment

Streamlit Cloud automatically redeploys when you push to GitHub:
1. Make changes locally
2. Commit and push: `git push origin main`
3. Streamlit detects changes
4. Auto-redeploys (takes ~1-2 minutes)

### Custom Domain

1. Go to app settings
2. Click "Custom domain"
3. Enter your domain
4. Follow DNS configuration instructions

### Backup and Restore

```bash
# Clone deployed repo
git clone https://github.com/yourusername/repo.git

# Make local changes
# Push to GitHub
git push origin main

# Streamlit auto-redeploys
```

### Alternative Deployment Options

#### 1. Heroku (with buildpack)
```bash
# Create Procfile
echo "web: streamlit run app.py" > Procfile

# Deploy
git push heroku main
```

#### 2. AWS (using Elastic Beanstalk)
- Configure .ebextensions/
- Deploy via AWS CLI
- Manage auto-scaling

#### 3. Google Cloud Run
```bash
# Build container
gcloud run deploy medical-ai-website --source .
```

#### 4. Docker Deployment
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501
CMD ["streamlit", "run", "app.py"]
```

```bash
# Build
docker build -t medical-ai-website .

# Run
docker run -p 8501:8501 medical-ai-website
```

### Security Best Practices

1. **Never commit secrets**
   - Use .env files (gitignored)
   - Use Streamlit secrets in cloud

2. **Validate user inputs**
```python
if not isinstance(user_input, str):
    st.error("Invalid input")
```

3. **Rate limiting**
```python
import time
last_request = st.session_state.get("last_request", 0)
if time.time() - last_request < 1:
    st.error("Please wait before making another request")
```

4. **HTTPS enforcement**
- Streamlit Cloud uses HTTPS by default
- Enable redirect if using custom domain

### Cost Optimization

**Streamlit Cloud Pricing:**
- Free: Community tier
- Pro: $24/month per app
- Teams: Custom pricing

**API Costs:**
- Gemini: Pay as you go ($1-5 per million tokens)
- OpenAI: Pay per request ($0.0005-0.015 per 1K tokens)

**Tips:**
- Use caching to reduce API calls
- Implement rate limiting
- Monitor usage regularly

### Maintenance

1. **Weekly**
   - Check error logs
   - Monitor performance

2. **Monthly**
   - Update dependencies: `pip install --upgrade -r requirements.txt`
   - Review API costs
   - Check for security updates

3. **Quarterly**
   - Audit code for improvements
   - Update documentation
   - Plan new features

### Support & Resources

- **Streamlit Docs**: https://docs.streamlit.io
- **Community Forum**: https://discuss.streamlit.io
- **GitHub Issues**: Report bugs and request features
- **Email Support**: contact@medcare-ai.com

---

**Deployed with ❤️ using Streamlit Cloud**
