# AI Event Banner Generator

An interactive Flask app that uses Google’s Gem​ini image‐generation API to create event banners based on user prompts. Users can generate new banners, set an aspect ratio, and view a history of previously generated images.

---

## Project Overview

This project provides a simple web interface to generate AI‐driven event banners. Users supply a text prompt (e.g., “Luxury Tech Conference 2025: Innovating the Future – April 10th, New York City”) and select an aspect ratio. The backend calls Google’s Gemini model to produce an image, which is returned as a Base64‐encoded JPEG. All generated images are stored in memory and can be retrieved via a “History” tab.

Key components:
- **Flask** for routing and templating  
- **Gemini GenAI client** for image generation  
- **Pillow (PIL)** for image processing (converting Raw bytes → JPEG → Base64)  
- **Vanilla JavaScript + Tailwind CSS** for a modern, responsive UI  

---

## Prerequisites

1. **Python 3.8+**  
2. **pip** (or `pip3`) installed  
3. A valid **Google Gemini (GenAI) API key**  
4. (Optional) `virtualenv` or `venv` for creating isolated environments  

---


