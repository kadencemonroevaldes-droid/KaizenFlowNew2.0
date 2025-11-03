diff --git a/README.md b/README.md
index 8a2719a3c39632b65e9bb750f2ae0d74b2680981..64e7c0e9814f3b1ce57ac87d2a11df4fc5956d65 100644
--- a/README.md
+++ b/README.md
@@ -1 +1,27 @@
-# KaizenFlowNew2.0
+# Kaizen Flow 2.0
+
+Kaizen Flow is a FastAPI-powered experience for exploring improvement ideas, tracking delivery, and highlighting cultural insights.
+
+## Getting started
+1. Install dependencies:
+   ```bash
+   pip install -r requirements.txt
+   ```
+2. Launch the development server:
+   ```bash
+   uvicorn app.main:app --reload
+   ```
+3. Open your browser to [http://localhost:8000](http://localhost:8000) to explore the dashboard, tracker, and culture lens.
+
+## UI gallery
+Recent screenshots captured from the refreshed experience:
+
+![Dashboard view](docs/screens/dashboard.png)
+![Tracker view](docs/screens/tracker.png)
+![Culture lens](docs/screens/culture.png)
+
+## Project structure
+- `app/main.py` – FastAPI application with routes and SQLite models.
+- `app/templates/` – Jinja templates for dashboard, tracker, and culture experiences.
+- `app/static/css/style.css` – shared styling and layout system.
+- `docs/screens/` – exported UI captures for quick visual reference.
