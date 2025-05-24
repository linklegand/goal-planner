# Goal Planner API

This is a simple Flask API that generates a step-by-step action plan for a given personal development goal using OpenAI's GPT model.

## Endpoint

POST /generate_plan

### Request JSON body:

```json
{
  "goal": "提高英语口语",
  "duration": "3个月",
  "level": "初级",
  "time_per_day": "每天1小时"
} goal-planner
