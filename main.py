from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/generate_plan", methods=["POST"])
def generate_plan():
    data = request.get_json()
    goal = data.get("goal", "")
    duration = data.get("duration", "")
    level = data.get("level", "")
    time_per_day = data.get("time_per_day", "")

    prompt = (
        f"你是一位专业的成长教练。请根据以下信息，制定一个清晰的、可执行的阶段任务清单：\n\n"
        f"目标：{goal}\n"
        f"持续时间：{duration}\n"
        f"当前水平：{level}\n"
        f"每天可投入时间：{time_per_day}\n\n"
        f"请将计划分为多个阶段，并以清晰的列表方式输出。"
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )

        plan = response["choices"][0]["message"]["content"]
        return jsonify({"success": True, "plan_raw": plan})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500
@app.route("/", methods=["GET"])
def home():
    return "服务运行中"
if __name__== "__main__":
    app.run(host="0.0.0.0",port=8000)
