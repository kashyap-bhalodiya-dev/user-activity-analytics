from fastapi import FastAPI

from app.pipeline import build_normalized_logs
from app.analytics import generate_analytics
from app.insights import generate_insights


app = FastAPI()


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "message": "User Activity Analytics backend is running"
    }


@app.get("/logs")
def get_logs():
    logs = build_normalized_logs("logs")

    return {
        "total_logs": len(logs),
        "logs": logs
    }


@app.get("/analytics")
def get_analytics():
    logs = build_normalized_logs("logs")
    analytics = generate_analytics(logs)

    return analytics


@app.get("/insights")
def get_insights():
    logs = build_normalized_logs("logs")
    analytics = generate_analytics(logs)
    insights = generate_insights(analytics)

    return {
        "insights": insights
    }


@app.get("/summary")
def get_summary():
    logs = build_normalized_logs("logs")
    analytics = generate_analytics(logs)
    insights = generate_insights(analytics)

    return {
        "total_logs": len(logs),
        "analytics": analytics,
        "insights": insights
    }