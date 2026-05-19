# MediCare AI - Smart Pharmacy & Healthcare Website

A comprehensive AI-powered pharmacy platform built with Streamlit, featuring medicine search, AI chatbot, order tracking, and more.

## 🌟 Features

### Core Services
- **💊 Medicine Database** - Search and compare medicines with detailed information
- **🤖 24/7 AI Chatbot** - Instant health guidance powered by Gemini AI with OpenAI fallback
- **📸 Prescription Upload** - Upload medicine images and get instant information
- **🚚 Order Tracking** - Real-time delivery status with timeline
- **👥 Customer Support** - Contact form and FAQ sections
- **📚 Comprehensive Information** - Uses, side effects, dosages, precautions

### Technical Stack
- **Frontend**: Streamlit (Python web framework)
- **AI/ML**: Google Gemini API (primary), OpenAI API (fallback)
- **Backend**: Python 3.11+
- **Environment**: Python Virtual Environment (venv)
- **Deployment**: Ready for Streamlit Cloud

## 📋 Project Structure

```
Medical-AI-Website/
│
├── app.py                           # Home page with hero section
├── chatbot.py                       # AI chatbot with Gemini & OpenAI
├── .env                            # Environment variables (API keys)
├── requirements.txt                 # Python dependencies
│
└── pages/
    ├── 1_About.py                  # About MediCare AI
    ├── 2_Services.py               # Service offerings
    ├── 3_Medicine_Search.py        # Medicine search & database
    ├── 4_AI_Chatbot.py             # 24/7 AI chatbot
    ├── 5_Order_Tracking.py         # Order tracking
    ├── 6_Contact.py                # Contact form
    ├── 7_FAQ.py                    # Frequently asked questions
    └── 8_Upload_Medicine.py        # Upload & scan medicines
```

## 🚀 Quick Start

### Prerequisites
- Python 3.11 or higher
- pip (Python package manager)
- API keys for:
  - Google Gemini API
  - OpenAI API

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/medical-ai-website.git
cd medical-ai-website
```

2. **Create and activate virtual environment**
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Setup environment variables**
Create a `.env` file in the project root:
```env
GEMINI_API_KEY=your_gemini_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
```

### Get API Keys

**Google Gemini API:**
1. Visit https://ai.google.dev/
2. Click "Get API Key"
3. Create new API key
4. Copy and paste in `.env`

**OpenAI API:**
1. Visit https://platform.openai.com/
2. Sign up or log in
3. Go to API keys section
4. Create new secret key
5. Copy and paste in `.env`

### Run the Application

```bash
streamlit run app.py
```

The application will open at `http://localhost:8501`

## 📖 Usage

### Home Page
- View featured medicine categories
- Check statistics and customer reviews
- Read daily health tips
- Quick access to main features

### Medicine Search
- Search medicines by name
- View uses, side effects, dosages, precautions
- Get alternative medicine suggestions
- Check pricing information

### AI Chatbot
- Chat with AI assistant 24/7
- Ask about medicines, health, symptoms
- Get instant responses
- View chat history

### Prescription Upload
- Upload medicine images
- AI extracts medicine information
- Get detailed medicine details
- Add to cart or chat about medicines

### Order Tracking
- Enter Order ID to track
- Real-time delivery status
- Timeline view
- Contact support options

### Contact
- Submit contact forms
- View office locations
- Get support information
- Follow social media

### FAQ
- Comprehensive Q&A
- Categories: General, Medicine, Ordering, Account, Returns

## 🔑 Environment Variables

```env
# Required
GEMINI_API_KEY=sk-xxxxxxxxxxxxx
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxx
```

## 📦 Dependencies

- **streamlit** (1.28.1) - Web framework
- **google-genai** (0.3.0) - Gemini API client
- **openai** (1.3.0) - OpenAI API client
- **python-dotenv** (1.0.0) - Environment variables
- **Pillow** (10.0.0) - Image processing
- **easyocr** (1.7.1) - OCR for prescription scanning
- **opencv-python** (4.8.1.78) - Computer vision

## 🔐 Security Features

- ✅ Environment variables for sensitive data
- ✅ No hardcoded API keys
- ✅ HTTPS ready
- ✅ Input validation
- ✅ Error handling

## 📱 Responsive Design

- Desktop optimized
- Mobile-friendly UI
- Professional styling
- Accessibility features

## 🌐 Deployment to Streamlit Cloud

### Steps:

1. **Push code to GitHub**
```bash
git add .
git commit -m "Initial commit"
git push origin main
```

2. **Go to Streamlit Cloud**
   - Visit https://share.streamlit.io
   - Sign in with GitHub account

3. **Deploy app**
   - Click "New app"
   - Select repository
   - Select branch (main)
   - Set main file path: `app.py`
   - Click "Deploy"

4. **Add secrets**
   - Go to app settings
   - Add in "Secrets":
   ```
   GEMINI_API_KEY = "your_key_here"
   OPENAI_API_KEY = "your_key_here"
   ```

### Streamlit Cloud URL
Your app will be available at: `https://yourusername-medical-ai-website.streamlit.app`

## 🤖 AI Models Used

### Gemini (Primary)
- Model: `gemini-2.5-flash`
- Fast and efficient
- Good for real-time responses
- Fallback if fails

### OpenAI (Fallback)
- Model: `gpt-4o-mini`
- Used if Gemini fails
- More comprehensive responses
- Ensures uptime

## 📊 Features in Detail

### Medicine Search
- Detailed medicine information
- Uses and applications
- Side effects and precautions
- Dosage recommendations
- Drug interactions
- Alternative suggestions

### AI Chatbot
- Natural language processing
- Context-aware responses
- 24/7 availability
- Multi-topic support
- Chat history

### Order Tracking
- Real-time updates
- Order timeline
- Delivery status
- Contact support
- Reschedule options

### Prescription Upload
- Image upload support
- Automatic text extraction
- Medicine identification
- Detailed information
- Quick ordering

## 🛠️ Development

### Adding New Features

1. Create new page in `pages/` folder
2. Follow naming convention: `[number]_PageName.py`
3. Import `streamlit as st`
4. Use consistent styling

### Modifying Chatbot

Edit `chatbot.py` to:
- Change system prompt
- Add new functions
- Adjust API parameters
- Customize responses

### Styling

Modify CSS in page files or `app.py`:
```python
st.markdown("""
<style>
    /* Your CSS here */
</style>
""", unsafe_allow_html=True)
```

## 🐛 Troubleshooting

### Issue: API Key Not Working
- Verify keys in `.env` file
- Check API key permissions
- Ensure API is enabled in console

### Issue: Streamlit Page Not Loading
- Clear Streamlit cache: Delete `.streamlit/` folder
- Restart Streamlit: `streamlit run app.py`

### Issue: Medicine Search Returns Error
- Check internet connection
- Verify API keys
- Ensure valid medicine name

### Issue: Deployment Failed
- Check GitHub connection
- Verify requirements.txt
- Check secret keys in Streamlit Cloud

## 📞 Support

- **Email**: support@medcare-ai.com
- **Phone**: +1-800-MEDCARE
- **Live Chat**: Available 24/7

## 📄 License

This project is licensed under the MIT License - see LICENSE file for details.

## ⚠️ Disclaimer

This platform provides informational content only and is not a substitute for professional medical advice. Always consult healthcare professionals for medical concerns. In case of medical emergency, contact local emergency services.

## 🎯 Roadmap

- [ ] Mobile app version
- [ ] Video consultation feature
- [ ] Prescription management system
- [ ] Medicine reminders & notifications
- [ ] User accounts & history
- [ ] Payment gateway integration
- [ ] Multi-language support
- [ ] Advanced analytics

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create feature branch
3. Make your changes
4. Submit pull request

## 📝 Version History

- **v1.0.0** - Initial release
  - Core features implemented
  - Multi-page Streamlit app
  - AI chatbot integration
  - Medicine database
  - Order tracking

## ✨ Acknowledgments

- Streamlit for the amazing framework
- Google Gemini for AI capabilities
- OpenAI for robust fallback
- All contributors and users

---

**Built with ❤️ for better healthcare**

© 2024 MediCare AI. All rights reserved.
