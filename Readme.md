# 🤖 AI Blog Writer

An intelligent AI-powered blog writing assistant that generates comprehensive, well-researched blog posts on any topic with just one click. Built with modern AI technology and a beautiful React frontend.

![AI Blog Writer](https://img.shields.io/badge/AI-Blog%20Writer-blue?style=for-the-badge&logo=robot)
![Python](https://img.shields.io/badge/Python-3.8+-green?style=for-the-badge&logo=python)
![React](https://img.shields.io/badge/React-18.2.0-blue?style=for-the-badge&logo=react)
![FastAPI](https://img.shields.io/badge/FastAPI-0.116.1-green?style=for-the-badge&logo=fastapi)

## ✨ Features

- **🎯 One-Click Blog Generation** - Generate complete blog posts with just a topic
- **🔍 Comprehensive Research** - AI-powered research using multiple authoritative sources
- **📝 SEO-Optimized Content** - Engaging, structured content with proper formatting
- **💡 Practical Insights** - Includes pro tips, best practices, and actionable advice
- **📊 Data-Driven Analysis** - Incorporates statistics, expert quotes, and case studies
- **🎨 Beautiful UI** - Modern, responsive React frontend with real-time streaming
- **⚡ Real-Time Generation** - Watch your blog post being written live
- **📱 Mobile-Friendly** - Responsive design that works on all devices

## 🚀 Demo

Simply enter any topic and watch as the AI creates a comprehensive blog post with:
- Engaging headlines and introductions
- Detailed research and analysis
- Practical applications and examples
- Pro tips and best practices
- Expert insights and quotes
- FAQ sections
- Future outlook and predictions

## 🛠️ Technology Stack

### Backend
- **Python 3.8+** - Core programming language
- **FastAPI** - High-performance web framework
- **Agno** - AI agent framework for intelligent content generation
- **Groq** - LLM provider (Llama 4 Maverick 17B)
- **DuckDuckGo Tools** - Web search capabilities
- **Newspaper4k** - Article extraction and processing

### Frontend
- **React 18.2.0** - Modern UI framework
- **React Markdown** - Markdown rendering
- **CSS Modules** - Styled components
- **Real-time Streaming** - Live content generation

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- Node.js 16 or higher
- Groq API key

### Backend Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Salman313ali/AI-Blog-Writer.git
   cd ai-blog-writer
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

5. **Run the backend server**
   ```bash
   python main.py
   ```
   The API will be available at `http://localhost:8000`

### Frontend Setup

1. **Navigate to frontend directory**
   ```bash
   cd frontend
   ```

2. **Install Node.js dependencies**
   ```bash
   npm install
   ```

3. **Start the React development server**
   ```bash
   npm start
   ```
   The frontend will be available at `http://localhost:3000`

## 🎯 Usage

1. **Open the application** in your browser at `http://localhost:3000`
2. **Enter your blog topic** in the input field
3. **Click "Generate Blog"** and watch the AI create your content
4. **View the complete blog post** with all sections and formatting

### Example Topics
- "Artificial Intelligence in Healthcare"
- "Sustainable Business Practices"
- "Digital Marketing Trends 2024"
- "Remote Work Best Practices"
- "Cybersecurity for Small Businesses"

## 📁 Project Structure

```
ai-blog-writer/
├── Blog_post_agent.py    # AI agent configuration
├── main.py              # FastAPI backend server
├── requirements.txt      # Python dependencies
├── .env                 # Environment variables
├── frontend/            # React frontend
│   ├── src/
│   │   ├── App.js       # Main React component
│   │   ├── App.module.css # Styling
│   │   ├── BlogMarkdown.js # Markdown renderer
│   │   └── AgentSteps.js   # Progress indicators
│   ├── package.json     # Node.js dependencies
│   └── public/          # Static assets
└── README.md           # This file
```

## 🔧 API Endpoints

### POST `/generate-blog`
Generates a blog post based on the provided topic.

**Request Body:**
```json
{
  "topic": "Your blog topic here"
}
```

**Response:** Streaming text content of the generated blog post.

## 🤖 AI Agent Features

The AI agent is configured with comprehensive capabilities:

- **Research Phase** - Gathers 8-12 authoritative sources
- **Content Planning** - Creates engaging headlines and structure
- **Writing Phase** - Generates conversational, informative content
- **Enhancement Phase** - Adds links, CTAs, and optimizations

### Content Structure
- Engaging headline and introduction
- Understanding the topic with context
- Key insights and analysis
- Practical applications and examples
- Pro tips and best practices
- Expert insights and quotes
- FAQ section
- Future outlook
- Conclusion with takeaways

## 🚀 Deployment

### Backend Deployment
```bash
# Install production dependencies
pip install gunicorn uvicorn

# Run with Gunicorn
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker
```

### Frontend Deployment
```bash
cd frontend
npm run build
# Deploy the build folder to your hosting service
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Agno](https://github.com/agno-ai/agno) - AI agent framework
- [Groq](https://groq.com/) - LLM provider
- [React](https://reactjs.org/) - Frontend framework
- [FastAPI](https://fastapi.tiangolo.com/) - Backend framework

## 📞 Support

If you have any questions or need help, please open an issue on GitHub or contact me at [salman313ali@gmail.com].

---

