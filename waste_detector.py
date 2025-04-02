import google.generativeai as genai
import os
import PIL.Image
import json

# Configure the Gemini API
def configure_genai(api_key):
    genai.configure(api_key=api_key)

def get_api_key():
    """Get API key from environment variable or config file"""
    # Try to get from environment variable first
    api_key = os.environ.get("GEMINI_API_KEY")
    
    # If not found, try to load from config file
    if not api_key:
        config_path = os.path.join(os.path.dirname(__file__), 'config.json')
        if os.path.exists(config_path):
            try:
                with open(config_path, 'r') as f:
                    config = json.load(f)
                    api_key = config.get('gemini_api_key')  # Changed from 'AIzaSyDSxKe836f0p_2C-OleGGMKsUp3pWELWcc'
            except Exception as e:
                print(f"Error loading config file: {e}")
    
    return api_key

def detect_waste(image_path, api_key=None):
    """
    Detect waste type in an image using Gemini API
    
    Args:
        image_path: Path to the uploaded image
        api_key: Optional API key to use instead of environment variable
        
    Returns:
        waste_type: Detected waste type
        confidence: Confidence score
        items: List of specific items detected
    """
    try:
        # Use provided API key or get from environment/config
        if not api_key:
            api_key = get_api_key()
            
        if not api_key:
            raise ValueError("Gemini API key not found. Please provide it as an argument, set the GEMINI_API_KEY environment variable, or add it to config.json")
        
        configure_genai(api_key)
        
        # Load the image
        img = PIL.Image.open(image_path)
        
        # Initialize the Gemini model
        # Using gemini-1.5-flash instead of the deprecated gemini-pro
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Prepare the prompt
        prompt = """
        Analyze this image and identify all types of waste shown.
        First, categorize them into these categories:
        - Plastic
        - Paper
        - Glass
        - Metal
        - Organic
        - Electronic
        - Hazardous
        - Textiles
        - Medical
        - Construction
        - Mixed
        
        Then, identify the specific items present (e.g., plastic bottle, paper cup, glass jar, etc.).
        
        If multiple waste types are present, list all of them with confidence scores and specific items.
        Format: {
            "waste_types": [
                {"type": "category1", "confidence": score1, "items": ["item1", "item2"]}, 
                {"type": "category2", "confidence": score2, "items": ["item3", "item4"]}
            ]
        }
        
        If only one type is present, just return that type with its items.
        Format: {"waste_type": "category", "confidence": score, "items": ["item1", "item2"]}
        """
        
        # Generate response
        response = model.generate_content([prompt, img])
        
        # Parse the response to extract waste type and confidence
        response_text = response.text
        print(f"AI Response: {response_text}")  # For debugging
        
        # Try to parse JSON response
        try:
            import re
            json_str = re.search(r'\{.*\}', response_text, re.DOTALL)
            if json_str:
                import json
                result = json.loads(json_str.group(0))
                
                # Check for multiple waste types
                if "waste_types" in result and isinstance(result["waste_types"], list) and len(result["waste_types"]) > 0:
                    # Return the primary waste type (highest confidence) and its confidence
                    waste_types = sorted(result["waste_types"], key=lambda x: x.get("confidence", 0), reverse=True)
                    primary_type = waste_types[0]["type"]
                    confidence = waste_types[0]["confidence"]
                    items = waste_types[0].get("items", [])
                    return primary_type, confidence, items
                
                # Check for single waste type
                elif "waste_type" in result:
                    waste_type = result["waste_type"]
                    confidence = result.get("confidence", 0.8)
                    items = result.get("items", [])
                    return waste_type, confidence, items
        except Exception as e:
            print(f"Error parsing JSON response: {e}")
        
        # Fall back to simple parsing for single waste type
        if "plastic" in response_text.lower():
            waste_type = "Plastic"
            confidence = 0.85
            items = extract_items(response_text, "plastic")
        elif "paper" in response_text.lower():
            waste_type = "Paper"
            confidence = 0.82
            items = extract_items(response_text, "paper")
        elif "glass" in response_text.lower():
            waste_type = "Glass"
            confidence = 0.88
            items = extract_items(response_text, "glass")
        elif "metal" in response_text.lower():
            waste_type = "Metal"
            confidence = 0.84
            items = extract_items(response_text, "metal")
        elif "organic" in response_text.lower():
            waste_type = "Organic"
            confidence = 0.86
            items = extract_items(response_text, "organic")
        elif "electronic" in response_text.lower():
            waste_type = "Electronic"
            confidence = 0.83
            items = extract_items(response_text, "electronic")
        elif "hazardous" in response_text.lower():
            waste_type = "Hazardous"
            confidence = 0.87
            items = extract_items(response_text, "hazardous")
        elif "textile" in response_text.lower():
            waste_type = "Textiles"
            confidence = 0.81
            items = extract_items(response_text, "textile")
        elif "medical" in response_text.lower():
            waste_type = "Medical"
            confidence = 0.89
            items = extract_items(response_text, "medical")
        elif "construction" in response_text.lower():
            waste_type = "Construction"
            confidence = 0.84
            items = extract_items(response_text, "construction")
        else:
            waste_type = "Mixed"
            confidence = 0.75
            items = extract_items(response_text, "")
            
        return waste_type, confidence, items
        
    except Exception as e:
        print(f"Error in waste detection: {e}")
        return "Unknown", 0.0, []

def extract_items(text, waste_type):
    """Extract specific items from the response text"""
    common_items = {
        "plastic": ["bottle", "bag", "container", "wrapper", "cup", "straw", "pipe", "packaging"],
        "paper": ["cardboard", "newspaper", "magazine", "box", "cup", "bag", "napkin", "tissue"],
        "glass": ["bottle", "jar", "container", "window", "mirror", "light bulb"],
        "metal": ["can", "aluminum", "foil", "container", "cap", "wire", "scrap"],
        "organic": ["food", "vegetable", "fruit", "leaf", "plant", "wood", "coffee grounds"],
        "electronic": ["phone", "computer", "cable", "battery", "charger", "appliance"],
        "hazardous": ["battery", "chemical", "paint", "oil", "solvent", "cleaner"],
        "textile": ["clothing", "fabric", "carpet", "curtain", "towel", "shoe"],
        "medical": ["mask", "glove", "syringe", "bandage", "medicine", "pill bottle"],
        "construction": ["wood", "concrete", "brick", "tile", "pipe", "insulation"]
    }
    
    # Try to find specific items in the text
    found_items = []
    
    # If waste type is specified, check for common items of that type
    if waste_type and waste_type in common_items:
        for item in common_items[waste_type]:
            if item in text.lower():
                found_items.append(f"{waste_type} {item}")
    
    # If no items found or no waste type specified, check all common items
    if not found_items:
        for type_key, items in common_items.items():
            for item in items:
                if item in text.lower() and f"{type_key} {item}" not in found_items:
                    found_items.append(f"{type_key} {item}")
    
    # If still no items found, return a generic item
    if not found_items:
        if waste_type:
            found_items = [f"{waste_type} waste"]
        else:
            found_items = ["Mixed waste"]
    
    return found_items