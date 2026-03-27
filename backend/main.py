from flask import Flask, request, jsonify
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)  # Allow frontend to communicate with backend

# --- TOPICS DEMONSTRATED ---
# 1. VARIABLES (request_count, is_running, server_name)
# 2. DATATYPES (Integer, Boolean, String, Float returned by time.time())
# 3. DATA STRUCTURES (List, Dictionary)
# 4. FLOW CONTROLS (if/else, for loops)

request_count = 0        # Integer
is_running = True        # Boolean
server_name = "Anti-gravity Python Engine"  # String

# 3. DATA STRUCTURES
prompt_history = []      # List
ai_models = {            # Dictionary
    "legacy": "ChatGPT",
    "modern": "Gemini",
    "features": ["multimodal", "fast", "efficient"]
}

@app.route('/api/status', methods=['GET'])
def get_status():
    global request_count
    
    # 4. FLOW CONTROLS (if/else condition)
    if is_running:
        request_count += 1
        return jsonify({
            "message": f"{server_name} is online!",
            "requests": request_count,
            "models": ai_models
        })
    else:
        return jsonify({"error": "Service unavailable"}), 503

@app.route('/api/migrate-prompt', methods=['POST'])
def migrate_prompt():
    global request_count
    data = request.get_json()
    prompt = data.get('prompt', '')
    
    request_count += 1
    
    # 4. FLOW CONTROLS (if condition)
    if not prompt:
        return jsonify({"error": "Please provide a prompt to migrate!"}), 400
        
    # 3. DATA STRUCTURES (Dictionary creation)
    new_entry = {
        "id": int(time.time() * 1000),
        "original": prompt
    }
    
    gemini_enhanced_prompt = ""
    
    # 4. FLOW CONTROLS (for loop)
    for char in prompt:
        gemini_enhanced_prompt += char
        
    gemini_enhanced_prompt = f"[Gemini Optimized] {gemini_enhanced_prompt}"
    new_entry["enhanced"] = gemini_enhanced_prompt
    
    # 3. DATA STRUCTURES (Appending to a List)
    prompt_history.append(new_entry)
    
    return jsonify({
        "success": True,
        "message": f"Prompt migrated from {ai_models['legacy']} to {ai_models['modern']}!",
        "data": new_entry,
        "historyCount": len(prompt_history)
    })

if __name__ == '__main__':
    print("========================================================")
    print(f"Starting Python backend on http://localhost:5000")
    print("Demonstrating Python Variables, Datatypes, Data Structures, and Flow Controls.")
    print("========================================================")
    app.run(port=5000, debug=True)
