# Waste Impact Analyzer

An AI-powered web application that analyzes waste images to identify waste types, provide environmental impact assessments, and offer eco-friendly recommendations.

![Waste Impact Analyzer](https://via.placeholder.com/800x400?text=Waste+Impact+Analyzer)

## Features

- **Waste Type Identification**: Upload images of waste items and get accurate identification
- **Environmental Impact Analysis**: Detailed metrics on CO₂ emissions, decomposition time, and more
- **Disposal Recommendations**: Learn the proper way to dispose of different waste types
- **Eco-friendly Alternatives**: Discover sustainable alternatives to common waste items
- **Regional Guidelines**: Access disposal guidelines specific to your region

## Technologies Used

- **Backend**: Python Flask
- **AI/ML**: Google Gemini AI for image analysis
- **Frontend**: HTML, CSS, JavaScript
- **Data Visualization**: Chart.js
- **UI Components**: Font Awesome icons

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sojwal000/waste-impact-analyzer.git
   cd waste-impact-analyzer
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
3. Create and activate a virtual environment:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up your Google Gemini API key:
   - Create a .env file in the project root
   - Add your API key:
   ```bash
   GOOGLE_API_KEY=your_api_key_here
   ```
5. Start the Flask development server:
   ```bash
   python app.py
   ```
